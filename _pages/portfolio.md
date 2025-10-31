---
title: "Portfolio"
layout: single
permalink: /portfolio/
author_profile: false
classes: wide
---

<style>

.portfolio-header {
max-width: 100%;
  width: 100%;
  padding: 40px 20px;
  border-bottom: 2px solid #e0e0e0;
  margin-bottom: 40px;
  text-align: center;
}
.portfolio-header img {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 20px;
}
.portfolio-header h1 {
  margin: 10px 0;
}
.portfolio-header p {
  color: #666;
  font-size: 1.1em;
}
.download-btns {
  display: flex;
  gap: 10px;
  justify-content: center;
  margin-bottom: 10px;
  padding-left : 100px;
}
.download-btn {
  padding: 4px 8px;
  background:rgba(155, 214, 189, 0.59);
  color: rgb(94, 108, 102);
  text-decoration: none;
  border-radius: 4px;
  transition: all 0.3s;
  font-size: 0.9em;
}
.download-btn:hover {
  background: #88bca7;
  transform: translateY(-2px);
}
.skills-section {
  margin: 30px 0;
  text-align: left;
}
.skills-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 15px;
}
.skill-tag {
  padding: 4px 8px;
  background: #f0f0f0;
  border-radius: 20px;
  font-size: 0.8em;
  color: #333;
}
.project {
  margin: 50px 0;
  padding: 30px;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
}
.project h2 {
  color: #333;
  border-bottom: 3px solidrgba(155, 214, 189, 0.6);
  padding-bottom: 10px;
  margin-bottom: 20px;
}
.project-meta {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
  font-size: 0.9em;
  color: #666;
}
.project-section {
  margin: 20px 0;
}
.project-section h3 {
  color: #555;
  margin-bottom: 10px;
}
.project-links {
  margin-top: 20px;
  padding-top: 20px;
  border-top: 1px solid #e0e0e0;
}
.project-links a {
  color: #9bd6bd;
  text-decoration: none;
  margin-right: 20px;
}
.project-links a:hover {
  text-decoration: underline;
}

/* 다크모드 */
[data-theme="dark"] .portfolio-header {
  border-bottom-color: #333;
}
[data-theme="dark"] .portfolio-header h1,
[data-theme="dark"] .portfolio-header p {
  color: #e0e0e0;
}
[data-theme="dark"] .skill-tag {
  background: #2d2d2d;
  color: #e0e0e0;
}
[data-theme="dark"] .project {
  border-color: #333;
  background: #1a1a1a;
}
[data-theme="dark"] .project h2 {
  color: #e0e0e0;
}
[data-theme="dark"] .project-section h3 {
  color: #b0b0b0;
}
[data-theme="dark"] .project-links {
  border-top-color: #333;
}

[data-theme="dark"] .download-btn {
  color: white;
}

</style>



<div class="portfolio-header">
   <div style="display: flex; align-items: center; text-align: left; gap: 30px; margin-bottom: 30px;">
        <img src="/assets/images/ProfilePicture.jpeg" alt="Profile" style="width: 120px; height: 120px; border-radius: 50%; object-fit: cover; flex-shrink: 0;">
        <div>
          <h3 style="margin: 0 0 5px 0;">김 윤 영</h3>
          <p style="color: #666; margin: 0;">Backend Developer</p>
        </div>
        <div class="download-btns" style="display: flex; flex-direction: column;">
            <a href="/assets/portfolio251031-ko.pdf" class="download-btn" download>📄 다운로드</a>
            <a href="/assets/portfolio-en.pdf" class="download-btn" download>📄 download</a>
        </div>
      </div>
  
  
  
  <div class="skills-section">
    <h3>💻 Tech Stack</h3>
    <div class="skills-grid">
      <span class="skill-tag">Java</span>
      <span class="skill-tag">Spring Boot</span>
      <span class="skill-tag">Python</span>
      <span class="skill-tag">MySQL</span>
      <span class="skill-tag">PostgreSQL</span>
      <span class="skill-tag">Docker</span>
      <span class="skill-tag">AWS</span>
      <span class="skill-tag">React</span>
      <span class="skill-tag">TypeScript</span>
    </div>
  </div>
</div>

<div class="project">
  <h2>🗺️ FLIK - RAG 기반 AI 여행 코스 추천 서비스</h2>
  
  <div class="project-meta">
    <span>📅 2025.08 ~ 2025.09 (1개월)</span>
    <span>👥 2인 (풀스택 개발 1명, 기획/디자인 1명)</span>
  </div>
  
  <div class="project-section">
    <h3>📌 개요</h3>
    <p>사용자가 스와이프 인터페이스를 통해 선호 여행지를 선택하면 RAG 기반으로 맞춤형 여행 코스를 자동 생성해주는 서비스</p>
  </div>
  
  <div class="project-section">
    <h3>🎯 핵심 기능</h3>
    <ul>
      <li><strong>RAG 기반 AI 코스 생성:</strong> 사용자 스와이프 데이터 분석하여 개인 선호도 벡터 생성 후 최적 동선 추천</li>
      <li><strong>플랜 저장 및 공유:</strong> 다른 사용자 코스 탐색, 개별 장소 저장 기능</li>
      <li><strong>여행기 작성:</strong> 코스 정보 연동 블로그 기능</li>
      <li><strong>지도 시각화:</strong> 여행 순서별 핀 표시로 직관적 코스 확인</li>
    </ul>
  </div>
  
  <div class="project-section">
    <h3>💡 담당 역할 및 기술적 구현</h3>
    
    <h4>1. 백엔드 서버 아키텍처 설계 및 구현</h4>
    <ul>
      <li>Spring Boot 기반 RESTful API 서버 구축</li>
      <li>MySQL과 PostgreSQL 용도별 분리 운영 (트랜잭션 중심 데이터 / 벡터 연산 데이터)</li>
    </ul>
    
    <h4>2. RAG 기반 추천 알고리즘 개발</h4>
    <ul>
      <li>TourAPI 관광지 데이터 수집 후 OpenAI 임베딩 API로 벡터화</li>
      <li>사용자 스와이프 이벤트 기반 선호도 벡터 실시간 업데이트</li>
      <li>카테고리별 슬롯 배정 및 지리적 거리 고려 최적 동선 알고리즘 구현</li>
      <li>영업시간, 접근성, 계절성 등 도메인 특화 필터 적용</li>
    </ul>
    
    <h4>3. 인프라 설계 및 운영</h4>
    <ul>
      <li>Raspberry Pi 메인 서버로 비용 최적화</li>
      <li>Docker Compose로 앱, DB, Redis 컨테이너화</li>
      <li>Nginx 리버스 프록시, 로드밸런싱, SSL 인증서 적용</li>
    </ul>
    
    <h4>4. CI/CD 파이프라인 구축</h4>
    <ul>
      <li>GitHub Actions 활용 자동 빌드, 테스트, 배포</li>
      <li>Blue/Green 무중단 배포</li>
    </ul>
    
    <h4>5. 프론트엔드 개발</h4>
    <ul>
      <li>React TypeScript SPA 구현</li>
      <li>Kakao Map API 연동 지도 시각화</li>
      <li>반응형 디자인 적용</li>
    </ul>
    
    <h4>6. 문서화 및 협업 관리</h4>
    <ul>
      <li>Swagger API 문서 자동화</li>
      <li>GitHub Project 이슈 관리</li>
      <li>Discord Webhook 배포 알림 자동화</li>
    </ul>
  </div>
  
  <div class="project-links">
    <a href="https://flik-tau.vercel.app" target="_blank">🔗 서비스 바로가기</a>
    <a href="https://flikapp.org/api/swagger-ui/index.html" target="_blank">📚 API 문서</a>
  </div>
</div>

<div class="project">
  <h2>🎧 도르멍드르멍 - 제주 오디오 스토리텔링 관광 서비스</h2>
  
  <div class="project-meta">
    <span>📅 2025.01 (2박3일 해커톤)</span>
    <span>👥 5인 (백엔드 1명, 프론트엔드 2명, 기획 1명, 디자인 1명)</span>
    <span>🏆 제14기 구름톤 In JEJU 최우수상</span>
  </div>
  
  <div class="project-section">
    <h3>📌 개요</h3>
    <p>제주도를 살펴보고 그 안의 이야기에 귀 기울이는 방식으로 제주를 경험할 수 있도록 기획된 오디오 스토리텔링 기반 관광 서비스</p>
  </div>
  
  <div class="project-section">
    <h3>🎯 핵심 기능</h3>
    <ul>
      <li><strong>QR 코드 스캔:</strong> 관광지 안내판 QR 코드 스캔 시 오디오 콘텐츠 출력</li>
      <li><strong>위치 기반 & 검색:</strong> 현재 위치 기준 가까운 명소 표시</li>
      <li><strong>제주 명소 오디오:</strong> AI 음성(제주 사투리)으로 스토리 제공</li>
      <li><strong>이야기 조각 수집:</strong> 콘텐츠 소비 시 스토리 조각 자동 저장</li>
    </ul>
  </div>
  
  <div class="project-section">
    <h3>💡 담당 역할 및 기술적 구현</h3>
    
    <h4>1. 인프라 & 배포</h4>
    <ul>
      <li>Kubernetes + Jenkins + ArgoCD 파이프라인 구축</li>
      <li>kubectl로 MySQL 노드 직접 생성 및 관리</li>
      <li>해커톤 종료 후 Raspberry Pi 기반 자체 서버 재구축</li>
    </ul>
    
    <h4>2. 데이터 관리 및 처리</h4>
    <ul>
      <li>제주 관광지 CSV 데이터 수집 후 Python 스크립트로 DB 초기화</li>
      <li>데이터 반정규화로 API 단순화 및 성능 확보</li>
      <li>위치기반, 실시간 키워드검색 API 구현</li>
    </ul>
    
    <h4>3. AI 기반 오디오 생성</h4>
    <ul>
      <li>QR 스캔/검색 시 AI 프롬프트 요청 → 제주어 스크립트 생성</li>
      <li>ElevenLabs API로 오디오 변환</li>
      <li>생성 오디오 캐시/DB 저장하여 재사용</li>
    </ul>
    
    <h4>4. 협업 과정</h4>
    <ul>
      <li>5명 팀원과 현장에서 처음 만나 2박3일만에 MVP 완성</li>
      <li>효과적인 의사소통과 배려로 빠른 협업 능력 체득</li>
    </ul>
  </div>
  
  <div class="project-links">
    <a href="https://dormung.netlify.app" target="_blank">🔗 서비스 바로가기</a>
    <a href="https://9oormthon.goorm.io/23b4e699-7fb0-8058-9022-c72255784662" target="_blank">🏆 구름톤 전시관</a>
  </div>
</div>

<div class="project">
  <h2>🚶 SafeWalk - 보행자 사고 안전 관리 플랫폼</h2>
  
  <div class="project-meta">
    <span>📅 2025.08 (2주)</span>
    <span>👥 3인 (백엔드 1명, 프론트엔드 1명, 기획 1명)</span>
  </div>
  
  <div class="project-section">
    <h3>📌 개요</h3>
    <p>전국 관광지 및 보행자 사고 데이터를 융합해 사고 다발 구간을 시각화하는 대시보드 기반 안전 관리 플랫폼</p>
  </div>
  
  <div class="project-section">
    <h3>📊 활용 데이터</h3>
    <ul>
      <li>한국관광 데이터랩: 전국 인기관광지/중심관광지</li>
      <li>경찰청 교통사고 DB, 도로교통공단 사고 다발 지점</li>
      <li>법정동 경계/좌표 정보</li>
    </ul>
  </div>
  
  <div class="project-section">
    <h3>💡 담당 역할 및 기술적 구현</h3>
    
    <h4>1. 데이터 전처리 및 융복합</h4>
    <ul>
      <li>법정동 단위 사고 건수 기반 위험도 산출 (인구 밀집도, 도시 개발률 반영)</li>
      <li>데이터 정합성 문제 해결 (법정동/행정동 코드, 연도별 코드 변경)</li>
      <li>대용량 폴리곤(shp) → JSON 변환·압축 후 GitHub Pages 업로드</li>
    </ul>
    
    <h4>2. API 설계 및 구현</h4>
    <ul>
      <li>Spring Boot RESTful API 서버</li>
      <li>영역별 법정동 조회, 사고 정보 조회, 관광지 검색, 그래프 조회 API</li>
    </ul>
    
    <h4>3. 시각화 및 대시보드</h4>
    <ul>
      <li>Python pandas 데이터 가공</li>
      <li>matplotlib, seaborn 그래프 보고서 출력</li>
    </ul>
    
    <h4>4. 인프라 및 배포</h4>
    <ul>
      <li>Docker 컨테이너화, Nginx 리버스 프록시</li>
      <li>GitHub Actions CI/CD</li>
      <li>AWS 환경 안정적 운영</li>
    </ul>
    
    <h4>5. 문서화 및 협업</h4>
    <ul>
      <li>Figma 디자인 공유</li>
      <li>Swagger API 문서화</li>
      <li>Discord Webhook 배포 알림</li>
    </ul>
  </div>
  
  <div class="project-links">
    <a href="https://safewalk-kr.netlify.app" target="_blank">🔗 서비스 바로가기</a>
    <a href="https://api.safewalk.cloud/api/swagger-ui/index.html" target="_blank">📚 API 문서</a>
  </div>
</div>

