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
  - Emulated Container Support가 무거운 프로그램(OS)를 지원하여, Container별로 운영체제를 설치할 필요 X

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