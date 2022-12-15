# Puang-Bot

## 소개
- Discord에서 작동하는 Chatbot, Puang-Bot입니다.
- 질문에 대한 답변을 할 수 있습니다.
- 질문에 대한 답변을 학습할 수 있습니다.

## 목차
- [Puang-Bot](#puang-bot)
  - [소개](#소개)
  - [목차](#목차)
  - [Methods](#methods)
    - [대화](#대화)
    - [가르치기](#가르치기)
- [Puang-BOT 구성](#puang-bot-구성)
    - [Python](#python)
    - [Tensorflow](#tensorflow)
    - [Puang-BOT Client.exe](#puang-bot-clientexe)
    - [requirements.txt](#requirementstxt)
    - [Token](#token)
  - [Puang-BOT\\data](#puang-botdata)
    - [ChatBotData.csv](#chatbotdatacsv)
    - [intro.txt](#introtxt)
    - [data\\ChatBotData-Old 폴더](#datachatbotdata-old-폴더)



## Methods

### 대화
- '푸앙아 대화' 명령어를 이용해 말을 걸면 푸앙이가 대답합니다.
```
User : /푸앙아 푸앙해줘
```
``Puang-Bot`` : 푸앙푸앙!


### 가르치기
- '푸앙아 가르치기' 명령어를 이용하여 푸앙이에게 질문에 대한 대답을 가르칠 수 있습니다.
```
User : /가르치기
```
``Puang-Bot`` : 뭐라고 물어보실 건가요?

``User`` : 1+1은?

``Puang-Bot`` : 1+1은?에 대한 답변은 무엇인가요?

``User`` : 2입니다!

``Puang-Bot`` : 질문과 답변이 추가되었습니다!
    


# Puang-BOT 구성

### Python

- Python 3.9.12를 사용하여 테스트를 진행하였습니다.

### Tensorflow

- Tensorflow를 이용하여 질문에 대한 답변을 학습합니다.
- Tessflow의 버전은 2.9.2를 사용하였습니다. (requirements.txt 참고)

### Puang-BOT Client.exe

- Puang-BOT Client.exe는 Puang-BOT을 실행하는 프로그램입니다.

- 기본적으로 내장되어 있는 기능은 다음과 같습니다.
  - Puang-BOT을 실행합니다.
  - Puang-BOT을 종료합니다.
  - Puang-BOT의 학습을 진행합니다.
  - Puang-BOT의 학습을 진행하는 동안 Puang-BOT을 종료하지 않습니다.
  
- 매 정각마다 학습을 진행합니다. (학습은 컴퓨터 성능에 따라 5~20분 정도 소요됩니다.)
- Puang-BOT Client.exe는 C++로 작성되었습니다.
- Source Code는 Source 폴더의 Puang-BOT Client.cpp 파일을 참고해주세요.
   
### requirements.txt

- requirements.txt에는 Puang-Bot을 실행하기 위해 필요한 라이브러리들이 명시되어 있습니다.
- 아래는 대표적인 라이브러리들입니다.
  - tensorflow(2.9.2)
  - discord.py
  - numpy
  - pandas
  - matplotlib
  - pydot

### Token

- Discord Bot Token은 내장된 Token.txt 파일에 입력하여 사용합니다.
- '여기에 토큰 입력' 부분을 자신의 토큰으로 변경하여 사용합니다.
  
## Puang-BOT\data

### ChatBotData.csv

- ChatBotData.csv는 푸앙이가 학습할 질문과 답변이 저장되어 있는 파일입니다.

### intro.txt

- intro.txt는 Puang-BOT Client.exe를 실행할 때 출력되는 문구입니다.
- 기본적으로는 귀여운 푸앙이의 아스키 아트가 출력됩니다.

### data\ChatBotData-Old 폴더

- ChatBotData-Old 폴더는 Puang-BOT이 실행될 때마다 ChatBotData.csv 파일을 백업하는 폴더입니다.
- 백업된 시간이 파일명에 포함됩니다.

