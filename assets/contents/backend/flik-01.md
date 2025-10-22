# FLIK 개발기 - 백엔드 #1

**스와이프 기반 장소 카드 저장 및 코스 생성 서비스**

---

## 🚀 프로젝트 시작 배경

2025 관광데이터 공모전에 참가하려고 했던 게 이 프로젝트의 출발점이었다.  
신청 마감 전날에 알게된 이 공모전에 팀을 못꾸린 채로 냅다 급하게 신청서를 넣었다. 그리고 기획서 예비심사에서 덜컥 통과가 되었다.  
그 후 벌리는 일이 많아 해커톤 등 다른 여러 프로젝트 참여로 시간은 계속 지나갔고 제출일이 두달이 채 안남게되었다.  
**“이걸 혼자 할 수 있을까?”** 하는 생각에 취소를 고민하던 찰나, 운 좋게도 **기획자를 찾게 되었고**, 그렇게 본격적인 FLIK 개발이 시작됐다.  

기획자 겸 디자이너친구가 와이어프레임과 화면 설계를 진행하는 동안,  
나는 백엔드 개발자로서 **아키텍처 설계, CI/CD 파이프라인, 코드 컨벤션**을 구축했다.  
요즘 특히나 AI의 도움을 제대로 받기 위해서 무엇보다 가장 중요한 절차라고 생각한다.  
초반에 시간을 꽤 투자했지만, 이 덕분에 이후 개발 속도와 품질 모두 안정적으로 유지할 수 있었다.  

---

## 🧱 개발 철학과 코드 기준

FLIK의 백엔드는 단순한 CRUD API가 아니라,  
**도메인 중심의 구조와 확장성을 고려한 서비스**를 목표로 했다.  
그래서 다음과 같은 기준을 엄격히 적용했다.  

* **Clean Architecture + Hexagonal Architecture**  
  → 비즈니스 로직을 프레임워크나 인프라에 종속되지 않게 분리  
* **DDD (Domain Driven Design)**  
  → 도메인 용어를 중심으로 설계하고, 각 모듈의 역할을 명확히 구분  
* **TDD (Test Driven Development)**  
  → 핵심 로직은 테스트 코드로 먼저 검증  
* **AOP (Aspect Oriented Programming)**  
  → 로깅, 트랜잭션, 예외처리 같은 횡단 관심사 분리  
* **CQRS (Command Query Responsibility Segregation)**  
  → Command / Query를 분리해 읽기와 쓰기 로직의 명확한 책임 구분  

그리고 개발 중 다음과 같은 규칙을 통일했다.

* `@Setter` 사용 금지 → 도메인 객체는 **메서드 기반 생성**
* `@AllArgsConstructor` 대신 `@RequiredArgsConstructor` 사용
* API 응답은 항상 `Response.success()` 형태로 통일
* 예외는 `FlikException`을 상속받아 처리 (`GlobalExceptionHandler` 적용)

---

## 🧩 기술 스택

| 구분         | 기술                                |
| ---------- | --------------------------------- |
| **언어**     | Java 21+                          |
| **프레임워크**  | Spring Boot 3.x                   |
| **빌드 도구**  | Gradle                            |
| **CI/CD**  | GitHub Actions                    |
| **서버**     | Raspberry Pi (ARM64)              |
| **로드밸런서**  | Nginx (Blue/Green upstream proxy) |
| **CDN**    | Cloudflare + SSL 인증서              |
| **데이터베이스** | MySQL + Redis                     |
| **ORM**    | JPA / Hibernate                   |
| **보안**     | Spring Security + OAuth2 + JWT    |
| **문서화**    | Swagger / OpenAPI 3               |
| **컨테이너**   | Docker                            |
| **테스트**    | JUnit 5, MockMVC, TestContainers  |

개인 프로젝트이지만, 실제 서비스 배포 환경과 최대한 유사하게 구성했다.
덕분에 **CI/CD 파이프라인 자동화, 도메인 기반 코드 설계, 캐시 전략, 로드밸런싱** 등 실무적인 경험을 한 번에 다뤄볼 수 있었다.

---

## 🏗 아키텍처 설계

FLIK은 **Hexagonal Architecture (Ports & Adapters)** 패턴을 기반으로 설계했다.

```
Ports              ->            Core            ->           Adapters
in/out(interfaces)      model/service(business)    in(web,batch,scheduler)/out(external, db, JPA-entity)
```

즉, **비즈니스 로직(Core)** 은 외부 입출력(Adapters)과 완전히 분리되어 있고,
입출력 계층은 **Ports 인터페이스**를 통해서만 접근할 수 있다.

---

## 📁 프로젝트 구조

```
src/main/java/yunrry/flik/
├── adapters/
│   ├── in/
│   │   ├── dto/           # Request / Response DTO
│   │   ├── scheduler/     # 배치 작업
│   │   └── web/           # REST Controllers
│   └── out/
│       ├── cache/         # Redis 어댑터
│       ├── external/      # 외부 API 어댑터
│       └── persistence/   # JPA 어댑터
│           └── entity/    # JPA 엔티티
├── config/               # 설정 클래스
├── core/
│   ├── domain/
│   │   ├── event/        # 도메인 이벤트
│   │   ├── exception/    # 비즈니스 예외
│   │   └── model/        # 도메인 모델
│   └── service/          # 비즈니스 로직
└── ports/
    ├── in/
    │   ├── query/        # Query 모델
    │   ├── command/      # Command 모델
    │   └── usecase/      # UseCase 인터페이스
    └── out/
        ├── message/      # 메시징 포트
        └── repository/   # Repository 인터페이스
```

---

## 🧠 계층별 역할 요약

| 계층                        | 역할                                |
| ------------------------- | --------------------------------- |
| **Controller**            | `in ports` 인터페이스 구현 (REST API)    |
| **UseCase**               | 비즈니스 로직 인터페이스 정의                  |
| **Service**               | Core 비즈니스 로직 구현체                  |
| **Command / Query**       | CQRS 입력 모델                        |
| **Repository (out port)** | 저장소 인터페이스 정의                      |
| **JpaRepository**         | Spring Data JPA 상속 인터페이스          |
| **Adapter**               | Repository 구현체 (JpaRepository 주입) |
| **Domain**                | 핵심 비즈니스 객체                        |
| **Entity**                | JPA 엔티티 (영속성 객체)                  |

---

## ✍️ 네이밍 컨벤션

통일된 네이밍은 협업뿐 아니라 유지보수에서도 큰 힘을 발휘한다.
FLIK에서는 다음 컨벤션을 따랐다.

| 구분                | 규칙                                               |
| ----------------- | ------------------------------------------------ |
| **JpaRepository** | `{Domain}JpaRepository`                          |
| **Adapter**       | `{Domain}Adapter`                                |
| **Repository**    | `{Domain}Repository`                             |
| **Command**       | `{Action}{Domain}Command`                        |
| **Query**         | `Get{Domain}Query`, `Search{Domain}Query`        |
| **UseCase**       | `{Domain}UseCase`                                |
| **Service**       | `{Action}Service`                                |
| **Entity**        | `{Domain}Entity`                                 |
| **Domain**        | `{Domain}`                                       |
| **DTO**           | `{Domain}{Purpose}Request/Response` (record 클래스) |
| **Exception**     | `{Domain}Exception` extends `FlikException`      |

---

## 💬 마무리

1편에서는 FLIK의 **기획 배경과 기술적 토대**를 중심으로 정리했다.
다음 편에서는 실제로 **도메인 설계, API 흐름, 배포 자동화 과정** 등을 좀 더 구체적으로 다뤄볼 예정이다.

> 🔜 2편 예고: “Raspberry Pi 위에 Spring Boot를 띄워서 실제 서비스하기”

---

원하면 다음편(2편)용으로 “도메인 설계 + API 흐름 + 배포 자동화 과정” 중심의 초안도 바로 이어서 써드릴 수 있어요.
그렇게 이어서 쓸까?
