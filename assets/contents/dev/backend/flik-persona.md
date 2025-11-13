# 페르소나 만들기 

```python
ATEGORIES = ["NATURE", "HISTORY_CULTURE", "CAFE", "THEMEPARK", "ACTIVITY", "MARKET", "FESTIVAL", "INDOOR"]

PERSONAS = [
    {
        "persona_id": "U001",
        "name": "역사·분석형",
        "traits": {
            "성격": "체계적, 관찰력 높음, 계획 중심",
            "여행 리듬": "아침 일찍 출발, 하루 2~3곳 깊이 있게 탐방",
            "취향": "역사 유적지, 사찰, 고건축, 해설 프로그램",
            "싫어하는 것": "소음, 즉흥적 일정, 대형 쇼핑몰",
            "식사 성향": "현지식 중 한식 위주, 전통차 선호",
            "숙박": "한옥스테이, 조용한 마을형 숙소",
            "피로 허용도": "낮음 — 하루 3곳 이상 이동 시 피로도 증가"
        },
        "category_like_prob": {
            "NATURE": 0.6,
            "HISTORY_CULTURE": 0.9,
            "CAFE": 0.6,
            "THEMEPARK": 0.2,
            "ACTIVITY": 0.3,
            "MARKET": 0.4,
            "FESTIVAL": 0.4,
            "INDOOR": 0.7
        }
    },
    {
        "persona_id": "U002",
        "name": "감성·힐링형",
        "traits": {
            "성격": "감성적, 내향적, 사색을 즐김",
            "여행 리듬": "늦은 아침 출발, 여유로운 일정 선호",
            "취향": "자연 풍경, 조용한 카페, 일몰 명소",
            "싫어하는 것": "시끄러운 군중, 과한 일정",
            "식사 성향": "브런치, 디저트 카페, 지역 베이커리 선호",
            "숙박": "뷰 좋은 숙소, 감성 숙소",
            "피로 허용도": "보통 이하 — 휴식 위주 일정 선호"
        },
        "category_like_prob": {
            "NATURE": 0.9,
            "HISTORY_CULTURE": 0.5,
            "CAFE": 0.95,
            "THEMEPARK": 0.3,
            "ACTIVITY": 0.4,
            "MARKET": 0.5,
            "FESTIVAL": 0.6,
            "INDOOR": 0.7
        }
    },

```

U001~U010 까지 10개의 페르소나들을 이런식으로 정의해보았다.    

정의한 페르소나를 gpt에 빙의 시켜 장소데이터를 순차적으로 전송하고 해당 장소를 선택 할지 안할지를 판단시킬것이다.  

```python

# -----------------------------
# OpenAI 선택 함수
# -----------------------------
def should_select_spot(persona, spot_description):
    prompt = f"""
당신은 여행 추천 전문가입니다.

사용자 페르소나 정보:
- 이름: {persona['name']}
- 카테고리별 선호도: {persona['category_like_prob']}

장소 설명: {spot_description}

질문: 이 사용자가 이 장소를 선택할 가능성이 높다면 "yes", 선택하지 않을 가능성이 높다면 "no"로만 응답하세요.
"""

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "당신은 여행 추천 전문가입니다."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0,
                max_tokens=5
            )
            text = response.choices[0].message.content.strip().lower()
            selected = text.startswith("y")
            logging.info(f"GPT 응답: {text} -> 선택: {selected}")
            return selected

        except Exception as e:
            logging.warning(f"OpenAI API 호출 실패: {e} (시도 {attempt}/{MAX_RETRIES})")
            if attempt < MAX_RETRIES:
                time.sleep(2)
            else:
                logging.error("최대 재시도 횟수 도달, 건너뜀")
                return False
```


메인함수에서 적당한 브레이크 포인트를 걸어서 OpenAI 요청 함수를 호출하고
결과를 저장했다.

```json
{
  "U001": {
    "NATURE": [
      4019,
      4020,
      4027,
      4032,
      4033,
      4037,
      4038,
      4040,
      4046,
      4052
    ],
    "HISTORY_CULTURE": [
      4003,
      4004,
      4005,
      4006,
      4007,
      4008,
      4009,
      4010,
      4011,
      4012
    ],
    "CAFE": [
      5584,
      5589,
      5591,
      5593,
      5594,
      5595,
      5596,
      5599,
      5600,
      5601
    ],
    .
    .
    .
    },
    "U002": {
        .
        .
        .
    }
  }
```

위와 같이 각 페르소나가 선택할법한 카테고리별 장소 ID목록을 json으로 추출했다.  

다음은 FLIK서버 api로 각 유저를 생성하고 장소를 저장하는 스크립트를 만든다.


```python
# -----------------------------
# 상수 정의
# -----------------------------
BASE_URL = "http://localhost:8080"
SIGNUP_URL = f"{BASE_URL}/api/v1/auth/signup"
SWIPE_URL = f"{BASE_URL}/api/v1/swipe"
JSON_FILE = "persona_selected_spots_partial.json"

# -----------------------------
# API 호출 함수
# -----------------------------
def signup(persona_id: str) -> Dict[str, Any]:
    """회원가입 API 호출"""
    email = f"{persona_id}@test.com"
    password = f"password{persona_id}"
    nickname = persona_id
    
    payload = {
        "email": email,
        "password": password,
        "nickname": nickname
    }
    
    try:
        response = httpx.post(SIGNUP_URL, json=payload, timeout=30.0)
        response.raise_for_status()
        result = response.json()
        
        if result.get("success") and result.get("data"):
            access_token = result["data"].get("accessToken")
            return {
                "success": True,
                "access_token": access_token,
                "user_id": result["data"].get("user", {}).get("id"),
                "response": result
            }
        else:
            return {
                "success": False,
                "error": result.get("message", "Unknown error"),
                "response": result
            }
    except httpx.HTTPStatusError as e:
        return {
            "success": False,
            "error": f"HTTP {e.response.status_code}: {e.response.text}",
            "response": None
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "response": None
        }

def swipe_spot(access_token: str, spot_id: int) -> Dict[str, Any]:
    """Swipe API 호출"""
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "spotId": spot_id
    }
    
    try:
        response = httpx.post(SWIPE_URL, json=payload, headers=headers, timeout=30.0)
        response.raise_for_status()
        result = response.json()
        
        return {
            "success": result.get("success", False),
            "spot_id": spot_id,
            "saved": result.get("data", {}).get("saved", False),
            "message": result.get("data", {}).get("message", result.get("message", "")),
            "response": result
        }
    except httpx.HTTPStatusError as e:
        return {
            "success": False,
            "spot_id": spot_id,
            "error": f"HTTP {e.response.status_code}: {e.response.text}",
            "response": None
        }
    except Exception as e:
        return {
            "success": False,
            "spot_id": spot_id,
            "error": str(e),
            "response": None
        }

```


![flik-persona-1](/assets/contents/dev/images/flik-persona-1.png) 


이제 A/B 테스트의 바탕이 될 페르소나가 만들어졌다.  
각 유저가 저장한 장소들로 유저 선호도 벡터가 저장되었고,  
각 테스트마다 이 벡터 상태로 다시 돌아와야한다.

![flik-persona-2](/assets/contents/dev/images/flik-persona-2.png) 
