# JPA

## Hibernate
### hibernate.hbm2ddl.auto=OPTION
**Options**
**create**: 매번 스키마를 삭제하고 새로 생성  
**create-drop**: 애플리케이션 종료시 스키마 삭제  
**update**: 기존 스키마 유지하면서 변경사항만 반영 (없으면 생성)  
**validate**: 스키마 검증만 하고 변경하지 않음  
**none**: 아무것도 하지 않음  

```yaml
# application.yml
spring:
  jpa:
    hibernate:
      ddl-auto: update  # 없으면 생성, 있으면 업데이트
```

개발환경에서는 주로 **update**사용  
- 데이터베이스가 존재하지 않는 경우: 새로운 데이터베이스와 테이블을 생성  
- 데이터베이스가 존재하는 경우: 기존 스키마와 엔티티를 비교해서 필요한 부분만 수정/추가

운영환경 ->  보통 validate나 none을 사용



<br><br>
---
`#JPA` `#Hibernate`