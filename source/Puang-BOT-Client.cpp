#include <iostream>
#include <thread>
#include <chrono>
#include <cstdlib>

using namespace std;

int main() {

    // cmd 창의 크기를 intro.txt의 크기에 맞춥니다.
    system("mode con cols=91 lines=56");

    // cmd 창의 제목을 Puang-BOT Client로 설정합니다.
    system("title Puang-BOT Client");

    // python.exe가 실행되어 있으면 종료합니다.
    system("taskkill /f /im python.exe");
    // fakepuang.exe이 실행되어 있으면 종료합니다.
    system("taskkill /f /im fakepuang.exe");

    // data/intro.txt를 읽어와 출력합니다.
    system("type data\\intro.txt");

    // fakepuang.exe를 실행합니다.
    system("start tool\\fakepuang.exe");

    // 새로운 창에 main.py를 실행합니다.
    system("start python main.py");

    // 7분간 대기합니다.
    this_thread::sleep_for(chrono::seconds(420));

    // fakepuang.exe를 정지합니다.
    system("taskkill /f /im fakepuang.exe");


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

            // tool/fakepuang.exe를 실행합니다.
            system("start tool\\fakepuang.exe");

            // main.py를 실행합니다.
            system("start python main.py");

            // 7분간 대기합니다.
            this_thread::sleep_for(chrono::seconds(420));

            // fakepuang.exe를 정지합니다.
            system("taskkill /f /im fakepuang.exe");
        }
        // 1초간 대기합니다.
        this_thread::sleep_for(chrono::seconds(1));
    }

    return 0;
}