# SSH
 Secure Shell의 약자로, 네트워크를 통해 서버에 원격으로 안전하게 접속하고 명령을 실행하기 위한 프로토콜

접속방식 1 : 비밀번호  
접속방식 2 : 공개키key & 개인key


원격 테스트 시, 호스트의 방화벽에서 TCP 22번 포트를 개방한 상태더라도 공유기(라우터) 또는 ISP에서 TCP 22번 포트를 막아버려 
접속이 불가한 경우가 있다. (보통 ssh 접속 포트는 22번이 고정인듯, AWS EC2 사용할때도 마찬가지로)  

**22번 포트가 안될때 대응방법**
1. sshd_config 파일을 수정하여 접속 포트를 임의의 다른 포트 번호로 변경한다.
2. 공유기의 포트포워딩 기능을 이용, 공유기의 WAN 측 임의의 포트를 SSH 호스트가 사용하는 IP의 TCP 22번 포트와 연결한다.  
DMZ 기능이나 Twin-IP 기능은 호스트를 완전히 외부로 개방하게 되므로 사설 네트워크 내부가 아닌 이상 가급적 사용하지 않는다.
VPN을 경유하도록 구성할 수도 있겠지만 이중 암호화로 오버헤드만 늘리는 꼴이 되니 차라리 텔넷이 더 낫다.      
3. 공유기 관리자나 ISP 관리자 측에 내가 사용할 호스트의 IP에 대한 22번 포트를 개방하도록 요청한다. 
다만 이 경우는 심각한 보안문제가 발생할 수 있으므로 대부분의 관리자가 거부할 것이다.    
> 출처: 나무위키

내가 사용하는 서버 제공자가 같이 프로젝트 했던 팀원분이신데 서버 네트워크는 그분 집의 공유기로 라우팅되고있다.   
sk브로드밴드를 사용중이신데 22번 80번 포워딩이 차단되어있었다.  
그래서 2022번을 뚫어서 주셨다.

githubAction과 같은 배포자동화 도구는  
push할 서버 접속시 기본적으로 22번 포트로 접근한다.  
22번 포트가 아니라면 반드시 스크립트에 지정 포트를 작성해야한다.

```yaml
#deploy.yml
- name: Deploy to Raspberry Pi
  uses: appleboy/ssh-action@v1.0.0
  with:
    host: ${{ env.RASPBERRY_PI_HOST }}
    username: ${{ env.RASPBERRY_PI_USER }}
    key: ${{ secrets.RASPBERRY_PI_SSH_KEY }}
    port: 2022  # 이 줄 추가
```
-> 모든 SSH 단계에 port: 2022 추가

GitHub Secrets에 ssh key(개인키) 등록시  
-----BEGIN OPENSSH PRIVATE KEY-----부터 -----END OPENSSH PRIVATE KEY-----까지   
그대로 전체 복붙


### 키 생성한적 없을 때 / 새로 생성하고싶을 떄

**SSH 공개키 생성 (Linux 기반):**  
```bash
ssh-keygen -t rsa -b 4096 -C "github-actions"
```
-C "name" 은 키를 구별하기 위해 이름 붙이는것(생략가능). 용도별로 키 여러개 생성 가능  
-> ~/.ssh/id_rsa.pub 생성됨

생성한 키를 사용하기 위해서 등록이 필요하다
```bash
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys 
chmod 600 ~/.ssh/authorized_keys
```

**SSH 개인키 확인**
```bash
# 호스트에서
cat ~/.ssh/id_rsa
```

**SSH 설정 확인**

```bash
sudo nano /etc/ssh/sshd_config
```

```nano
Include /etc/ssh/sshd_config.d/*.conf

Port 2022
PubkeyAuthentication yes # 없으면 추가
AuthorizedKeysFile .ssh/authorized_keys #인증된 키들은 authorized_keys 에 모여있음
PasswordAuthentication yes
ChallengeResponseAuthentication no
UsePAM yes
```
변경사항 있을 시
```bash
sudo systemctl reload ssh
```

**quick process**
```bash
ssh-keygen -t rsa -b 4096  # or 이름 지정시 $ ssh-keygen -t rsa -b 4096 -C "name"
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys 
chmod 600 ~/.ssh/authorized_keys
sudo nano /etc/ssh/sshd_config #PubkeyAuthentication yes 없으면 추가-> ctrl+O -> ctrl+X
sudo systemctl reload ssh 
cat ~/.ssh/id_rsa #키 복사
```

### 클라이언트에서 SSH 접속 개인키 저장하기 (보안주의 내 PC여야함)
1. 텍스트 편집기에 호스트에서 복사한키 복붙
2. .pem 확장자로 저장
3. 파일 권한: chmod 600 filename.pem (Mac/Linux)


<br><br>
---
`#SSH` `#RaspberryPi` `#Linux` `#RSA`