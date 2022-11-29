#txt 파일을 수정하고 csv 파일로 저장하는 프로그램
#csv 파일은 엑셀에서 열 수 있음

# E:\Puang-BOT\data\Validation Data\KAKAO-DATA.txt

import os
import csv

# 만약 csv 파일이 존재하면 삭제
def delete_csv():
    if os.path.exists('E:\Puang-BOT\data\Validation Data\KAKAO-DATA.csv'):
        os.remove('E:\Puang-BOT\data\Validation Data\KAKAO-DATA.csv')

#txt 파일의 코덱을 변경하여 읽어서 리스트로 저장
def read_txt():
    f = open('E:\Puang-BOT\data\Validation Data\KAKAO-DATA.txt', 'r', encoding='UTF-8')
    lines = f.readlines()
    f.close()
    return lines

#리스트에 1 : 이라는 문자열이 있으면 제거
def remove_1(lines):
    for i in range(len(lines)):
        if lines[i].find('1 : ') != -1:
            lines[i] = lines[i].replace('1 : ', '')
    return lines

#리스트에 2 : 이라는 문자열이 있으면 ,로 변경
def change_2(lines):
    for i in range(len(lines)):
        if lines[i].find('2 : ') != -1:
            lines[i] = lines[i].replace('2 : ', ',')
    return lines

# 리스트를 두개씩 묶어서 리스트로 저장
def make_list(lines):
    list = []
    for i in range(0, len(lines), 2):
        list.append([lines[i], lines[i + 1]])
    return list


# 코덱을 변경하여 csv 파일로 저장
def write_csv(lines):
    f = open('E:\Puang-BOT\data\Validation Data\KAKAO-DATA.csv', 'w', encoding='UTF-8', newline='')
    wr = csv.writer(f)
    for line in lines:
        wr.writerow(line.split(','))
    f.close()

# csv 파일을 읽어서 리스트로 저장    
def read_csv():
    f = open('E:\Puang-BOT\data\Validation Data\KAKAO-DATA.csv', 'r', encoding='UTF-8')
    rdr = csv.reader(f)
    lines = []
    for line in rdr:
        lines.append(line)
    f.close()
    return lines

# "부호를 제거
def remove_quotation(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j] = lines[i][j].replace('"', '')
    return lines

# 문단 줄바꿈을 ,3으로 변경하고 줄바꿈 추가
def change_paragraph(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j] = lines[i][j].replace('\n', ',3\n')
    return lines

# 미션 수행

delete_csv()
lines = read_txt()
lines = remove_1(lines)
lines = change_2(lines)
lines = make_list(lines)
write_csv(lines)
lines = read_csv()
lines = remove_quotation(lines)
lines = change_paragraph(lines)
write_csv(lines)

