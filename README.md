# 청주 Gwellcity1 홈 어시스턴트 애드온

이 프로젝트는 청주 Gwellcity1차 아파트를 위한 홈 어시스턴트 애드온입니다. 아파트의 시스템 및 서비스와 통합을 제공합니다.

## 기능

- 청주 Gwellcity1차 cvnet Wallpad 시스템과 실시간 연동
- 전열교환기 On/Off 제어

## 설치 방법

1. 홈 어시스턴트의 Supervisor 패널로 이동합니다.
2. "애드온 스토어" 탭을 클릭합니다.
3. 우측 상단의 세 개의 점을 클릭하고 "저장소"를 선택합니다.
4. 다음 저장소 URL을 추가합니다: `https://github.com/yuribini/cj-gwellcity1-ha-addon`
5. 애드온 스토어에서 "CJ Gwellcity1 애드온"을 클릭합니다.
6. "설치" 버튼을 클릭합니다.

## 설정

애드온 설치 후 다음 설정을 완료해야 합니다:

1. 홈 어시스턴트의 "Supervisor" -> "애드온" -> "CJ Gwellcity1 애드온" -> "구성" 탭으로 이동합니다.
2. 다음 설정 옵션을 입력합니다:
   - `mqtt_host`: MQTT 브로커의 호스트 주소 (보통 홈 어시스턴트의 IP 주소)
   - `mqtt_port`: MQTT 브로커의 포트 (기본값: 1883)
   - `mqtt_username`: MQTT 브로커 사용자 이름
   - `mqtt_password`: MQTT 브로커 비밀번호
   - `gwellcity1_host`: CJ Gwellcity1 시스템의 IP 주소
   - `gwellcity1_port`: CJ Gwellcity1 시스템의 포트 (기본값: 8899)
3. "저장" 버튼을 클릭하여 설정을 저장합니다.

## 사용 방법

1. 애드온 설치 및 설정 완료 후, "시작" 버튼을 클릭하여 애드온을 실행합니다.
2. 애드온이 성공적으로 시작되면, CJ Gwellcity1 시스템의 데이터가 자동으로 홈 어시스턴트로 전송됩니다.
3. 홈 어시스턴트의 통합 구성요소에서 새로운 장치와 센서를 확인할 수 있습니다.
4. 대시보드에 위젯을 추가하여 CJ Gwellcity1 시스템의 상태를 모니터링하고 제어할 수 있습니다.
5. 전열교환기 제어:
   - On: MQTT 토픽 "homeassistant/gwellcity1/command"에 메시지 {"device": "heat_exchanger", "state": "on"} 발행
   - Off: MQTT 토픽 "homeassistant/gwellcity1/command"에 메시지 {"device": "heat_exchanger", "state": "off"} 발행

참고: 특정 기능이나 명령어는 아파트 시스템의 구현에 따라 다를 수 있습니다. 자세한 사용 방법은 아파트 관리사무소나 시스템 제공업체에 문의해 주세요.

## 문제 해결

애드온 실행 중 문제가 발생하면 다음 단계를 따라 문제를 해결해 보세요:

1. 애드온의 로그를 확인하여 오류 메시지를 확인합니다.
2. 설정값이 올바른지 다시 한 번 확인합니다.
3. 홈 어시스턴트와 CJ Gwellcity1 시스템이 같은 네트워크에 있는지 확인합니다.
4. 문제가 지속되면 이 저장소에 issue를 생성하여 도움을 요청하세요.

## 기여하기

기여는 언제나 환영합니다! 풀 리퀘스트를 자유롭게 제출해 주세요.
