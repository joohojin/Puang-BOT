import os
import glob

# 파일들이 있는 경로
path = r'F:\푸앙봇\020.주제별 텍스트 일상 대화 데이터\01.데이터\2.Validation\원천데이터\VS_01. KAKAO'

# 파일들을 읽어서 하나의 파일로 만들기
files = glob.glob(os.path.join(path, '*.txt'))
with open(os.path.join(path, 'KAKAO-Data.txt'), 'w', encoding='utf-8') as outfile:
    for fname in files:
        with open(fname, encoding='utf-8') as infile:
            outfile.write(infile.read() + '\n')