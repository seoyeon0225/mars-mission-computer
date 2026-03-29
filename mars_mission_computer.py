import random
from datetime import datetime  # 표준 라이브러리 (사용 가능)

class DummySensor:
    """화성 기지의 환경 데이터를 시뮬레이션하는 더미 센서 클래스"""

    def __init__(self):
        # 멤버 변수 초기화 (사전 객체)
        self.env_values = {
            "mars_base_internal_temperature": 0.0,
            "mars_base_external_temperature": 0.0,
            "mars_base_internal_humidity": 0.0,
            "mars_base_external_illuminance": 0.0,
            "mars_base_internal_co2": 0.0,
            "mars_base_internal_oxygen": 0.0
        }

    def set_env(self):
        """요구사항에 명시된 범위 내에서 무작위 환경 값을 생성하여 저장"""
        self.env_values["mars_base_internal_temperature"] = random.uniform(18, 30)
        self.env_values["mars_base_external_temperature"] = random.uniform(0, 21)
        self.env_values["mars_base_internal_humidity"] = random.uniform(50, 60)
        self.env_values["mars_base_external_illuminance"] = random.uniform(500, 715)
        self.env_values["mars_base_internal_co2"] = random.uniform(0.02, 0.1)
        self.env_values["mars_base_internal_oxygen"] = random.uniform(4, 7)

    def get_env(self):
        """현재 환경 값을 반환하고 로그 파일에 기록"""
        # 현재 시간 생성 (표준 라이브러리 활용)
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # 로그 문자열 구성 (PEP 8에 따라 한 줄이 너무 길지 않게 관리)
        log_msg = (
            f"[{now}] "
            f"In_Temp: {self.env_values['mars_base_internal_temperature']:.2f}, "
            f"Ex_Temp: {self.env_values['mars_base_external_temperature']:.2f}, "
            f"In_Hum: {self.env_values['mars_base_internal_humidity']:.2f}, "
            f"Ex_Illu: {self.env_values['mars_base_external_illuminance']:.2f}, "
            f"In_CO2: {self.env_values['mars_base_internal_co2']:.4f}, "
            f"In_O2: {self.env_values['mars_base_internal_oxygen']:.2f}\n"
        )
        
        # 파일 출력 (별도 패키지 설치 없이 내장함수 open 사용)
        with open("mars_log.txt", "a", encoding="utf-8") as f:
            f.write(log_msg)
            
        return self.env_values


# 메인 실행부 (인스턴스 생성 및 테스트)
if __name__ == "__main__":
    # 클래스 인스턴스 생성
    ds = DummySensor()
    
    # 순차적 메서드 호출
    ds.set_env()
    data = ds.get_env()

    # 결과 확인 출력
    print("--- Mission Computer: Environment Data ---")
    for key, value in data.items():
        print(f"{key}: {value:.4f}")
    print("\nData has been successfully logged to 'mars_log.txt'.")