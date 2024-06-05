# Docker & Container
Docker is a container techonology : A tool for creating and managing containers
- Container : package of code (+ dependency & Tools)
  - same container always yields the same result (코드가 항상 정확한 버전으로 실행하도록 도움)
  - 팀 별로 같은 개발환경에서 개발을 할 수 있음 (재현성)
  - 상황 별로 다른 개발 환경을 적용시킬 수 있음 (환경 변환이 용이)

# Virtual Machine vs Docker Container
## Virtual Machine
Virtual Machine : Host Operating System 위에 VM 설치 (Computer on Computer)
- 분리된 환경 생성, 환경별 구성, 안정적인 공유 및 생산 가능
- Overhead 발생 : 머신이 여러 개 있는 경우, 매번 새로운 프로그램을 머신 내에 설치해야 함 (자원 낭비)
  - linux on VM1, linux on VM2, linux on VM3 -> 같은 linux지만 중복하여 모두 설치해야 함
- 추가적 프로그램 on host system -> 성능이 저하될 수 있음
- 자원 공유가 어려움 (모든 vm에 동일한 환경을 제공해야 함; 단일 구성 파일 존재 X)

## Containers
내재 운영체재 or 내장 컨테이너를 사용한 후, 위에 Docker Engine 도구 실행
- 도커 엔진을 기반으로 하여 위에 여러 개의 컨테이너를 올려놓을 수 있음
  - 각 컨테이너는 별도의 App, Library, Dependency를 가지고 있음
  - Emulated Container Support가 무거운 프로그램(OS)를 지원하여, Container별로 운영체제를 **설치할** 필요 X

# Image
Image : container의 template
- 코드와 코드를 실행할 때 필요한 도구를 포함 -> 모든 설정과 코드를 한 번에 실행할 수 있음
- 한 번 정의하면, 다른 시스템과 서버에서 여러 번 실행 가능
  - 컨테이너 -> 이미지의 구체적인 실행 인스턴스

# 이미지의 사용, 실행
1. 이미 존재하는 이미지 사용
- dockerhub(https://hub.docker.com/)에서 공식 이미지를 찾을 수 있음
  - 이미지 생성? ex. node.js (`docker run node`)
  - `docker ps -a` : ps=processs a = all -> 도커가 생성한 모든 컨테이너를 확인할 수 있음
  - `docker run -it node` : node container의 대화형 세션을 노출하고 싶다. -> node.js의 터미널로 이동
    - it은 internal인가?
    - 탈출하는 건 컨트롤+C 두 번 (command+C 아님)

2. 이미 존재하는 이미지 기반으로 Custom Image 생성
  - `Dockerfile`라는 파일 생성 (이미지 빌드할 때 필요한 도커 명령 포함)
```
  # base가 될 Image의 이름으로 시작
FROM node

# 후속 명령이 어디에서 실행될 것인가?
WORKDIR /app

# 어느 폴더/파일이 이미지에 포함되어야 하는가?
COPY . ./

# 어떤 명령을 실행해야 하는가?
RUN npm install

# 특정 포트를 노출하고 싶을 때
EXPOSE 80

# 모든 작업(종속성 설치)이 종료되면 무엇을 실행해야 하는가?
CMD ["node", "server.js"]
```
- `docker build .`를 통해 Dockerfile을 기반으로 한 커스텀 이미지 생성 (맨 마지막 .은 같은 폴더임을 의미)
- `docker run {imageID}`를 통해 해당 image를 실행
  - `EXPOSE`로 포트번호 노출 시, `docker run -p {액세스하려는 로컬포트:컨테이너에서 노출된 로컬포트} {imageID}`와 같이 사용
  - `p` means publish
- `docker stop {name}`은 해당 image를 실행종료함
- 컨테이너를 재시작해도 변경사항이 저장되지는 않음.
  - 소스코드는 이미지에 반영되지 않기 때문에, 이미지를 재빌드해야함 (읽기 전용)
  - 그래도 일부(레이어)는 캐싱했기 때문에 더 빠르게 빌드됨. (각각의 줄은 layer라고 함.)
    - 다시 시작해야 하는 레이어 및 후속 코드만 재빌드

---
# 이미지 & 컨테이너 관리
1. `docker run` -> 새로운 컨테이너 실행
2. `docker start {containerID or name}` -> 중지되었던 컨테이너 재시작
   - Terminal을 점유하지 않음 (터미널에서 다른 명령 실행할 수 있음)


