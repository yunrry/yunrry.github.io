# 15. 웹소켓 (WebSocket)

## 📌 개념

```
양방향 실시간 통신 프로토콜
- 클라이언트 ↔ 서버 동시 통신
- 지속적인 연결 유지
- 낮은 지연시간
```

### HTTP vs WebSocket

```
HTTP (요청-응답):
Client: "데이터 주세요"
Server: "여기 있어요"
Client: "또 데이터 주세요"
Server: "또 줄게요"
(매번 새로운 연결)

WebSocket (양방향):
Client ↔ Server (연결 유지)
Client: "메시지1"
Server: "메시지2"
Server: "메시지3" (서버가 먼저!)
Client: "메시지4"
(하나의 연결로 계속 통신)
```

---

## 🔄 WebSocket 동작 과정

### 1. 핸드셰이크 (Handshake)

```
HTTP로 시작하여 WebSocket으로 업그레이드

1. 클라이언트 요청:
GET /chat HTTP/1.1
Host: example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Sec-WebSocket-Version: 13

2. 서버 응답:
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=

3. WebSocket 연결 확립 ✅
```

### 2. 데이터 전송

```
프레임 (Frame) 단위로 전송

Frame 구조:
┌─────────┬─────────┬──────────┐
│ Header  │ Payload │          │
│ (2-14B) │ Length  │ Payload  │
└─────────┴─────────┴──────────┘

Frame 종류:
- 텍스트 프레임 (Text)
- 바이너리 프레임 (Binary)
- 제어 프레임 (Ping, Pong, Close)
```

### 3. 연결 종료

```
1. 클라이언트 또는 서버가 Close 프레임 전송
2. 상대방이 Close 프레임으로 응답
3. TCP 연결 종료
```

---

## 💻 WebSocket 구현

### 클라이언트 (JavaScript)

```javascript
// WebSocket 연결
const socket = new WebSocket('ws://localhost:8080');

// 연결 성공
socket.onopen = (event) => {
  console.log('Connected to WebSocket');
  socket.send('Hello Server!');
};

// 메시지 수신
socket.onmessage = (event) => {
  console.log('Received:', event.data);
  
  // JSON 파싱
  const data = JSON.parse(event.data);
  console.log(data);
};

// 에러 발생
socket.onerror = (error) => {
  console.error('WebSocket Error:', error);
};

// 연결 종료
socket.onclose = (event) => {
  console.log('Disconnected from WebSocket');
  console.log('Code:', event.code);
  console.log('Reason:', event.reason);
};

// 메시지 전송
function sendMessage(message) {
  if (socket.readyState === WebSocket.OPEN) {
    socket.send(message);
  } else {
    console.log('WebSocket is not open');
  }
}

// 연결 상태
// WebSocket.CONNECTING (0): 연결 중
// WebSocket.OPEN (1): 연결됨
// WebSocket.CLOSING (2): 닫는 중
// WebSocket.CLOSED (3): 닫힘

// 연결 종료
socket.close();
```

### 서버 (Node.js - ws 라이브러리)

```javascript
const WebSocket = require('ws');

// WebSocket 서버 생성
const wss = new WebSocket.Server({ port: 8080 });

// 연결된 클라이언트 목록
const clients = new Set();

// 클라이언트 연결
wss.on('connection', (ws) => {
  console.log('Client connected');
  clients.add(ws);
  
  // 메시지 수신
  ws.on('message', (message) => {
    console.log('Received:', message.toString());
    
    // 모든 클라이언트에게 브로드캐스트
    clients.forEach((client) => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(message.toString());
      }
    });
  });
  
  // 연결 종료
  ws.on('close', () => {
    console.log('Client disconnected');
    clients.delete(ws);
  });
  
  // 에러 처리
  ws.on('error', (error) => {
    console.error('WebSocket Error:', error);
  });
  
  // 환영 메시지
  ws.send(JSON.stringify({
    type: 'welcome',
    message: 'Connected to WebSocket server'
  }));
});

// Ping/Pong (연결 유지)
setInterval(() => {
  clients.forEach((ws) => {
    if (ws.isAlive === false) {
      ws.terminate();
      return;
    }
    ws.isAlive = false;
    ws.ping();
  });
}, 30000);

console.log('WebSocket server running on port 8080');
```

### 실전 예시: 채팅 애플리케이션

```javascript
// 클라이언트
const socket = new WebSocket('ws://localhost:8080');
const messagesDiv = document.getElementById('messages');
const input = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');

// 연결 성공
socket.onopen = () => {
  addMessage('System', 'Connected to chat');
};

// 메시지 수신
socket.onmessage = (event) => {
  const data = JSON.parse(event.data);
  
  switch (data.type) {
    case 'message':
      addMessage(data.username, data.text);
      break;
    case 'userJoined':
      addMessage('System', `${data.username} joined`);
      break;
    case 'userLeft':
      addMessage('System', `${data.username} left`);
      break;
  }
};

// 메시지 전송
sendButton.onclick = () => {
  const message = input.value.trim();
  if (message && socket.readyState === WebSocket.OPEN) {
    socket.send(JSON.stringify({
      type: 'message',
      text: message
    }));
    input.value = '';
  }
};

// 메시지 표시
function addMessage(username, text) {
  const messageEl = document.createElement('div');
  messageEl.innerHTML = `<strong>${username}:</strong> ${text}`;
  messagesDiv.appendChild(messageEl);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
}
```

---

## 🆚 WebSocket vs 다른 기술

### 1. WebSocket vs HTTP Polling

```
HTTP Polling (단기 폴링):
Client: "업데이트 있어?" (요청)
Server: "없어" (응답)
(3초 대기)
Client: "업데이트 있어?" (요청)
Server: "없어" (응답)
(3초 대기)
Client: "업데이트 있어?" (요청)
Server: "있어! 데이터" (응답)

문제:
❌ 불필요한 요청 많음
❌ 서버 부하
❌ 지연시간

WebSocket:
Client ↔ Server (연결 유지)
Server: "데이터" (즉시 전송!)

장점:
✅ 실시간
✅ 효율적
✅ 낮은 지연
```

### 2. WebSocket vs Long Polling

```
Long Polling:
Client: "업데이트 있으면 알려줘" (요청)
Server: (대기... 대기...)
Server: "있어! 데이터" (응답)
Client: "또 업데이트 있으면 알려줘" (요청)
Server: (대기... 대기...)

장점:
✅ Polling보다 효율적

단점:
❌ 연결 재수립 필요
❌ WebSocket보다 복잡

WebSocket이 더 나음 ✅
```

### 3. WebSocket vs Server-Sent Events (SSE)

```
SSE:
- 서버 → 클라이언트 (단방향)
- HTTP 기반
- 텍스트만

Client ← Server

WebSocket:
- 양방향
- 자체 프로토콜
- 텍스트/바이너리

Client ↔ Server

선택:
- 서버 푸시만 필요 → SSE
- 양방향 필요 → WebSocket ✅
```

---

## 🎯 WebSocket 사용 사례

### 1. 실시간 채팅

```
카카오톡, Slack, Discord

특징:
- 즉시 메시지 전달
- 읽음 표시
- 타이핑 표시

효과:
✅ 실시간 소통
✅ 낮은 지연
```

### 2. 실시간 알림

```
Facebook, Twitter 알림

특징:
- 새 메시지
- 좋아요
- 댓글

효과:
✅ 즉시 알림
✅ 사용자 참여
```

### 3. 실시간 협업 도구

```
Google Docs, Figma, Notion

특징:
- 동시 편집
- 실시간 동기화
- 커서 위치 공유

효과:
✅ 원활한 협업
✅ 충돌 방지
```

### 4. 온라인 게임

```
멀티플레이어 게임

특징:
- 플레이어 위치
- 게임 상태
- 채팅

효과:
✅ 낮은 지연
✅ 동기화
```

### 5. 주식/암호화폐 거래

```
실시간 가격 정보

특징:
- 가격 변동
- 체결 내역
- 차트 업데이트

효과:
✅ 실시간 정보
✅ 빠른 거래
```

### 6. IoT (사물인터넷)

```
스마트홈, 센서 데이터

특징:
- 센서 값
- 제어 명령
- 상태 모니터링

효과:
✅ 실시간 제어
✅ 즉각 반응
```

---

## 🔐 WebSocket 보안

### 1. WSS (WebSocket Secure)

```
HTTPS처럼 암호화된 WebSocket

ws://  → 암호화 안 됨 ❌
wss:// → 암호화됨 ✅

사용:
const socket = new WebSocket('wss://example.com');

효과:
- 데이터 암호화
- 중간자 공격 방지
```

### 2. 인증 (Authentication)

```
연결 시 토큰 전송

// 클라이언트
const token = localStorage.getItem('authToken');
const socket = new WebSocket(`wss://example.com?token=${token}`);

웹소켓 보안에 관한 이어지는 부분을 작성해드리겠습니다.

```
// 또는 연결 후 전송
socket.onopen = () => {
  socket.send(JSON.stringify({ 
    type: 'auth', 
    token: token 
  }));
};

// 서버
wss.on('connection', (ws, req) => {
  // URL 파라미터에서 토큰 확인
  const url = new URL(req.url, 'wss://example.com');
  const token = url.searchParams.get('token');
  
  if (!validateToken(token)) {
    ws.close(1008, '인증 실패');
    return;
  }
  
  // 또는 메시지로 받은 토큰 확인
  ws.on('message', (message) => {
    const data = JSON.parse(message);
    if (data.type === 'auth') {
      if (!validateToken(data.token)) {
        ws.close(1008, '인증 실패');
      }
    }
  });
});
```

### 3. 입력 검증 (Input Validation)
```
// 클라이언트에서 전송된 데이터 검증
ws.on('message', (message) => {
  try {
    // JSON 형식 확인
    const data = JSON.parse(message);
    
    // 데이터 유효성 검사
    if (!data.type || !data.message) {
      throw new Error('잘못된 메시지 형식');
    }
    
    // XSS 방지 (특수문자 이스케이프)
    const sanitizedMessage = sanitizeHtml(data.message);
    
    // 처리 계속...
  } catch (error) {
    console.error('메시지 검증 실패:', error);
  }
});
```

### 4. 속도 제한 (Rate Limiting)
```
// 클라이언트별 메시지 횟수 제한
const messageCount = new Map();

wss.on('connection', (ws, req) => {
  // 클라이언트 IP 또는 식별자
  const clientId = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
  
  // 초기 카운트 설정
  messageCount.set(clientId, 0);
  
  // 1분마다 카운트 초기화
  const interval = setInterval(() => {
    messageCount.set(clientId, 0);
  }, 60000);
  
  ws.on('message', () => {
    // 현재 카운트 증가
    const count = messageCount.get(clientId) + 1;
    messageCount.set(clientId, count);
    
    // 제한 초과 시 연결 종료
    if (count > 100) { // 분당 100개 제한
      ws.close(1008, '속도 제한 초과');
      clearInterval(interval);
    }
  });
  
  ws.on('close', () => {
    clearInterval(interval);
  });
});
```

---

## 🚀 WebSocket 최적화

### 1. 데이터 압축
```
// 클라이언트 (압축 라이브러리 사용)
import pako from 'pako';

// 데이터 전송 시 압축
function sendCompressed(data) {
  const jsonString = JSON.stringify(data);
  const compressed = pako.deflate(jsonString);
  socket.send(compressed);
}

// 서버 (데이터 압축 해제)
const pako = require('pako');

ws.on('message', (message) => {
  try {
    // 바이너리 데이터 확인
    if (message instanceof Buffer) {
      // 압축 해제
      const decompressed = pako.inflate(message);
      const jsonString = Buffer.from(decompressed).toString();
      const data = JSON.parse(jsonString);
      
      // 처리 계속...
    }
  } catch (error) {
    console.error('압축 해제 실패:', error);
  }
});
```

### 2. 메시지 배치 처리
```
// 클라이언트 (메시지 묶음 전송)
const messageQueue = [];
let sendInterval;

function queueMessage(message) {
  messageQueue.push(message);
  
  // 첫 메시지면 전송 타이머 시작
  if (messageQueue.length === 1) {
    sendInterval = setInterval(sendQueuedMessages, 50); // 50ms마다
  }
}

function sendQueuedMessages() {
  if (messageQueue.length > 0 && socket.readyState === WebSocket.OPEN) {
    // 여러 메시지를 하나의 배열로 전송
    socket.send(JSON.stringify({
      type: 'batch',
      messages: messageQueue.splice(0)
    }));
  }
  
  // 큐가 비었으면 타이머 중지
  if (messageQueue.length === 0) {
    clearInterval(sendInterval);
    sendInterval = null;
  }
}

// 서버 (배치 메시지 처리)
ws.on('message', (message) => {
  const data = JSON.parse(message);
  
  if (data.type === 'batch' && Array.isArray(data.messages)) {
    // 배치 메시지 각각 처리
    data.messages.forEach(processMessage);
  } else {
    // 단일 메시지 처리
    processMessage(data);
  }
});
```

### 3. 하트비트 (Heartbeat)
```
// 클라이언트 (연결 유지)
function setupHeartbeat(socket) {
  let pingInterval;
  let pongTimeout;
  
  // 연결 시 시작
  socket.onopen = () => {
    pingInterval = setInterval(() => {
      // Ping 전송
      socket.send(JSON.stringify({ type: 'ping' }));
      
      // Pong 응답 타임아웃
      pongTimeout = setTimeout(() => {
        console.error('서버 응답 없음');
        socket.close();
      }, 5000);
    }, 30000); // 30초마다
  };
  
  // Pong 수신
  socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    if (data.type === 'pong') {
      clearTimeout(pongTimeout);
    }
  };
  
  // 연결 종료 시 정리
  socket.onclose = () => {
    clearInterval(pingInterval);
    clearTimeout(pongTimeout);
  };
}

// 서버 (Ping에 응답)
ws.on('message', (message) => {
  try {
    const data = JSON.parse(message);
    if (data.type === 'ping') {
      ws.send(JSON.stringify({ type: 'pong' }));
    }
  } catch (error) {
    console.error('메시지 처리 실패:', error);
  }
});
```

---

## 📱 WebSocket 확장 기술

### 1. Socket.IO
```
// 클라이언트
<script src="/socket.io/socket.io.js"></script>
<script>
  const socket = io();
  
  // 이벤트 기반 통신
  socket.on('connect', () => {
    console.log('Connected to Socket.IO');
  });
  
  // 메시지 수신
  socket.on('chat message', (data) => {
    console.log('Message:', data);
  });
  
  // 메시지 전송
  socket.emit('chat message', {
    text: 'Hello!',
    user: 'User123'
  });
  
  // 네임스페이스 & 룸
  const chatRoom = io('/chat');
  chatRoom.emit('join', 'room1');
</script>

// 서버 (Node.js)
const io = require('socket.io')(server);

io.on('connection', (socket) => {
  console.log('New user connected');
  
  // 메시지 수신
  socket.on('chat message', (data) => {
    console.log('Message received:', data);
    
    // 모든 클라이언트에 브로드캐스트
    io.emit('chat message', data);
  });
  
  // 룸 기능
  socket.on('join', (room) => {
    socket.join(room);
    io.to(room).emit('user joined', socket.id);
  });
});

// 장점
// ✅ 자동 재연결
// ✅ 폴백 메커니즘 (WebSocket 불가 시 다른 방식)
// ✅ 룸 & 네임스페이스
// ✅ 이벤트 기반 API
```

### 2. SockJS
```
// 클라이언트
<script src="https://cdn.jsdelivr.net/npm/sockjs-client/dist/sockjs.min.js"></script>
<script>
  const socket = new SockJS('/echo');
  
  socket.onopen = () => {
    console.log('Connected to SockJS');
    socket.send('Hello!');
  };
  
  socket.onmessage = (e) => {
    console.log('Message:', e.data);
  };
  
  socket.onclose = () => {
    console.log('Disconnected from SockJS');
  };
</script>

// 서버 (Node.js)
const http = require('http');
const sockjs = require('sockjs');

// SockJS 서버 생성
const sockjsServer = sockjs.createServer();

// 연결 핸들러
sockjsServer.on('connection', (conn) => {
  console.log('New connection');
  
  conn.on('data', (message) => {
    console.log('Message received:', message);
    conn.write('Echo: ' + message);
  });
  
  conn.on('close', () => {
    console.log('Connection closed');
  });
});

// HTTP 서버에 SockJS 연결
const server = http.createServer();
sockjsServer.attach(server);
server.listen(8080);

// 장점
// ✅ 크로스 브라우저 호환성
// ✅ 폴백 옵션 (XHR, JSONP 등)
// ✅ WebSocket API 유사
```

---

## 🔍 WebSocket 디버깅과 모니터링

### 1. 브라우저 개발자 도구
```
Chrome DevTools:
1. Network 탭
2. WS 필터 선택
3. 메시지 내용 보기

정보:
- 연결 상태
- 프레임 송수신
- 오류 확인
```

### 2. 서버 로깅
```
// 서버 로깅 설정
wss.on('connection', (ws, req) => {
  const clientIp = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
  
  console.log(`[${new Date().toISOString()}] 새 연결: ${clientIp}`);
  
  ws.on('message', (message) => {
    console.log(`[${new Date().toISOString()}] 메시지 수신: ${message}`);
  });
  
  ws.on('close', (code, reason) => {
    console.log(`[${new Date().toISOString()}] 연결 종료: ${code} ${reason}`);
  });
  
  ws.on('error', (error) => {
    console.error(`[${new Date().toISOString()}] 오류: ${error.message}`);
  });
});

// 로그 파일 저장 (winston 사용)
const winston = require('winston');
const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  defaultMeta: { service: 'websocket-service' },
  transports: [
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' })
  ]
});

// WebSocket 로깅
wss.on('connection', (ws, req) => {
  logger.info('새 연결', {
    ip: req.headers['x-forwarded-for'] || req.connection.remoteAddress,
    timestamp: new Date().toISOString()
  });
  
  // 나머지 이벤트 로깅...
});
```

### 3. 모니터링 도구
```
1. Prometheus + Grafana:
- 연결 수 모니터링
- 메시지 처리량
- 오류율

2. Elastic Stack (ELK):
- 로그 분석
- 실시간 모니터링
- 이상 탐지

3. 자체 대시보드:
// 통계 수집
const stats = {
  connections: 0,
  messages: 0,
  errors: 0
};

wss.on('connection', (ws) => {
  stats.connections++;
  
  ws.on('message', () => {
    stats.messages++;
  });
  
  ws.on('error', () => {
    stats.errors++;
  });
  
  ws.on('close', () => {
    stats.connections--;
  });
});

// HTTP 엔드포인트로 통계 제공
app.get('/stats', (req, res) => {
  res.json(stats);
});
```

---

## 🌐 웹소켓 트러블슈팅

### 1. 일반적인 문제와 해결
```
문제: 연결이 자주 끊김
해결:
- 서버 Timeout 설정 확인
- 프록시/로드밸런서 설정 조정
- 하트비트(Ping/Pong) 구현
- 자동 재연결 메커니즘 구현

문제: 메모리 사용량 증가
해결:
- 불필요한 연결 정리
- 메시지 크기 제한
- 비활성 클라이언트 감지 및 연결 해제

문제: 메시지 전송 실패
해결:
- 연결 상태 확인 (readyState)
- 오류 처리 추가
- 메시지 큐 구현 (재연결 시 전송)
```

### 2. 스케일링 문제 해결
```
문제: 많은 동시 연결 처리
해결:
- 수평적 확장 (여러 서버)
- Redis/RabbitMQ로 메시지 브로커 구현
- 서버 간 메시지 동기화
- 세션 어피니티 (Sticky Sessions)

구현 예시:
// Redis 사용 (Node.js)
const Redis = require('ioredis');
const sub = new Redis();
const pub = new Redis();

// 구독 설정
sub.subscribe('chat');

// 메시지 수신 시
sub.on('message', (channel, message) => {
  // 모든 클라이언트에 브로드캐스트
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(message);
    }
  });
});

// 메시지 발행
wss.on('connection', (ws) => {
  ws.on('message', (message) => {
    // Redis 채널에 발행
    pub.publish('chat', message);
  });
});
```

---

## 📊 웹소켓 성능 측정

### 1. 핵심 지표
```
1. 지연 시간 (Latency)
- 메시지 왕복 시간 (Round-trip time)
- 클라이언트 → 서버 → 클라이언트

2. 처리량 (Throughput)
- 초당 메시지 수 (Messages per second)
- 초당 데이터량 (MB/s)

3. 연결 수 (Connection Count)
- 최대 동시 연결 수
- 연결 성공률

4. 리소스 사용량
- CPU 사용률
- 메모리 사용량
- 네트워크 대역폭
```

### 2. 벤치마킹 도구
```
1. Artillery (https://artillery.io)
- 부하 테스트 
- 시나리오 기반 테스트
- WebSocket 전용 기능

2. Tsung (http://tsung.erlang-projects.org)
- 분산 부하 테스트
- 다양한 프로토콜 지원

3. K6 (https://k6.io)
- 스크립트 기반 테스트
- 메트릭 수집
- WebSocket 지원
```

### 3. 성능 측정 예시
```
// Artillery 테스트 구성 (YAML)
config:
  target: "wss://example.com/socket"
  phases:
    - duration: 60
      arrivalRate: 5
      rampTo: 50
      name: "Warm up"
    - duration: 120
      arrivalRate: 50
      name: "Sustained load"
  
  ws:
    # 재연결 시도
    rejectUnauthorized: false
    
scenarios:
  - engine: "ws"
    name: "WebSocket chat"
    flow:
      # 연결
      - think: 1
      
      # 메시지 전송
      - send: '{"type":"message","text":"Hello World!"}'
      
      # 응답 대기
      - think: 2
      
      # 10개 메시지 전송
      - loop:
          - send: '{"type":"message","text":"Message {{$loopCount}}"}'
          - think: 1
        count: 10
```

---

## 💡 주요 포인트

- **양방향 통신**: 클라이언트와 서버가 자유롭게 통신
- **낮은 지연시간**: HTTP 폴링보다 효율적
- **확장성**: 적절한 최적화로 대규모 시스템 구축 가능
- **보안**: WSS, 인증, 검증으로 안전한 통신 구현
- **생태계**: Socket.IO, SockJS 등 확장 라이브러리 활용

