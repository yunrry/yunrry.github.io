# 운영환경에 웹 기반 DB 관리 도구 컨테이너 실행하기


### 컨테이너 실행

```bash
# Adminer 컨테이너 추가
docker run -d \
  --name adminer \
  --network container:mysql \
  -e ADMINER_DEFAULT_SERVER=mysql \
  adminer:latest

# 또는 phpMyAdmin
docker run -d \
  --name phpmyadmin \
  --network container:mysql \
  -e PMA_HOST=mysql \
  -e PMA_PORT=3306 \
  phpmyadmin:latest
```

### nginx 설정
```nginx
server {
    listen 19909;
    
    # Spring Boot 애플리케이션
    location / {
        proxy_pass http://app-blue:8080/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
    
    # 웹 기반 DB 관리 도구
    location /adminer/ {
        proxy_pass http://adminer:8080/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

`http://address(orDN):19909/` → Spring Boot 애플리케이션  
`http://address(orDN)/db/` → 웹 기반 DB 관리 도구