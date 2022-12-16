# Puang-Bot

## 소개
- Discord에서 작동하는 Chatbot, Puang-Bot입니다.
- 질문에 대한 답변을 할 수 있습니다.
- 질문에 대한 답변을 학습할 수 있습니다.

## 서론
- 기존의 유명한 챗봇들은 특정한 애플리케이션을 다운받아야 사용할 수 있었습니다.
  
  대화를 위해 만들어진 챗봇들이 앱이라는 틀에 갇혀있다는 아이러니를 가지고 있었습니다.
  
  그러한 문제점을 타파하기 위해 저희는 Discord에서 작동하는 챗봇을 만들기로 하였습니다.
  
  그 결과, Puang-Bot이라는 챗봇을 만들었습니다.

  
- Puang-Bot은 2022-2학기 오픈소스프로그래밍 수업의 프로젝트로 진행되었습니다.
  
  (학생들의 고통이 끝났습니다 ㅠㅠ)
  
  아래의 가이드는 Puang-Bot을 실행하는 방법과 Puang-Bot의 구성을 설명합니다.


  
- ## 목차
- [Methods](#methods)
  - [대화](#대화)
  - [가르치기](#가르치기)
- [실행 방법](#실행-방법)
  - [라이브러리 설치](#라이브러리-설치)
  - [1. Puang-BOT Client.exe를 사용하는 방법](#1-puang-bot-clientexe를-사용하는-방법)
  - [2. main.ipynb를 사용하는 방법](#2-mainipynb를-사용하는-방법)
  - [3. main.py를 사용하는 방법](#3-mainpy를-사용하는-방법)
- [Puang-BOT 구성](#puang-bot-구성)
  - [Python](#python)
  - [Tensorflow](#tensorflow)
  - [Puang-BOT 폴더 구성](#puang-bot-폴더-구성)
    - [Puang-BOT Client.exe](#puang-bot-clientexe-1)
    - [requirements.txt](#requirementstxt)
    - [Token.txt](#tokentxt)
  - [Puang-BOT/data 폴더 구성](#puang-botdata-폴더-구성)
    - [ChatBotData.csv](#chatbotdatacsv)
    - [intro.txt](#introtxt)
    - [data/ChatBotData-Old 폴더](#datachatbotdata-old-폴더)
    - [Organizing-Data, Validation Data](#organizing-data-validation-data)
  - [Puang-BOT/source 폴더 구성](#puang-botsource-폴더-구성)
    - [Puang-BOT Client.cpp](#puang-bot-clientcpp)
    - [chat-bot.ipynb](#chat-botipynb)
    - [푸앙봇 테스트.py, chatbot\_mention\_ver, GPT3\_Chatbot.ipynb](#푸앙봇-테스트py-chatbot_mention_ver-gpt3_chatbotipynb)
    - [Puang.ico(png)](#puangicopng)
    - [puangbot.py](#puangbotpy)
  - [Puang-BOT/tool 폴더 구성](#puang-bottool-폴더-구성)
    - [fakepuang.exe](#fakepuangexe)
    - [fakepuang.py](#fakepuangpy)
    - [data organizing.py](#data-organizingpy)
    - [TXT.py](#txtpy)
    - [Untitled-1.py](#untitled-1py)


## Methods

### 대화
- '/푸앙아' 명령어를 이용해 말을 걸면 푸앙이가 대답합니다.

예시 코드
```
User : /푸앙아 '푸앙해줘'
```
``Puang-Bot`` : User 님: 푸앙해줘

``Puang-Bot`` : 푸앙푸앙!


### 가르치기
- '/가르치기' 명령어를 이용하여 푸앙이에게 질문에 대한 대답을 가르칠 수 있습니다.

예시 코드
```
User : /가르치기 '1+1은?' '2입니다!'
```
``Puang-Bot`` : 앞으로 '1+1은?'이라는 질문에 '2입니다!'라고 대답할게요!
    
# 실행 방법

## 라이브러리 설치

- requirements.txt에 있는 라이브러리를 설치합니다.

## 1. Puang-BOT Client.exe를 사용하는 방법

- 먼저 Token.txt에 Discord Bot Token을 입력합니다.
- Puang-BOT Client.exe를 실행하면 Puang-BOT이 실행됩니다.
- 정각마다 Puang-BOT이 학습을 위해 자동으로 꺼졌다가 켜집니다.

## 2. main.ipynb를 사용하는 방법

- main.ipynb를 실행하면 Puang-BOT이 실행됩니다.
- 토큰은 직접 '여기에 토큰을 입력하세요'에 입력해야 합니다.
- 모든 셀을 실행하면 Puang-BOT이 실행됩니다.

## 3. main.py를 사용하는 방법

- 먼저 Token.txt에 Discord Bot Token을 입력합니다.
- main.py를 실행하면 Puang-BOT이 실행됩니다.


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
  
- 정각마다 학습을 진행합니다. (학습은 컴퓨터 성능에 따라 5~20분 정도 소요됩니다.)
- Puang-BOT Client.exe는 C++로 작성되었습니다.
- Source Code는 source 폴더의 Puang-BOT Client.cpp 파일을 참고해주세요.
   
### requirements.txt

- requirements.txt에는 Puang-Bot을 실행하기 위해 필요한 라이브러리들이 명시되어 있습니다.
- 아래는 대표적인 라이브러리들의 예시입니다.
  - tensorflow (2.9.2)
  - discord.py
  - numpy
  - pandas
  - matplotlib
  - pydot

### Token.txt

- Discord Bot Token은 내장된 Token.txt 파일에 입력하여 사용합니다.
- '여기에 토큰 입력' 부분을 본인의 토큰으로 변경하여 사용합니다.
- 이 Token.txt 파일은 main.py, fakepuang.exe와 연동되어 있습니다.
  
## Puang-BOT/data 폴더 구성

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

## Puang-BOT/source 폴더 구성

### Puang-BOT Client.cpp

- Puang-BOT Client.exe의 소스코드입니다.
- 소스코드를 수정하여 클라이언트의 스케줄러를 변경할 수 있습니다.
- 시간 구현에는 chrono 라이브러리를 사용하였습니다.

### chat-bot.ipynb

- Jupiter Notebook으로 작성된 Puang-BOT의 학습 코드입니다.
- Tensorflow 2.9.2를 사용하여 작성되었습니다.
- 셀을 실행하여 학습을 진행할 수 있습니다.

### 푸앙봇 테스트.py, chatbot_mention_ver, GPT3_Chatbot.ipynb

- 푸앙봇 테스트.py : Disord 봇을 테스트하기 위해서 작성한 코드입니다.
- chatbot_mention_ver : reply를 사용해보기 위해서 작성한 코드입니다.
- GPT3_Chatbot.ipynb : GPT3를 이용한 챗봇 코드입니다. 실행을 위해서는 GPT3 API Key가 필요합니다.

### Puang.ico(png)

- Puang-BOT Client.exe의 아이콘입니다.
- 위 파일은 중앙대학교에서 제공하는 푸앙이 이미지를 편집하여 만들었습니다.
  
### puangbot.py

- slash command를 테스트하기 위해 작성한 코드입니다.
- 자세한 시도들은 Puang-BOT/source/slash test 폴더를 봐주시기 바랍니다.

## Puang-BOT/tool 폴더 구성

### fakepuang.exe

- fakepuang.py는 Puang-BOT이 학습할 때 봇이 종료되지 않도록 하는 프로그램입니다.
- 주어진 명령어가 입력되었을 때 학습 중이니 기다려달라는 메시지를 출력합니다.
- (한마디로 사기를 치는 프로그램입니다.)
- 일종의 디스코드 봇이라고 생각하시면 됩니다. (어쨌든 봇이 작동하기는 하잖아요?)
  <br/>
  <br/>  
- 위 프로그램(사기)은 python으로 작성되었습니다.
- 실행에 원활한 확장자인 exe로 변환하기 위해 auto-py-to-exe를 사용하였습니다.
- pyinstaller와 auto-py-to-exe의 개발자, 기여자분들께 감사드립니다.
- 좋은 프로그램을 제공해주셔서 감사합니다! (진짜로요! 사랑해요!)
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
