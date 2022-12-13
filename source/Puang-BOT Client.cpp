#include <iostream>
#include <thread>
#include <chrono>
#include <cstdlib>

using namespace std;

int main() {
    // cmd 창의 크기를 intro.txt의 크기에 맞춥니다.
    system("mode con cols=91 lines=56");

    // data/intro.txt를 읽어와 출력합니다.
    system("type data\\intro.txt");

    // 새로운 창에 main.py를 실행합니다.
    system("start python main.py");


    while (true) {
		// 현재 시간을 hour, min, sec에 기록합니다.
		time_t now = chrono::system_clock::to_time_t(chrono::system_clock::now());
		int hour = now / 3600 % 24;
		int min = now / 60 % 60;
		int sec = now % 60;
		

        // 현재 시간이 정시라면 main.py를 실행합니다.
        if (min == 0 && sec == 0) {
            // main.py를 정지합니다.
            system("taskkill /f /im python.exe");

            // main.py를 실행합니다.
            system("start python main.py");
        }
        // 1초간 대기합니다.
        this_thread::sleep_for(chrono::seconds(1));
    }
}
