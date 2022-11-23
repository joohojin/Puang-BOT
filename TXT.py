import os
import glob

# 파일들이 있는 경로
path = r'여기에 경로 입력'

# 파일들을 읽어서 하나의 파일로 만들기
files = glob.glob(os.path.join(path, '*.txt'))
with open(os.path.join(path, '여기에 텍스트 파일 이름 입력.txt'), 'w', encoding='utf-8') as outfile:
    for fname in files:
        with open(fname, encoding='utf-8') as infile:
            outfile.write(infile.read() + '\n')