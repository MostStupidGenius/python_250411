# part4_file_expand.py
# 파일 입출력 심화
# 파일 입출력을 할 때
# open() 함수로 파일 객체를 만들고 이를 다룬 뒤
# close()함수로 닫아주기까지가 너무 귀찮았다.
# with open(): 구문을 이용하면, with 구문을 벗어날 때
# 자동으로 .close()가 동작하게 된다.
file_name = 'test.txt'
def file_read():
  # with만 앞에 붙이고 뒤에 콜론:만 적어주면
  # 해당 코드블록 안에서만 file 객체가 열려있게 된다.
  with open(file_name, 'r', encoding='utf-8') as file:
    # as file은 open()으로 연 파일 객체를 가리킨 별칭을 정하는 곳이다.
    lines = file.readlines()
  
  for line in lines:
    print(line)

import csv
def read_csv():
  with open('people.csv', 'w', encoding='utf-8-sig') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow(['이름', '나이'])
    writer.writerow(['홍길동', 30])

  with open('people.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    rows = list(reader)
    for row in rows:
      print(row)
data = {
  '이름': '홍길동',
  '나이': 30
}
import json
def write_json():
  with open('file.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    # indent는 들여쓰기를 표현할 때
    # 띄어쓰기문자를 몇 개 사용할지를 정하는 부분이다.(일반적으로 4 사용)
  
  with open('file.json', 'r', encoding='utf-8') as file:
    content = json.load(file)
    print(content)
# 하위 폴더에 파일을 만드려면
# open('./day10/file.json')과 같이 작성해야 한다.
# 상대 경로

# 절대 경로
# 드라이브 문자부터 작성한 파일 경로를 절대 경로라고 부르며
import os
# OS와 무관한 절대 경로로 변환하는 함수
file_path = os.path.abspath('./day10/file.json')
print(file_path)


if __name__ == "__main__":
  # file_read()
  # read_csv()
  write_json()

