# Flik - Grafana + Prometheus 설정

## 1. 아키텍처 개요
```
Spring Boot Application (Flik)
    ↓ (Actuator /metrics endpoint)
Prometheus (메트릭 수집 및 저장)
    ↓
Grafana (시각화 및 대시보드)
```

**메모리 사용량:**
```
Prometheus: 약 200-300MB
Grafana:    약 150-200MB
────────────────────────────
총합:       약 350-500MB
```
### 프로젝트 디렉토리 구조

```
flik-project/
├── docker-compose.yml                    # 기존 Flik 애플리케이션
├── docker-compose-monitoring.yml         # 새로 생성
├── prometheus/
│   ├── prometheus.yml                    # Prometheus 메인 설정
│   └── alert.rules.yml                   # 알림 규칙
├── grafana/
│   ├── provisioning/
│   │   ├── datasources/
│   │   │   └── prometheus.yml            # Grafana 데이터소스 설정
│   │   └── dashboards/
│   │       └── dashboard.yml             # 대시보드 프로비저닝 설정
│   └── dashboards/
│       ├── flik-overview.json            # 대시보드 JSON
│       └── flik-business.json            # 비즈니스 메트릭 대시보드
├── src/
├── Dockerfile
└── ...
```

### Prometheus 디렉토리
```
prometheus/
├── prometheus.yml       # Prometheus 메인 설정 파일
│                       # - 스크래핑 대상 정의
│                       # - 스크래핑 간격 설정
│                       # - 알림 규칙 파일 참조
│
└── alert.rules.yml     # 알림 규칙 정의
                        # - CPU, 메모리, 에러율 등의 알림 조건
```

### Grafana 디렉토리
```
grafana/
├── provisioning/                    # Grafana 자동 설정
│   ├── datasources/
│   │   └── prometheus.yml          # Prometheus 데이터소스 자동 등록
│   └── dashboards/
│       └── dashboard.yml           # 대시보드 파일 위치 지정
│
└── dashboards/                      # 실제 대시보드 JSON 파일들
    ├── flik-overview.json
    └── flik-business.json
```

## 2. 파일 생성 명령어

### 2.1 디렉토리 생성

```bash
# Flik 프로젝트 루트 디렉토리에서 실행
mkdir -p prometheus
mkdir -p grafana/provisioning/datasources
mkdir -p grafana/provisioning/dashboards
mkdir -p grafana/dashboards
```


### 2.6 docker-compose-monitoring.yml 생성

```bash
cat > docker-compose-monitoring.yml << 'EOF'
version: '3.8'

services:
  prometheus:
    image: prom/prometheus:v2.48.0
    container_name: flik-prometheus
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
      - ./prometheus/alert.rules.yml:/etc/prometheus/alert.rules.yml
      - prometheus-data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--storage.tsdb.retention.time=30d'
      - '--web.console.libraries=/usr/share/prometheus/console_libraries'
      - '--web.console.templates=/usr/share/prometheus/consoles'
      - '--web.enable-lifecycle'
    ports:
      - "9090:9090"
    networks:
      - goormthon-java_dormung-network
    restart: unless-stopped
    mem_limit: 512m
    healthcheck:
      test: ["CMD", "wget", "--quiet", "--tries=1", "--spider", "http://localhost:9090/-/healthy"]
      interval: 30s
      timeout: 10s
      retries: 3

  grafana:
    image: grafana/grafana:10.2.2
    container_name: flik-grafana
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_ADMIN_PASSWORD:-admin}
      - GF_USERS_ALLOW_SIGN_UP=false
      - GF_SERVER_ROOT_URL=http://localhost:3000
      - GF_INSTALL_PLUGINS=grafana-piechart-panel
    volumes:
      - grafana-data:/var/lib/grafana
      - ./grafana/provisioning:/etc/grafana/provisioning
      - ./grafana/dashboards:/var/lib/grafana/dashboards
    ports:
      - "3000:3000"
    networks:
      - goormthon-java_dormung-network
    depends_on:
      - prometheus
    restart: unless-stopped
    mem_limit: 384m
    healthcheck:
      test: ["CMD", "wget", "--quiet", "--tries=1", "--spider", "http://localhost:3000/api/health"]
      interval: 30s
      timeout: 10s
      retries: 3

volumes:
  prometheus-data:
    driver: local
  grafana-data:
    driver: local

networks:
  goormthon-java_dormung-network:
    external: true
EOF
```


## 3. Prometheus 설정

### 3.1 prometheus.yml
prometheus/prometheus.yml

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  external_labels:
    monitor: 'flik-monitor'
    environment: 'production'

# Alertmanager 설정 (선택사항)
# alerting:
#   alertmanagers:
#     - static_configs:
#         - targets: ['alertmanager:9093']

rule_files:
  - "alert.rules.yml"

scrape_configs:
  # Prometheus 자체 메트릭
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']
        labels:
          service: 'prometheus'

  # Flik Blue 애플리케이션
  - job_name: 'flik-blue'
    metrics_path: '/api/actuator/prometheus'
    scrape_interval: 10s
    static_configs:
      - targets: ['flik-blue:8080']
        labels:
          application: 'flik'
          environment: 'blue'
          service: 'flik-backend'
    # 헬스체크
    relabel_configs:
      - source_labels: [__address__]
        target_label: instance
        replacement: 'flik-blue'

  # Flik Green 애플리케이션
  - job_name: 'flik-green'
    metrics_path: '/api/actuator/prometheus'
    scrape_interval: 10s
    static_configs:
      - targets: ['flik-green:8080']
        labels:
          application: 'flik'
          environment: 'green'
          service: 'flik-backend'
    relabel_configs:
      - source_labels: [__address__]
        target_label: instance
        replacement: 'flik-green'

  # MySQL Exporter (선택사항)
  # - job_name: 'mysql'
  #   static_configs:
  #     - targets: ['mysql-exporter:9104']
  #       labels:
  #         service: 'mysql'

  # Redis Exporter (선택사항)
  # - job_name: 'redis'
  #   static_configs:
  #     - targets: ['redis-exporter:9121']
  #       labels:
  #         service: 'redis'

  # PostgreSQL Exporter (선택사항)
  # - job_name: 'postgresql'
  #   static_configs:
  #     - targets: ['postgres-exporter:9187']
  #       labels:
  #         service: 'postgresql'
```

### 3.2 alert.rules.yml
prometheus/alert.rules.yml

```yaml
groups:
  - name: flik_alerts
    interval: 30s
    rules:
      # 애플리케이션 다운 알림
      - alert: FlikApplicationDown
        expr: up{job=~"flik-.*"} == 0
        for: 1m
        labels:
          severity: critical
          service: flik
        annotations:
          summary: "Flik application {{ $labels.instance }} is down"
          description: "{{ $labels.instance }} has been down for more than 1 minute."

      # 높은 메모리 사용률
      - alert: HighMemoryUsage
        expr: (jvm_memory_used_bytes{area="heap"} / jvm_memory_max_bytes{area="heap"}) * 100 > 85
        for: 5m
        labels:
          severity: warning
          service: flik
        annotations:
          summary: "High memory usage on {{ $labels.instance }}"
          description: "Memory usage is above 85% (current: {{ $value }}%)"

      # 높은 CPU 사용률
      - alert: HighCpuUsage
        expr: process_cpu_usage * 100 > 80
        for: 5m
        labels:
          severity: warning
          service: flik
        annotations:
          summary: "High CPU usage on {{ $labels.instance }}"
          description: "CPU usage is above 80% (current: {{ $value }}%)"

      # 높은 에러율
      - alert: HighErrorRate
        expr: rate(http_server_requests_seconds_count{status=~"5.."}[5m]) > 0.05
        for: 5m
        labels:
          severity: warning
          service: flik
        annotations:
          summary: "High error rate on {{ $labels.instance }}"
          description: "Error rate is above 5% (current: {{ $value }})"

      # HikariCP 커넥션 부족
      - alert: DatabaseConnectionPoolLow
        expr: (hikaricp_connections_active / hikaricp_connections_max) * 100 > 80
        for: 5m
        labels:
          severity: warning
          service: flik
        annotations:
          summary: "Database connection pool running low on {{ $labels.instance }}"
          description: "Connection pool usage is above 80% (current: {{ $value }}%)"

      # 느린 응답 시간
      - alert: SlowResponseTime
        expr: histogram_quantile(0.95, rate(http_server_requests_seconds_bucket[5m])) > 2
        for: 5m
        labels:
          severity: warning
          service: flik
        annotations:
          summary: "Slow response time on {{ $labels.instance }}"
          description: "95th percentile response time is above 2 seconds (current: {{ $value }}s)"

      # Redis 연결 실패
      - alert: RedisConnectionFailed
        expr: up{job="redis"} == 0
        for: 2m
        labels:
          severity: critical
          service: redis
        annotations:
          summary: "Redis connection failed"
          description: "Cannot connect to Redis for more than 2 minutes."

      # 디스크 사용률 높음
      - alert: HighDiskUsage
        expr: (1 - (node_filesystem_avail_bytes / node_filesystem_size_bytes)) * 100 > 85
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High disk usage"
          description: "Disk usage is above 85% (current: {{ $value }}%)"
```

## 4. Grafana 설정

### 4.1 prometheus.yml
grafana/provisioning/datasources/prometheus.yml

```yaml
apiVersion: 1

datasources:
  - name: Prometheus
    type: prometheus
    access: proxy
    url: http://prometheus:9090
    isDefault: true
    editable: true
    jsonData:
      timeInterval: "15s"
      queryTimeout: "60s"
      httpMethod: "POST"
```

### 4.2 dashboard.yml
grafana/provisioning/dashboards/dashboard.yml
```yaml
apiVersion: 1

providers:
  - name: 'Flik Dashboards'
    orgId: 1
    folder: ''
    type: file
    disableDeletion: false
    updateIntervalSeconds: 30
    allowUiUpdates: true
    options:
      path: /var/lib/grafana/dashboards
      foldersFromFilesStructure: true
```

## 5. Spring Boot 설정 수정

### 5.1 application.yml (이미 설정된 부분 확인)

현재 설정에 추가로 필요한 부분:

```yaml
management:
  endpoints:
    web:
      exposure:
        include: health,metrics,prometheus,info,beans,env,hikaricp
      base-path: /actuator
  endpoint:
    health:
      show-details: always
      show-components: always
    metrics:
      enabled: true
    prometheus:
      enabled: true
  metrics:
    tags:
      application: ${spring.application.name}
      environment: ${DEPLOYMENT_ENV:unknown}
    enable:
      jvm: true
      system: true
      process: true
      hikaricp: true
      logback: true
      tomcat: true
    distribution:
      percentiles-histogram:
        http.server.requests: true
      percentiles:
        http.server.requests: 0.5, 0.95, 0.99
      slo:
        http.server.requests: 100ms,200ms,400ms,800ms,1s,2s,5s
```

### 5.2 build.gradle 의존성 추가 (이미 있는지 확인)

```gradle

dependencies {

    implementation 'org.springframework.boot:spring-boot-starter-actuator'
    implementation 'io.micrometer:micrometer-registry-prometheus'

}
```

## 6. 커스텀 메트릭 추가 (선택사항)

### 6.1 MeterRegistry를 활용한 비즈니스 메트릭

```java
package yunrry.flik.config;

import io.micrometer.core.instrument.Counter;
import io.micrometer.core.instrument.MeterRegistry;
import io.micrometer.core.instrument.Timer;
import org.springframework.stereotype.Component;

@Component
public class MetricsService {
    
    private final Counter swipeCounter;
    private final Counter recommendationCounter;
    private final Timer embeddingTimer;
    private final Counter cacheHitCounter;
    private final Counter cacheMissCounter;
    
    public MetricsService(MeterRegistry registry) {
        // 스와이프 카운터
        this.swipeCounter = Counter.builder("flik.swipe.count")
                .description("Total number of swipes")
                .tag("type", "user_interaction")
                .register(registry);
        
        // 추천 카운터
        this.recommendationCounter = Counter.builder("flik.recommendation.count")
                .description("Total number of recommendations generated")
                .register(registry);
        
        // 임베딩 생성 시간 측정
        this.embeddingTimer = Timer.builder("flik.embedding.duration")
                .description("Time taken to generate embeddings")
                .register(registry);
        
        // 캐시 히트
        this.cacheHitCounter = Counter.builder("flik.cache.hit")
                .description("Cache hit count")
                .register(registry);
        
        // 캐시 미스
        this.cacheMissCounter = Counter.builder("flik.cache.miss")
                .description("Cache miss count")
                .register(registry);
    }
    
    public void recordSwipe() {
        swipeCounter.increment();
    }
    
    public void recordRecommendation() {
        recommendationCounter.increment();
    }
    
    public Timer.Sample startEmbeddingTimer() {
        return Timer.start();
    }
    
    public void recordEmbeddingTime(Timer.Sample sample) {
        sample.stop(embeddingTimer);
    }
    
    public void recordCacheHit() {
        cacheHitCounter.increment();
    }
    
    public void recordCacheMiss() {
        cacheMissCounter.increment();
    }
}
```

### 6.2 사용 예시

```java
@Service
@RequiredArgsConstructor
public class RecommendationService {
    
    private final MetricsService metricsService;
    private final OpenAIEmbeddingService embeddingService;
    
    public List<Place> getRecommendations(UserPreference preference) {
        metricsService.recordRecommendation();
        
        // 임베딩 생성 시간 측정
        Timer.Sample sample = metricsService.startEmbeddingTimer();
        try {
            List<Double> embedding = embeddingService.createEmbedding(preference);
            metricsService.recordEmbeddingTime(sample);
            
            // ... 추천 로직
            return recommendations;
        } catch (Exception e) {
            metricsService.recordEmbeddingTime(sample);
            throw e;
        }
    }
}
```

## 7. Grafana 대시보드 JSON

### 7.1 grafana/dashboards/flik-overview.json

```json
{
    "title": "Flik Application Overview",
    "tags": ["flik", "spring-boot", "overview"],
    "timezone": "Asia/Seoul",
    "panels": [
      {
        "title": "Application Status",
        "type": "stat",
        "targets": [
          {
            "expr": "up{job=~\"flik-.*\"}",
            "legendFormat": "{{instance}}"
          }
        ],
        "gridPos": {"h": 4, "w": 6, "x": 0, "y": 0}
      },
      {
        "title": "Request Rate (req/s)",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(http_server_requests_seconds_count{application=\"flik\"}[5m])",
            "legendFormat": "{{method}} {{uri}} ({{status}})"
          }
        ],
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 4}
      },
      {
        "title": "Response Time (95th percentile)",
        "type": "graph",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(http_server_requests_seconds_bucket{application=\"flik\"}[5m]))",
            "legendFormat": "95th percentile"
          }
        ],
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 4}
      },
      {
        "title": "JVM Memory Usage",
        "type": "graph",
        "targets": [
          {
            "expr": "jvm_memory_used_bytes{area=\"heap\"}",
            "legendFormat": "{{instance}} - Used"
          },
          {
            "expr": "jvm_memory_max_bytes{area=\"heap\"}",
            "legendFormat": "{{instance}} - Max"
          }
        ],
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 12}
      },
      {
        "title": "CPU Usage",
        "type": "graph",
        "targets": [
          {
            "expr": "process_cpu_usage * 100",
            "legendFormat": "{{instance}}"
          }
        ],
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 12}
      },
      {
        "title": "HikariCP Active Connections",
        "type": "graph",
        "targets": [
          {
            "expr": "hikaricp_connections_active",
            "legendFormat": "{{instance}} - {{pool}}"
          },
          {
            "expr": "hikaricp_connections_max",
            "legendFormat": "{{instance}} - Max"
          }
        ],
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 20}
      },
      {
        "title": "HTTP Status Codes",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(http_server_requests_seconds_count{status=~\"2..\"}[5m])",
            "legendFormat": "2xx - {{instance}}"
          },
          {
            "expr": "rate(http_server_requests_seconds_count{status=~\"4..\"}[5m])",
            "legendFormat": "4xx - {{instance}}"
          },
          {
            "expr": "rate(http_server_requests_seconds_count{status=~\"5..\"}[5m])",
            "legendFormat": "5xx - {{instance}}"
          }
        ],
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 20}
      }
    ]
}

```

### 7.2 Flik 특화 대시보드 (grafana/dashboards/flik-business.json)

```json
{
    "title": "Flik Business Metrics",
    "tags": ["flik", "business"],
    "panels": [
      {
        "title": "Total Swipes",
        "type": "stat",
        "targets": [
          {
            "expr": "flik_swipe_count_total",
            "legendFormat": "Total Swipes"
          }
        ],
        "gridPos": {"h": 4, "w": 6, "x": 0, "y": 0}
      },
      {
        "title": "Recommendations Generated",
        "type": "stat",
        "targets": [
          {
            "expr": "flik_recommendation_count_total",
            "legendFormat": "Total Recommendations"
          }
        ],
        "gridPos": {"h": 4, "w": 6, "x": 6, "y": 0}
      },
      {
        "title": "Cache Hit Rate",
        "type": "gauge",
        "targets": [
          {
            "expr": "(flik_cache_hit_total / (flik_cache_hit_total + flik_cache_miss_total)) * 100",
            "legendFormat": "Hit Rate %"
          }
        ],
        "gridPos": {"h": 4, "w": 6, "x": 12, "y": 0}
      },
      {
        "title": "Embedding Generation Time",
        "type": "graph",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(flik_embedding_duration_seconds_bucket[5m]))",
            "legendFormat": "95th percentile"
          },
          {
            "expr": "histogram_quantile(0.50, rate(flik_embedding_duration_seconds_bucket[5m]))",
            "legendFormat": "50th percentile"
          }
        ],
        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 4}
      },
      {
        "title": "Swipe Rate (per minute)",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(flik_swipe_count_total[1m]) * 60",
            "legendFormat": "Swipes/min"
          }
        ],
        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 4}
      }
    ]
  
}
```



### 8 모니터링 스택 실행

```bash
# 모니터링 스택 시작
docker-compose -f docker-compose-monitoring.yml up -d

# 로그 확인
docker-compose -f docker-compose-monitoring.yml logs -f

# 상태 확인
docker-compose -f docker-compose-monitoring.yml ps
```

### 8.1 Flik 애플리케이션 재시작 (Actuator 엔드포인트 활성화)

```bash
# Blue 환경 재시작
docker-compose --profile blue restart flik-blue

# 메트릭 엔드포인트 확인
curl http://localhost:8083/api/actuator/prometheus
```

## 9. 접속 및 확인

### 9.1 Prometheus

```
URL: http://localhost:9090
```

**확인할 쿼리:**
```promql
# Flik 애플리케이션 상태
up{job=~"flik-.*"}

# 요청 수
rate(http_server_requests_seconds_count[5m])

# 메모리 사용률
(jvm_memory_used_bytes{area="heap"} / jvm_memory_max_bytes{area="heap"}) * 100

# HikariCP 커넥션
hikaricp_connections_active
```

### 9.2 Grafana

```
URL: http://localhost:3000
기본 로그인: admin / admin (또는 설정한 비밀번호)
```

**초기 설정:**
1. 로그인
2. Configuration → Data Sources → Prometheus 확인 (자동 프로비저닝됨)
3. Dashboards → Browse → Import dashboard
4. 대시보드 JSON 파일 업로드 또는 직접 작성

## 10. 유용한 Prometheus 쿼리 모음

```promql
# === 애플리케이션 상태 ===
# 애플리케이션 Up/Down 상태
up{job=~"flik-.*"}

# === HTTP 메트릭 ===
# 초당 요청 수
rate(http_server_requests_seconds_count[5m])

# 응답 시간 (95th percentile)
histogram_quantile(0.95, rate(http_server_requests_seconds_bucket[5m]))

# 에러율
rate(http_server_requests_seconds_count{status=~"5.."}[5m]) / rate(http_server_requests_seconds_count[5m])

# === JVM 메트릭 ===
# Heap 메모리 사용률
(jvm_memory_used_bytes{area="heap"} / jvm_memory_max_bytes{area="heap"}) * 100

# GC 횟수
rate(jvm_gc_pause_seconds_count[5m])

# GC 시간
rate(jvm_gc_pause_seconds_sum[5m])

# 스레드 수
jvm_threads_live_threads

# === 데이터베이스 ===
# HikariCP 활성 커넥션
hikaricp_connections_active

# HikariCP 대기 중인 스레드
hikaricp_connections_pending

# HikariCP 커넥션 사용률
(hikaricp_connections_active / hikaricp_connections_max) * 100

# 커넥션 획득 시간
rate(hikaricp_connections_acquire_seconds_sum[5m]) / rate(hikaricp_connections_acquire_seconds_count[5m])

# === 시스템 메트릭 ===
# CPU 사용률
process_cpu_usage * 100

# 시스템 CPU 사용률
system_cpu_usage * 100

# === 커스텀 비즈니스 메트릭 ===
# 스와이프 속도
rate(flik_swipe_count_total[1m]) * 60

# 추천 생성 속도
rate(flik_recommendation_count_total[1m]) * 60

# 캐시 히트율
(flik_cache_hit_total / (flik_cache_hit_total + flik_cache_miss_total)) * 100

# 임베딩 생성 평균 시간
rate(flik_embedding_duration_seconds_sum[5m]) / rate(flik_embedding_duration_seconds_count[5m])
```

## 11. 알림 테스트

```bash
# Prometheus 설정 리로드
curl -X POST http://localhost:9090/-/reload

# 알림 규칙 확인
curl http://localhost:9090/api/v1/rules

# 활성 알림 확인
curl http://localhost:9090/api/v1/alerts
```

## 12. 모니터링 대시보드 추천 레이아웃

### Row 1: 시스템 상태
- Application Status (Up/Down)
- Total Requests
- Error Rate
- Average Response Time

### Row 2: 성능 메트릭
- Request Rate Graph
- Response Time (P50, P95, P99)
- HTTP Status Codes Distribution

### Row 3: JVM 메트릭
- Heap Memory Usage
- Non-Heap Memory Usage
- GC Pause Time
- Thread Count

### Row 4: 데이터베이스
- HikariCP Active Connections
- Connection Pool Usage %
- Connection Acquire Time
- Query Execution Time

### Row 5: 비즈니스 메트릭
- Swipe Count
- Recommendation Count
- Cache Hit Rate
- Embedding Generation Time



###  prometheus/prometheus.yml
- what is Exporter?
ex) MySQL Exporter

## 13 Prometheus/Grafana 데이터 지속성
```yml
# docker-compose-monitoring.yml
prometheus:
  image: prom/prometheus
  volumes:
    - prometheus-data:/prometheus # 볼륨 넣기

grafana:
  image: grafana/grafana
  volumes:
    - grafana-data:/var/lib/grafana # 볼륨 넣기

volumes:
  prometheus-data:
    driver: local
  grafana-data:
    driver: local
```

### 데이터 저장 위치
- **컨테이너 내부**: `/prometheus` 디렉터리
- **TSDB 형식**: 시계열 데이터베이스로 효율적 저장
- **기본 보관기간**: 15일 (설정 가능)


### 복원 과정

**1. 컨테이너 재시작 시**
```bash
docker-compose -f docker-compose-monitoring.yml down
docker-compose -f docker-compose-monitoring.yml up -d
```

**2. 자동 복원 내용**
- **Prometheus**: 모든 메트릭 히스토리
- **Grafana**: 대시보드, 데이터소스 설정, 알림 규칙

**3. 볼륨 확인**
```bash
# 볼륨 목록 확인
docker volume ls

# Prometheus 데이터 확인
docker exec -it flik-prometheus ls -la /prometheus

# Grafana 데이터 확인
docker exec -it flik-grafana ls -la /var/lib/grafana
```

### 백업 방법

```bash
# Prometheus 데이터 백업
docker run --rm -v prometheus-data:/data -v $(pwd):/backup ubuntu tar czf /backup/prometheus-backup.tar.gz /data

# Grafana 데이터 백업
docker run --rm -v grafana-data:/data -v $(pwd):/backup ubuntu tar czf /backup/grafana-backup.tar.gz /data
```

```java
@Configuration
public class MetricsConfig {

    @Bean
    public MeterRegistryCustomizer<MeterRegistry> metricsCommonTags() {
        return registry -> {
            registry.config()
                    .commonTags("application", "flik", "environment", "local")
                    .meterFilter(MeterFilter.deny(id -> {
                        // 불필요한 메트릭 제외
                        String name = id.getName();
                        return name.startsWith("jvm.gc.pause") ||
                                name.startsWith("jvm.buffer");
                    }))
                    .meterFilter(MeterFilter.accept()); // 모든 HTTP 메트릭 허용
        };
    }

    @Bean
    public Timer.Builder customTimerBuilder() {
        return Timer.builder("http.server.requests")
                .publishPercentiles(0.5, 0.95, 0.99)
                .publishPercentileHistogram();
    }
}
```

## Prometheus에서 사용할 시계열 쿼리

### 1. 기본 HTTP 요청 수 (누적)
```promql
http_server_requests_seconds_count{application="flik"}
```

### 2. 초당 요청률 (Request Rate)
```promql
rate(http_server_requests_seconds_count{application="flik"}[5m])
```

### 3. URI별 요청 통계
```promql
rate(http_server_requests_seconds_count{application="flik",uri="/api/v1/swipe"}[5m])
```

### 4. 상태코드별 요청률
```promql
# 성공 요청 (2xx)
rate(http_server_requests_seconds_count{application="flik",status=~"2.."}[5m])

# 에러 요청 (4xx, 5xx)
rate(http_server_requests_seconds_count{application="flik",status=~"[45].."}[5m])
```

### 5. 응답시간 분포 (히스토그램)
```promql
# 95th percentile 응답시간
histogram_quantile(0.95, rate(http_server_requests_seconds_bucket{application="flik"}[5m]))

# 평균 응답시간
rate(http_server_requests_seconds_sum{application="flik"}[5m]) / rate(http_server_requests_seconds_count{application="flik"}[5m])
```


## 도메인 path 설정
```nginx
        location /prometheus/ {
            proxy_pass http://prometheus/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_http_version 1.1;
            proxy_set_header Connection "";
            
            # Prometheus 웹 UI 경로 수정
            sub_filter_once off;
            sub_filter '"/' '"/prometheus/';
        }

        # Grafana 모니터링
        location /grafana/ {
            proxy_pass http://grafana/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_http_version 1.1;
            proxy_set_header Connection "";
            
            # Grafana에서 subpath 처리
            proxy_set_header X-Forwarded-Host $host;
            proxy_set_header X-Forwarded-Server $host;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
```

***접속 URL***
- Prometheus: https://flikapp.org/prometheus/
- Grafana: https://flikapp.org/grafana/
- 기존 Flik API: https://flikapp.org/api/
- Actuator: https://flikapp.org/actuator/
- DB 관리: https://flikapp.org/db/

## 보안 : Basic Auth 없을 때 vs 있을 때

**Basic Auth를 추가하면 모니터링 도구에 접근할 때 추가 보안 레이어가 생긴다다.**

### 실제 차이점

### 1. 브라우저 접근
**Basic Auth 없을 때:**
- `https://flikapp.org/prometheus/` → 바로 Prometheus UI 화면

**Basic Auth 있을 때:**
- `https://flikapp.org/prometheus/` → 브라우저 로그인 팝업
- 아이디/비밀번호 입력 후 → Prometheus UI 화면

### 2. API 호출
**Basic Auth 없을 때:**
```bash
# 메트릭 데이터 바로 조회 가능
curl -s "https://flikapp.org/prometheus/api/v1/query?query=up"
```

**Basic Auth 있을 때:**
```bash
# 401 Unauthorized 에러
curl -s "https://flikapp.org/prometheus/api/v1/query?query=up"

# 인증 정보 포함해야 함
curl -s -u "admin:password123" "https://flikapp.org/prometheus/api/v1/query?query=up"
```



## Basic Auth 설정 방법

### 1. htpasswd 파일 생성

**방법1**
```bash
# 운영 서버에서 패스워드 파일 생성
sudo docker exec nginx sh -c '
echo -n "admin:" > /etc/nginx/.htpasswd
echo "password123" | openssl passwd -apr1 -stdin >> /etc/nginx/.htpasswd
'

# 생성된 파일 확인
sudo docker exec nginx cat /etc/nginx/.htpasswd
# 출력: admin:$apr1$salt$hashedpassword
```

-> 라즈베리파이 sk브로드밴드가 포트 안뚤어줘서 openssl 설치 못함 이슈

**방법2: apache2-utils로 대체**
```bash
# 1. 호스트에 apache2-utils 설치
sudo apt-get update && sudo apt-get install -y apache2-utils

# 2. htpasswd 파일 생성 (interactive 모드)
sudo htpasswd -c /tmp/.htpasswd admin
# 비밀번호 입력: password

# 3. 또는 한 번에 생성 (non-interactive)
sudo htpasswd -cb /tmp/.htpasswd admin password

# 4. 생성된 파일 확인
cat /tmp/.htpasswd
# 출력 예: admin:$apr1$salt$hashedpassword

# 5. Nginx 컨테이너로 복사
sudo docker cp /tmp/.htpasswd nginx:/etc/nginx/.htpasswd

# 6. 권한 설정
sudo docker exec nginx chmod 644 /etc/nginx/.htpasswd

# 7. 확인
sudo docker exec nginx cat /etc/nginx/.htpasswd

# 8. 환경변수 설정
export PROMETHEUS_BASIC_AUTH_USER="admin"
export PROMETHEUS_BASIC_AUTH_PASSWORD="password"
```

### 2. Nginx 설정에 Basic Auth 추가

```nginx
# Prometheus 보안 (읽기 전용)
location /prometheus/ {
    auth_basic "Prometheus Monitoring";
    auth_basic_user_file /etc/nginx/.htpasswd;
    
    proxy_pass http://prometheus/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_http_version 1.1;
    proxy_set_header Connection "";
    
    sub_filter_once off;
    sub_filter '"/' '"/prometheus/';
}

# Grafana는 자체 로그인이 있으므로 선택사항
location /grafana/ {
    # auth_basic "Grafana Dashboard";
    # auth_basic_user_file /etc/nginx/.htpasswd;
    
    proxy_pass http://grafana/;
    # ... 나머지 설정
}
```



### 3. Grafana 데이터소스 설정

**Basic Auth 없을 때:**
```yaml
# grafana/provisioning/datasources/prometheus.yml
apiVersion: 1
datasources:
  - name: Prometheus
    type: prometheus
    access: proxy
    url: http://flik-prometheus:9090
```

**Basic Auth 있을 때:**
```yaml
# grafana/provisioning/datasources/prometheus.yml
apiVersion: 1
datasources:
  - name: Prometheus
    type: prometheus
    access: proxy
    url: http://flik-prometheus:9090
    basicAuth: true
    basicAuthUser: admin
    secureJsonData:
      basicAuthPassword: password123 # 하드코딩 금지
```

## 보안 레벨 비교

### 1. 현재 상태 (Basic Auth 없음)
- **장점**: 간편한 접근, 개발/테스트 용이
- **단점**: 누구나 모니터링 데이터 접근 가능

### 2. Basic Auth 추가
- **장점**: 추가 보안 레이어, 간단한 설정
- **단점**: 매번 인증 필요, 비밀번호 관리

### 3. 보안 설정

```nginx
# 운영 환경에 적합한 설정
location /prometheus/ {
    # IP 제한도 추가 (회사 IP만)
    allow 123.123.123.123;  # 개발팀 IP
    deny all;
    
    auth_basic "Prometheus Monitoring";
    auth_basic_user_file /etc/nginx/.htpasswd;
    
    proxy_pass http://prometheus/;
    # ... 나머지 설정
}

# Grafana는 자체 보안이 충분
location /grafana/ {
    # Basic Auth 불필요 (Grafana 자체 로그인 사용)
    proxy_pass http://grafana/;
    # ... 나머지 설정
}
```

### 등록된 메트릭 목록 조회
```bash
curl http://localhost:8080/api/actuator/metrics
```

```

{"names":
["application.ready.time",
"application.started.time",
"cache.gets",
"cache.lock.duration",
"cache.puts",
"cache.removals",
"disk.free",
"disk.total",
"embedding_generation_count_total",
"embedding_generation_time",
"executor.active",
"executor.completed",
"executor.pool.core",
"executor.pool.max",
"executor.pool.size",
"executor.queue.remaining",
"executor.queued",
"hikaricp.connections",
"hikaricp.connections.acquire",
"hikaricp.connections.active",
"hikaricp.connections.creation",
"hikaricp.connections.idle",
"hikaricp.connections.max",
"hikaricp.connections.min",
"hikaricp.connections.pending",
"hikaricp.connections.timeout",
"hikaricp.connections.usage",
"http.server.requests",
"http.server.requests.active",
"jdbc.connections.active",
"jdbc.connections.idle",
"jdbc.connections.max",
"jdbc.connections.min",
"jvm.classes.loaded",
"jvm.classes.unloaded",
"jvm.compilation.time",
"jvm.gc.concurrent.phase.time",
"jvm.gc.live.data.size",
"jvm.gc.max.data.size",
"jvm.gc.memory.allocated",
"jvm.gc.memory.promoted",
"jvm.gc.overhead",
"jvm.info",
"jvm.memory.committed",
"jvm.memory.max",
"jvm.memory.usage.after.gc",
"jvm.memory.used",
"jvm.threads.daemon",
"jvm.threads.live",
"jvm.threads.peak",
"jvm.threads.started",
"jvm.threads.states",
"lettuce.command.completion",
"lettuce.command.firstresponse",
"logback.events",
"process.cpu.time",
"process.cpu.usage",
"process.files.max",
"process.files.open",
"process.start.time",
"process.uptime",
"spring.data.repository.invocations",
"spring.security.authorizations",
"spring.security.authorizations.active",
"spring.security.filterchains",
"spring.security.filterchains.JwtAuthenticationFilter.after",
"spring.security.filterchains.JwtAuthenticationFilter.before",
"spring.security.filterchains.access.exceptions.after",
"spring.security.filterchains.access.exceptions.before",
"spring.security.filterchains.active",
"spring.security.filterchains.authentication.anonymous.after",
"spring.security.filterchains.authentication.anonymous.before",
"spring.security.filterchains.authorization.after",
"spring.security.filterchains.authorization.before",
"spring.security.filterchains.context.async.after",
"spring.security.filterchains.context.async.before",
"spring.security.filterchains.context.holder.after",
"spring.security.filterchains.context.holder.before",
"spring.security.filterchains.context.servlet.after",
"spring.security.filterchains.context.servlet.before",
"spring.security.filterchains.cors.after",
"spring.security.filterchains.cors.before",
"spring.security.filterchains.header.after",
"spring.security.filterchains.header.before",
"spring.security.filterchains.logout.after",
"spring.security.filterchains.logout.before",
"spring.security.filterchains.requestcache.after",
"spring.security.filterchains.requestcache.before",
"spring.security.filterchains.session.management.after",
"spring.security.filterchains.session.management.before",
"spring.security.filterchains.session.urlencoding.after",
"spring.security.filterchains.session.urlencoding.before",
"spring.security.http.secured.requests",
"spring.security.http.secured.requests.active",
"system.cpu.count",
"system.cpu.usage",
"system.load.average.1m",
"tomcat.sessions.active.current",
"tomcat.sessions.active.max",
"tomcat.sessions.alive.max",
"tomcat.sessions.created",
"tomcat.sessions.expired",
"tomcat.sessions.rejected",
"user_spot_save_count_total",
"user_swipe_count_total"]}%                                                 
```
