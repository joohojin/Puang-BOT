import os
import csv

# Q,A,label의 형식의 csv 파일
# csv의 라벨에 따라서 뒤쪽 라벨이 1이고 다음 문단의 라벨이 2일 경우 두 문단을 묶어서 저장하는 함수를 만들자
# 이때 1라벨은 질문 2라벨은 답변으로 저장하게 코드를 작성하자

# data\Organizing-Data\BAND-DATA_organization.csv를 불러온다

original_data = open('data\Organizing-Data\BAND-DATA_organization.csv', 'r', encoding='utf-8')

# csv.reader를 사용하여 데이터를 읽어온다
original_data = csv.reader(original)

# data\Organizing-Data\BAND-DATA_organization.csv를 저장할 파일을 만든다

new_data = open('data\Organizing-Data\BAND-DATA_organization-2.csv', 'w', encoding='utf-8')

# 뒤쪽 라벨이 1이고 다음 문단의 라벨이 2일 경우 두 문단을 묶어서 저장하는 함수를 만들자
# 이때 1라벨은 질문 2라벨은 답변으로 저장하게 코드를 작성하자 

def organize_data(original_data, new_data):
    for i in original_data:
        if i[2] == '1':
            q = i[1]
        elif i[2] == '2':
            a = i[1]
            new_data.write(q + ',' + a + '\n')

# 막상 파일 형식 보니까 이거 어케하냐 ;;;