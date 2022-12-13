#include <iostream>
#include <thread>
#include <chrono>
#include <cstdlib>

using namespace std;

int main() {

    // 우선 main.py를 실행시킵니다.
	system("python main.py");
	
	// 시작 시간을 기록합니다.
	auto start = chrono::system_clock::now();

    while (true) {
		// 현재 시간을 hour, min, sec에 기록합니다. localtime은 사용하지 않습니다.
		time_t now = chrono::system_clock::to_time_t(chrono::system_clock::now());
		int hour = now / 3600 % 24;
		int min = now / 60 % 60;
		int sec = now % 60;
		
		
		

        // 현재 시간이 정시라면 main.py를 실행합니다.
        if (min == 0 && sec == 0) {
            // main.py를 정지합니다.
            system("taskkill /f /im python.exe");

            // main.py를 실행합니다.
            system("python main.py");

            // 20분간 대기합니다.
            this_thread::sleep_for(chrono::seconds(1200));		
        }
        // 1초간 대기합니다.
        this_thread::sleep_for(chrono::seconds(1));
    }
}
