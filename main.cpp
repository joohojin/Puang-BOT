#include <iostream>
#include <thread>
#include <chrono>
#include <ctime>
#include <cstdlib>

using namespace std;

// 현재 시간을 가져와 global 변수 hour, min, sec에 저장합니다.
void getTime(){
    time_t now = time(0);
    tm *ltm = localtime(&now);
    hour = ltm->tm_hour;
    min = ltm->tm_min;
    sec = ltm->tm_sec;
}

// 현재 시간을 가져오고 main.py의 실행 시간을 오늘 날짜_시간_log.txt에 저장하고 cout으로 출력하는 함수
void logmaker(){

    // 현재 시간을 가져옵니다.
    getTime();

    // 현재 시간을 저장합니다.
    string time = to_string(hour) + "시 " + to_string(min) + "분 " + to_string(sec) + "초";

    // 현재 시간을 출력합니다.
    cout << "main.py 실행 시간: " << hour << "시간 " << min << "분 " << sec << "초" << endl;

    // log.txt에 저장합니다.
    ofstream logFile;
    logFile.open("log.txt", ios::app);

    // 날짜를 저장합니다.
    logFile << "DATE: " << __DATE__ << endl;
    logFile << time << endl;
    logFile.close();

    // 현재 시간을 cout으로 출력합니다.
    cout << time << endl;
}




int main(){

    // 우선 main.py를 실행합니다.
    system("python main.py");

    // logmaker 함수를 실행합니다.
    logmaker();

    while(true){
        // 현재 시간을 가져옵니다.
        getTime();

        // 현재 시간이 정시라면 main.py를 실행합니다.
        if(min == 0 && sec == 0){
            // main.py를 정지합니다.
            system("taskkill /f /im python.exe");

            // 20분간 대기합니다.
            this_thread::sleep_for(chrono::seconds(1200));

            // main.py를 실행합니다.
            system("python main.py");

            // logmaker 함수를 실행합니다.
            logmaker();
        }

        // 1초간 대기합니다.
        this_thread::sleep_for(chrono::seconds(1));
    }
}