import csv

#파일 가져오기 'r':읽기, 'w':쓰기, 'a':마지막 라인에 새 내용 추가하기
file = open(r"C:\Users\tjd03\OneDrive\바탕 화면\과제\오픈소스 프로그래밍\팀플\데이터\DATA\KAKAO-DATA.txt", "r", encoding = 'UTF-8')
#정리한 데이터셋 넣을 새 파일 생성
new_file = open(r"C:\Users\tjd03\OneDrive\바탕 화면\과제\오픈소스 프로그래밍\팀플\데이터\DATA\KAKAO-DATA_organizing.csv", "w", encoding = "UTF-8")

#파일의 번호 제거하고 문장 끝에 ,'제거한 번호' 붙이기
while True:
    line = file.readline()
    if not line:
        break
    if "1 : " in line:
        new_line = line.replace("1 : ","").replace("\n",",1\n")
        if "\n" not in line:
            new_line = new_line + ",1"
    elif "2 : " in line:
        new_line = line.replace("2 : ","").replace("\n",",2\n")
        if "\n" not in line:
            new_line = new_line + ",2"
    elif "3 : " in line:
        new_line = line.replace("3 : ","").replace("\n",",3\n")
        if "\n" not in line:
            new_line = new_line + ",3"
    new_file.write(new_line)
file.close()