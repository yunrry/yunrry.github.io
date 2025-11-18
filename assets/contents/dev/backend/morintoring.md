# Flik - Prometheus 설정

## 1. 프로젝트 디렉토리 구조

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

## 2. 상세 디렉토리

### 2.1 Prometheus 디렉토리
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

### 2.2 Grafana 디렉토리
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

## 3. 파일 생성 명령어

### 3.1 디렉토리 생성

```bash
# Flik 프로젝트 루트 디렉토리에서 실행
mkdir -p prometheus
mkdir -p grafana/provisioning/datasources
mkdir -p grafana/provisioning/dashboards
mkdir -p grafana/dashboards
```

### 3.2 prometheus/prometheus.yml 생성

```bash
cat > prometheus/prometheus.yml << 'EOF'
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  external_labels:
    monitor: 'flik-monitor'
    environment: 'production'

rule_files:
  - "alert.rules.yml"

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']
        labels:
          service: 'prometheus'

  - job_name: 'flik-blue'
    metrics_path: '/api/actuator/prometheus'
    scrape_interval: 10s
    static_configs:
      - targets: ['flik-blue:8080']
        labels:
          application: 'flik'
          environment: 'blue'
          service: 'flik-backend'
    relabel_configs:
      - source_labels: [__address__]
        target_label: instance
        replacement: 'flik-blue'

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
EOF
```

### 3.3 prometheus/alert.rules.yml 생성

```bash
cat > prometheus/alert.rules.yml << 'EOF'
groups:
  - name: flik_alerts
    interval: 30s
    rules:
      - alert: FlikApplicationDown
        expr: up{job=~"flik-.*"} == 0
        for: 1m
        labels:
          severity: critical
          service: flik
        annotations:
          summary: "Flik application {{ $labels.instance }} is down"
          description: "{{ $labels.instance }} has been down for more than 1 minute."

      - alert: HighMemoryUsage
        expr: (jvm_memory_used_bytes{area="heap"} / jvm_memory_max_bytes{area="heap"}) * 100 > 85
        for: 5m
        labels:
          severity: warning
          service: flik
        annotations:
          summary: "High memory usage on {{ $labels.instance }}"
          description: "Memory usage is above 85% (current: {{ $value }}%)"

      - alert: HighCpuUsage
        expr: process_cpu_usage * 100 > 80
        for: 5m
        labels:
          severity: warning
          service: flik
        annotations:
          summary: "High CPU usage on {{ $labels.instance }}"
          description: "CPU usage is above 80% (current: {{ $value }}%)"

      - alert: HighErrorRate
        expr: rate(http_server_requests_seconds_count{status=~"5.."}[5m]) > 0.05
        for: 5m
        labels:
          severity: warning
          service: flik
        annotations:
          summary: "High error rate on {{ $labels.instance }}"
          description: "Error rate is above 5% (current: {{ $value }})"

      - alert: DatabaseConnectionPoolLow
        expr: (hikaricp_connections_active / hikaricp_connections_max) * 100 > 80
        for: 5m
        labels:
          severity: warning
          service: flik
        annotations:
          summary: "Database connection pool running low on {{ $labels.instance }}"
          description: "Connection pool usage is above 80% (current: {{ $value }}%)"

      - alert: SlowResponseTime
        expr: histogram_quantile(0.95, rate(http_server_requests_seconds_bucket[5m])) > 2
        for: 5m
        labels:
          severity: warning
          service: flik
        annotations:
          summary: "Slow response time on {{ $labels.instance }}"
          description: "95th percentile response time is above 2 seconds (current: {{ $value }}s)"
EOF
```

### 3.4 grafana/provisioning/datasources/prometheus.yml 생성

```bash
cat > grafana/provisioning/datasources/prometheus.yml << 'EOF'
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
EOF
```

### 3.5 grafana/provisioning/dashboards/dashboard.yml 생성

```bash
cat > grafana/provisioning/dashboards/dashboard.yml << 'EOF'
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
EOF
```

### 3.6 docker-compose-monitoring.yml 생성

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


## 4. 파일 검증

### 디렉토리 구조 확인

```bash
tree prometheus grafana
```

```
prometheus
├── alert.rules.yml
└── prometheus.yml
grafana
├── dashboards
├── provisioning
│   ├── dashboards
│   │   └── dashboard.yml
│   └── datasources
│       └── prometheus.yml
```

## 5. 설정 파일 문법 검증

```bash
# Prometheus 설정 검증
docker run --rm -v $(pwd)/prometheus:/etc/prometheus prom/prometheus:v2.48.0 \
  promtool check config /etc/prometheus/prometheus.yml

# Alert 규칙 검증
docker run --rm -v $(pwd)/prometheus:/etc/prometheus prom/prometheus:v2.48.0 \
  promtool check rules /etc/prometheus/alert.rules.yml
```

## 6. 실행 및 확인

```bash
# 1. 모니터링 스택 시작
docker-compose -f docker-compose-monitoring.yml up -d

# 2. 로그 확인
docker-compose -f docker-compose-monitoring.yml logs -f

# 3. 컨테이너 상태 확인
docker-compose -f docker-compose-monitoring.yml ps

# 4. Prometheus 타겟 확인
curl http://localhost:9090/api/v1/targets

# 5. Grafana 접속
# 브라우저에서 http://localhost:3000
# ID: admin, PW: admin (또는 환경변수로 설정한 값)
```

## 7. 문제 해결

### 파일을 찾을 수 없다는 에러가 나는 경우

```bash
# 현재 위치 확인
pwd

# docker-compose.yml이 있는 디렉토리인지 확인
ls -la docker-compose*.yml

# prometheus 디렉토리 확인
ls -la prometheus/

# 볼륨 마운트 경로 확인
docker-compose -f docker-compose-monitoring.yml config
```

### 권한 문제가 발생하는 경우

```bash
# Grafana 데이터 디렉토리 권한 설정
sudo chown -R 472:472 grafana/

# Prometheus 데이터 디렉토리 권한 설정
sudo chown -R 65534:65534 prometheus/
```
