# Github Action

GithubAction 으로 배포자동화를 수차례 진행해보면서 겪은 시행착오들을 정리해보려한다.  
프로젝트 첫 배포시 성공까지 workflow를 10번은 돌려봐야했던 지난날의 나...  
디버깅으로 시간낭비와 AI와의 끝도없는 말씨름은 그만하자.


레지스트리 권한은 어디서 설정해?

GitHub Repository → Settings → Actions → General → Workflow permissions → "Read and write permissions" 선택

또는

Settings → Packages → Package creation → "Public" 허용

Read and write permissions 클릭이 막혀있으면 어떡해?

Organization 소유자가 제한한 것입니다.

해결방법:

Organization owner에게 권한 요청
개인 계정으로 fork해서 사용
다른 레지스트리 사용 (Docker Hub 등)

GitHub Actions 실패 원인:

레지스트리 권한 없음: denied: installation not allowed to Create organization package
SSH 키 없음: can't connect without a private SSH key

내가 소유자야Organization Settings → Member privileges → Actions permissions → "Allow all actions and reusable workflows" 활성화
또는 Repository 권한을 직접 확인:
Settings → Actions → General → Actions permissions


GitHub Container Registry 권한 문제입니다. 몇 가지 해결 방법을 제시해드리겠습니다.
해결 방법 1: Personal Access Token 사용 (권장)
1. GitHub Personal Access Token 생성

GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
"Generate new token" 클릭
권한 선택:

write:packages (패키지 업로드)
read:packages (패키지 다운로드)
delete:packages (선택사항)



2. GitHub Actions Secrets에 토큰 추가

Repository → Settings → Secrets and variables → Actions
GHCR_TOKEN 이름으로 생성한 PAT 추가

3. GitHub Actions 워크플로우 수정
yaml      - name: 🔐 Log in to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GHCR_TOKEN }}  # GITHUB_TOKEN 대신 GHCR_TOKEN 사용
해결 방법 2: 패키지 권한 설정
1. Repository 설정 확인

Repository → Settings → Actions → General
"Workflow permissions"에서 "Read and write permissions" 선택

2. 패키지 가시성 설정

이미 생성된 패키지가 있다면: Packages → 해당 패키지 → Settings → "Change visibility"

해결 방법 3: 조직 권한 문제인 경우
만약 yunrry가 조직(Organization) 계정이라면:
1. 조직 설정에서 패키지 권한 확인

Organization Settings → Actions → General
"Package permissions" 확인

2. 개인 계정으로 변경
워크플로우에서 이미지 이름을 개인 계정으로 변경:
yamlenv:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.actor }}/flik-server  # 개인 계정으로 변경