import platform
import json
import os

class MissionComputer:
    def __init__(self):
        self.name = "Mars Mission Control Computer"
        self.settings = self._load_settings()

    def _load_settings(self):
        """setting.txt 파일을 읽어 출력 항목 설정을 로드합니다."""
        settings = {}
        try:
            if os.path.exists("setting.txt"):
                with open("setting.txt", "r") as f:
                    for line in f:
                        if ":" in line:
                            key, value = line.strip().split(":")
                            settings[key] = value.lower() == "true"
            else:
                print("경고: setting.txt 파일이 없어 모든 항목을 출력합니다.")
        except Exception as e:
            print(f"설정 파일 로드 중 오류 발생: {e}")
        return settings

     #메소드 이름 
    def get_mission_computer_info(self):
        """운영체제, CPU, 메모리 등 정적 시스템 정보를 반환합니다."""
        try:
            import psutil
            full_info = {
                "os": platform.system(),
                "os_version": platform.version(),
                "cpu_type": platform.processor(),
                "cpu_cores": psutil.cpu_count(logical=True),
                "memory_size_gb": round(psutil.virtual_memory().total / (1024**3), 2)
            }
            
            # 설정(settings)에 True로 된 항목만 필터링
            filtered_info = {k: v for k, v in full_info.items() if self.settings.get(k, True)}
            
            print("\n=== Mission Computer System Info ===")
            print(json.dumps(filtered_info, indent=4))
            return filtered_info
        except Exception as e:
            print(f"시스템 정보를 가져오는 중 오류 발생: {e}")
            return None

    def get_mission_computer_load(self):
        """CPU와 메모리의 실시간 사용량을 반환합니다."""
        try:
            import psutil
            full_load = {
                "cpu_usage_percent": psutil.cpu_percent(interval=1),
                "memory_usage_percent": psutil.virtual_memory().percent
            }
            
            # 설정(settings)에 True로 된 항목만 필터링
            filtered_load = {k: v for k, v in full_load.items() if self.settings.get(k, True)}
            
            print("\n=== Mission Computer Real-time Load ===")
            print(json.dumps(filtered_load, indent=4))
            return filtered_load
        except Exception as e:
            print(f"부하 정보를 가져오는 중 오류 발생: {e}")
            return None

# 인스턴스화 및 실행
if __name__ == "__main__":
    runComputer = MissionComputer()
    runComputer.get_mission_computer_info()
    runComputer.get_mission_computer_load()