🛰️ Project Objectives (프로젝트 목적)
환경 데이터 시뮬레이션: 화성의 극한 환경에서 발생할 수 있는 주요 지표들을 랜덤으로 생성하여 시스템의 견고함을 테스트합니다.
실시간 로깅 기능: 수집된 데이터를 시계열 순으로 저장하여 향후 데이터 분석 및 기지 상태 모니터링의 기초 자료로 활용합니다.
객체 지향 프로그래밍(OOP) 구현: Python 클래스를 활용하여 센서 객체를 모듈화하고 관리하기 용이하게 설계했습니다.
🛠️ System Specifications (시스템 상세 정보)
1. Data Definitions (데이터 정의)시스템은 다음과 같은 6가지 핵심 환경 데이터를 수집합니다.

| 수집 항목 | 변수명 | 유효 범위 (Range) | 단위 |
| :--- | :--- | :--- | :--- |
| **내부 온도** | `mars_base_internal_temperature` | 18 ~ 30 | °C |
| **외부 온도** | `mars_base_external_temperature` | 0 ~ 21 | °C |
| **내부 습도** | `mars_base_internal_humidity` | 50 ~ 60 | % |
| **외부 광량** | `mars_base_external_illuminance` | 500 ~ 715 | W/m² |
| **내부 CO2** | `mars_base_internal_co2` | 0.02 ~ 0.1 | % |
| **내부 산소** | `mars_base_internal_oxygen` | 4 ~ 7 | % |



(주요 기능)
set_env(): random.uniform() 함수를 사용하여 실시간으로 변화하는 환경 수치를 생성하고 env_values 사전에 업데이트합니다.get_env(): 현재 저장된 모든 데이터를 반환함과 동시에, mars_log.txt 파일에 타임스탬프와 함께 기록을 남깁니다.💻 
How to Run (실행 방법)PrerequisitesPython 3.x 이상이 설치되어 있어야 합니다.Execution저장소 폴더에서 다음 명령어를 실행합니다.Bashpython3 
mars_mission_computer.py

📋 Data Log Example (로그 기록 예시)실행 후 생성되는 mars_log.txt 파일의 모습입니다.Plaintext[2026-03-27 18:35:12] In_Temp: 22.45, Ex_Temp: 12.10, In_Hum: 54.32, Ex_Illu: 610.45, In_CO2: 0.0450, In_O2: 5.12
[2026-03-27 18:35:15] In_Temp: 28.12, Ex_Temp: 5.67, In_Hum: 58.90, Ex_Illu: 520.11, In_CO2: 0.0821, In_O2: 6.88

📖 Key Takeaways (학습 성과)Python Dictionary 활용: 복잡한 환경 변수들을 사전 객체로 묶어 효율적으로 관리하는 법을 익혔습니다.File I/O: with open() 구문을 사용하여 외부 파일에 데이터를 안전하게 기록하는 방법을 습득했습니다.
Documentation: 개발된 코드를 타인이 이해하기 쉽도록 Markdown 형식으로 문서화하는 능력을 배양했습니다.Maintained by: [본인 성함 입력]Institution: [학교 또는 소속 입력]
