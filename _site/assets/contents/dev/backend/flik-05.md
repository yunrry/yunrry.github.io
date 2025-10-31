# FLIK: 여행코스 추천 서비스 개발기 - (백엔드 5편)   
> **임베딩 프로세스 설계와 Postgres 벡터 저장 구조**

---

## 목표
사용자가 장소(Spot)를 저장할 때,
그 장소의 **설명(description)** 을 OpenAI 모델로 분석하고,  
핵심 키워드를 추출한 뒤 이를 **벡터 임베딩(Embedding)** 으로 변환하여  
PostgreSQL DB에 저장하는 전체 프로세스를 설계한다.  

---

## 시스템 개요

> “사용자가 저장한 장소를 시스템이 ‘이해’하는 과정”

```text
[User Action]
  ↓
(1) Spot 저장 요청
  ↓
(2) description 텍스트 분석 (LLM)
  ↓
(3) 키워드 추출
  ↓
(4) Embedding API 호출
  ↓
(5) 임베딩 벡터 생성
  ↓
(6) PostgreSQL에 벡터 저장
```

---

## 임베딩 프로세스 상세

### ➊ 키워드 추출 단계 — OpenAI LLM

* 모델: `gpt-4o-mini` (텍스트 분석 전용)
* 입력: `spot.description`
* 출력: 핵심 키워드 3~8개 JSON 배열 형식

```json
["자연", "한적함", "호수뷰", "산책", "가족여행"]
```

예시 프롬프트:

```text
당신은 텍스트 요약 전문가입니다.
다음 관광지 설명에서 핵심적인 의미를 대표하는 키워드 3~8개를 추출하세요.
출력은 JSON 배열 형식으로만 반환하세요.

설명:
"맑은 호수와 산책로가 매력적인 도심 속 자연 명소입니다.
가족 단위로 방문이 많으며, 조용한 분위기 속 힐링이 가능합니다."
```

---

### ➋ 임베딩 벡터 생성 — OpenAI Embedding API

* 모델: `text-embedding-3-small`
* 입력: 위에서 추출된 키워드 문자열 (공백 기준 join)
* 출력: 1536차원 벡터 리스트

예시:

```json
{
  "embedding": [0.0123, -0.0045, 0.0098, ...]
}
```

---

### ➌ 데이터 저장 — PostgreSQL + pgvector

FLIK에서는 MariaDB가 주요 트랜잭션 DB이지만,
**벡터 검색 최적화를 위해 PostgreSQL (pgvector 확장)** 을 별도 구성한다.

> 💡 PostgreSQL의 `pgvector`는 OpenAI 임베딩 모델과 완벽 호환된다.

```sql
CREATE TABLE spot_embeddings (
    id BIGSERIAL PRIMARY KEY,
    spot_id BIGINT NOT NULL,
    keywords TEXT[],
    embedding VECTOR(1536),
    created_at TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY (spot_id) REFERENCES spots(id)
);
```

---

## 전체 데이터 플로우

```text
[1] UserSavedSpotEventListener
     └── spot 저장 이벤트 수신
         └── LLMKeywordExtractor.extractKeywords(description)
              └── ["자연", "산책", "가족여행"]
         └── EmbeddingService.createEmbedding(keywords)
              └── [0.0123, -0.0045, ...]
         └── SpotEmbeddingRepository.save(spot_id, keywords, embedding)
```

---

## 서비스 코드 구조 예시

```java
@Service
@RequiredArgsConstructor
public class SpotEmbeddingService {

    private final LLMKeywordExtractor llmKeywordExtractor;
    private final EmbeddingClient embeddingClient;
    private final SpotEmbeddingRepository spotEmbeddingRepository;

    @Async
    public void processEmbedding(Spot spot) {
        // 1. 키워드 추출
        List<String> keywords = llmKeywordExtractor.extractKeywords(spot.getDescription());

        // 2. 벡터 임베딩 생성
        List<Double> vector = embeddingClient.embed(String.join(" ", keywords));

        // 3. PostgreSQL 저장
        spotEmbeddingRepository.save(spot.getId(), keywords, vector);
    }
}
```

---

## Repository 예시

```java
@Repository
@RequiredArgsConstructor
public class SpotEmbeddingRepository {

    private final JdbcTemplate jdbcTemplate;

    public void save(Long spotId, List<String> keywords, List<Double> embedding) {
        String sql = "INSERT INTO spot_embeddings (spot_id, keywords, embedding) VALUES (?, ?, ?)";
        jdbcTemplate.update(sql, spotId, keywords.toArray(new String[0]), embedding.toArray(new Double[0]));
    }
}
```

---

## 왜 PostgreSQL을 선택했나

| 기준             | MariaDB | PostgreSQL (pgvector) |
| -------------- | ------- | --------------------- |
| 트랜잭션 처리        | ✔ 우수    | ✔ 우수                  |
| 벡터 유사도 검색      | ✘ 미지원   | ✔ 지원                  |
| OpenAI 임베딩 호환성 | 낮음      | 매우 높음                 |
| 확장성            | 높음      | 높음                    |
| 운영 편의성         | 익숙함     | 다소 복잡                 |

> **결론:**
> 트랜잭션 로직은 MariaDB,
> 임베딩 및 추천 관련 연산은 PostgreSQL로 **역할 분리 (CQRS-like 구조)**

---

## 향후 확장 포인트

* **RAG 연계:**
  사용자 검색 요청 시 임베딩 기반 벡터 검색으로
  “유사한 장소” 또는 “유사한 테마” 자동 추천
* **주기적 벡터 리프레시:**
  Spot description이 업데이트되면 embedding 자동 재생성
* **멀티모달 확장:**
  이미지 설명문(Image Caption)을 함께 임베딩하여
  텍스트 + 이미지 기반 추천 강화

---


> 🔜 6편 예고: “나와 비슷한 여행자는 누구일까 — 사용자 임베딩과 추천 매칭 로직”
