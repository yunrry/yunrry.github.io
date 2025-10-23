# Docker

## Dcoker 설치

RaspberryPi4 ARM64 ver

### 1. 시스템 업데이트
```bash
sudo apt update
sudo apt upgrade -y
```

### 2. 필요한 패키지 설치
```bash
sudo apt install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

### 3. Docker GPG 키 추가
```bash
sudo mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg  
sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

### 4. Docker 저장소 추가
```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/debian $(lsb_release -cs) stable"  
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### 5. Docker 설치
```bash
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### 6. 사용자를 docker 그룹에 추가
```bash
sudo usermod -aG docker $USER
```

### 7. Docker 서비스 시작 및 활성화
```bash
sudo systemctl start docker
sudo systemctl enable docker
```

### 8. 재로그인 또는 그룹 적용
```bash
newgrp docker
```

### 9. 설치 확인
```bash
docker --version
docker run hello-world
```

### 10. Docker Compose 확인
```bash
docker compose version
```

## 🔐 GPG (GNU Privacy Guard) 키
GPG (GNU Privacy Guard) 키는 디지털 서명을 위한 암호화 키이다.  
왜 필요한가?  
Docker GPG 키는 패키지 무결성과 보안을 보장하기 위해 사용된다:
1. 패키지 검증: 다운로드하는 Docker 패키지가 정말 Docker 공식에서 만든 것인지 확인
2. 변조 방지: 패키지가 중간에 악의적으로 수정되지 않았는지 검증
3. 신뢰성: 가짜 패키지나 악성 소프트웨어 설치 방지

```bash
curl -fsSL https://download.docker.com/linux/debian/gpg  
sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```
명령어 설명
1. Docker 공식 GPG 키 다운로드 (https://download.docker.com/linux/debian/gpg)
2. 키를 시스템에 저장 (/etc/apt/keyrings/docker.gpg)
3. apt가 이 키로 패키지 서명을 검증하도록 설정

**비유로 설명하면**
- GPG 키 = 도장/인감
- Docker 패키지 = 중요한 문서
- 서명 검증 = 문서에 찍힌 도장이 진짜인지 확인

**보안상 중요한 이유**  
GPG 키 없이 설치하면:
- 누구나 가짜 Docker 패키지를 만들어 배포할 수 있음
- 악성 코드가 포함된 패키지를 설치할 위험
- 시스템 보안이 크게 취약해짐
  
---  
<br><br>
# 명령어

컨테이너명/ID 확인
```bash
# 실행 중인 컨테이너 확인
docker ps

# 컨테이너 중지
docker stop [컨테이너명]

# 컨테이너 재시작
docker restart [컨테이너명]

# 컨테이너 삭제
docker rm [컨테이너명]

# 컨테이너 로그 확인
docker logs [컨테이너명]

# MySQL 컨테이너만 필터링
docker ps | grep mysql
```

컨테이너 로그 출력 옵션
```bash
# 특정 컨테이너 실시간 로그
docker logs -f app-blue

# 여러 컨테이너 동시 모니터링
docker compose logs -f app-blue app-green

# 최근 100줄부터 실시간
docker logs -f --tail 100 app-blue

# 타임스탬프 포함
docker logs -f -t app-blue
```
<br><br>

# 자주 사용하는 Image

## MySQL
docker 명령어로 생성
```bash
docker run -d --name mysql \
  -e MYSQL_ROOT_PASSWORD=root_password \
  -e MYSQL_USER=new_username \
  -e MYSQL_PASSWORD=new_password \
  -e MYSQL_DATABASE=your_db \
  -p 3306:3306 mysql:latest

```

Docker Compose 사용 시
```yaml
# docker-compose.yml
version: '3.8'
services:
  mysql:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: yourpassword
      MYSQL_DATABASE: testdb
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:
```

방법 1. 바로 접속
```bash
docker exec -it [컨테이너명] mysql -u [사용자] -p
```
방법 2. 컨테이너 bash세션 접속후 mysql접속
```bash
# 컨테이너에 bash로 접속
docker exec -it [컨테이너명] bash

# 컨테이너 내부에서 mysql 접속
mysql -u root -p
```



## Docker Compose 실행 옵션

### 전체 서비스 시작 (백그라운드)
```bash
docker compose up -d
```
### 특정 프로필로 시작 (Blue-Green 배포용)
```bash
# Blue 환경만 시작
docker compose --profile blue up -d

# Green 환경만 시작  
docker compose --profile green up -d

# 기본 인프라만 시작 (MySQL, Redis, Nginx)
docker compose up -d mysql redis nginx
```
### 로그와 함께 포그라운드 실행
```bash
docker compose up
```
### 환경 변수 설정 (필요시)
```bash
# 필요한 환경 변수들 설정
export MYSQL_ROOT_PASSWORD="your_password"
export MYSQL_DATABASE="your_database"
export MYSQL_USER="your_user"
export MYSQL_PASSWORD="your_password"

# 또는 .env 파일 생성
cat > .env << EOF
MYSQL_ROOT_PASSWORD=your_password
MYSQL_DATABASE=your_database
MYSQL_USER=your_user
MYSQL_PASSWORD=your_password
EOF
```
### 실행 후 상태 확인
```bash
# 컨테이너 상태 확인
docker compose ps

# 또는
docker ps

# 로그 확인
docker compose logs -f

# 특정 서비스 로그만 확인
docker compose logs mysql
docker compose logs flik-blue
```

<br><br>
---
`#Docker` `#RaspberryPi` `#ARM`


