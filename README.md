# Puang-Bot

## 목차
- [Puang-Bot](#puang-bot)
  - [목차](#목차)
  - [소개](#소개)
  - [Methods](#methods)
    - [대화](#대화)
    - [가르치기](#가르치기)
- [Puang-BOT 구성](#puang-bot-구성)
  - [Python](#python)
  - [Tensorflow](#tensorflow)
  - [Puang-BOT 폴더 구성](#puang-bot-폴더-구성)
    - [Puang-BOT Client.exe](#puang-bot-clientexe)
    - [requirements.txt](#requirementstxt)
    - [Token](#token)
  - [Puang-BOT\\data](#puang-botdata)
    - [ChatBotData.csv](#chatbotdatacsv)
    - [intro.txt](#introtxt)
    - [data/ChatBotData-Old 폴더](#datachatbotdata-old-폴더)
    - [Organizing-Data, Validation Data](#organizing-data-validation-data)
  - [Puang-BOT\\source 폴더 구성](#puang-botsource-폴더-구성)
    - [Puang-BOT Client.cpp](#puang-bot-clientcpp)
    - [chat-bot.ipynb](#chat-botipynb)
    - [푸앙봇 테스트.py, chatbot\_mention\_ver, GPT3\_Chatbot.ipynb](#푸앙봇-테스트py-chatbot_mention_ver-gpt3_chatbotipynb)
    - [Puang.ico(png)](#puangicopng)
  - [Puang-BOT\\tool](#puang-bottool)
    - [fakepuang.exe](#fakepuangexe)
    - [fakepuang.py](#fakepuangpy)
    - [data organizing.py](#data-organizingpy)
    - [TXT.py](#txtpy)
    - [Untitled-1.py](#untitled-1py)

## 소개
- Discord에서 작동하는 Chatbot, Puang-Bot입니다.
- 질문에 대한 답변을 할 수 있습니다.
- 질문에 대한 답변을 학습할 수 있습니다.


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

## Python

- Python 3.9.12를 사용하여 테스트를 진행하였습니다.

## Tensorflow

- Tensorflow를 이용하여 질문에 대한 답변을 학습합니다.
- Tessflow의 버전은 2.9.2를 사용하였습니다. (requirements.txt 참고)

## Puang-BOT 폴더 구성

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
  - tensorflow (2.9.2)
  - discord.py
  - numpy
  - pandas
  - matplotlib
  - pydot

### Token

- Discord Bot Token은 내장된 Token.txt 파일에 입력하여 사용합니다.
- '여기에 토큰 입력' 부분을 본인의 토큰으로 변경하여 사용합니다.
  
## Puang-BOT\data

### ChatBotData.csv

- ChatBotData.csv는 푸앙이가 학습할 질문과 답변이 저장되어 있는 파일입니다.
- 위 데이터는 깃허브의 songys님의 Chatbot_data를 사용하였습니다.
- https://github.com/songys/Chatbot_data

### intro.txt

- intro.txt는 Puang-BOT Client.exe를 실행할 때 출력되는 문구입니다.
- 기본적으로는 귀여운 푸앙이의 아스키 아트가 출력됩니다.

### data/ChatBotData-Old 폴더

- ChatBotData-Old 폴더는 Puang-BOT이 실행될 때마다 ChatBotData.csv 파일을 백업하는 폴더입니다.
- 백업된 시간이 파일명에 포함됩니다.

### Organizing-Data, Validation Data

- 추가적인 학습을 할 수 있는 데이터들입니다.
- 기본적인 학습에는 사용되지 않습니다.
- 위 데이터들은 AI Hub의 챗봇 데이터를 사용하였습니다.
- https://www.aihub.or.kr/

## Puang-BOT\source 폴더 구성

### Puang-BOT Client.cpp

- Puang-BOT Client.exe의 소스코드입니다.
- 소스코드를 수정하여 클라이언트의 스케줄러를 변경할 수 있습니다.
- 시간 구현에는 chrono 라이브러리를 사용하였습니다.

### chat-bot.ipynb

- Jupiter Notebook으로 작성된 Puang-BOT의 학습 코드입니다.

### 푸앙봇 테스트.py, chatbot_mention_ver, GPT3_Chatbot.ipynb

- 푸앙봇 테스트.py : Disord 봇을 테스트하기 위해서 작성한 코드입니다.
- chatbot_mention_ver : 이하 동일
- GPT3_Chatbot.ipynb : GPT3를 이용한 챗봇 코드입니다. 실행을 위해서는 GPT3 API Key가 필요합니다.

### Puang.ico(png)

- Puang-BOT Client.exe의 아이콘입니다.
- 위 파일은 중앙대학교에서 제공하는 푸앙이 이미지를 편집하여 만들었습니다.
  
## Puang-BOT\tool

### fakepuang.exe

- fakepuang.py는 Puang-BOT이 학습할 때 봇이 종료되지 않도록 하는 프로그램입니다.
- 주어진 명령어가 입력되었을 때 학습 중이라는 메시지를 출력합니다.
- 일종의 디스코드 봇이라고 생각하시면 됩니다.
- 위 프로그램은 python으로 작성되었으며, exe로 변환하기 위해 quto-py-to-exe를 사용하였습니다.
- 좋은 프로그램을 제공해주셔서 감사합니다. brentvollebregt! (진짜로요! 사랑해요!)
- https://github.com/brentvollebregt/auto-py-to-exe

### fakepuang.py

- fakepuang.py는 fakepuang.exe의 소스코드입니다.

### data organizing.py

- data organizing.py는 Validation Data를 정리하는 코드입니다.

### TXT.py

- TXT.py는 한 폴더에 있는 모든 txt 파일을 하나의 txt 파일로 합치는 코드입니다.

### Untitled-1.py

- 안녕! 세상아!
- (무시해주세요!) 그냥 print("hello world!")를 해보고 싶어서 만든 코드입니다.