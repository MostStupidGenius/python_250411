# part2_file_handling_basic.py
# 파일 처리
# 파이썬 코드를 이용해서 파일을 열어서 읽거나 쓰는 작업을
# 파일 처리라고 부른다.
# 데이터를 읽거나 쓰기 위해서, 혹은 환경설정 정보를 저장하고(.env)
# 나중에 다시 불러오기 위해서(반영구 저장)

# 파일을 읽든 쓰든 그 파일을 열어야 한다.
# open(파일경로, 열기모드)
# 해당 파일을 파이썬에서 다룰 수 있는 객체로 바꿔주는 함수이며
# 열기 모드에는 쓰기(w), 읽기(r), 추가(a) 등의 모드가 있다.
# 이러한 모드 뒤에 +를 붙이면 읽기와 쓰기 모두를 지원하는 모드가 된다.
file_name = 'test.txt' # 전역 변수 file_name
# 전역변수는 어떤 함수든 이 아래쪽에 만들어지는 어디서든
# 접근하고 사용할 수 있다.
# 일반적으로 하나의 .py 파일 안에서 공통적으로 쓰이는 값을 선언하고
# 재사용하고자 할 때 사용하는 방식이다. 남용 금지.

# 파일 객체 생성하기
def make_file_obj():
    # 쓰기 모드로 파일 객체 생성
    file = open(file_name, 'w')
    # 쓰기 모드로 열었기 때문에 해당 경로에 파일이 없으면
    # 파일을 생성한 뒤 내용을 작성한다.
    file.write('new line 1st\n')
    file.write('new line 2nd')
    # write 함수는 전달된 문자열을 줄바꿈없이
    # 이어서 텍스트 파일에 작성한다.
    # 줄바꿈이 필요하다면 \n을 활용해야 한다.
    # 'w'모드는 이전에 파일이 있었다면 그 내용을 모두 삭제한 뒤
    # 처음부터 작성하기 때문에 조심해서 사용해야 한다.
    
    # 파일 객체는 모든 동작을 수행한 뒤, 반드시 닫아주어야 한다.
    file.close()

def append_content():
    file = open(file_name, 'a') # append의 'a' 모드 사용
    # 'a'모드는 기존에 파일이 없으면 생성한 뒤 내용을 작성한다.
    # 만약 이미 파일이 존재하면, 기존 내용 뒤에 이어서 내용을 작성한다.
    file.write('\nnew line with append.\n')
    file.close()

# 기존에 존재하는 파일의 내용을 읽어오는 함수
def read_file():
    file = open(file_name, 'r') # 파일을 읽기 모드로 연다
    # 파일의 내용을 읽는 방법은 두 가지가 있는데
    # 1. 전체 내용을 통째로 읽어오는 .read()
    content = file.read()
    # 모든 내용을 한꺼번에 들고 오기 때문에, 많은 내용이 있을 경우
    # 처리가 느려지거나 읽어서 다루기가 힘들 수 있다.
    print(content)
    file.close()

def read_file_lines():
    # 텍스트 파일의 내용을 한줄씩 읽어오는 예제
    file = open(file_name, 'r')
    # 2-1. 한줄씩 읽어오는 함수
    # line = file.readline()
    # print(line)
    # line = file.readline()
    # print(line)
    
    # 2-2. 각 줄을 요소로 하는 객체 반환 함수
    lines = file.readlines()
    for i, line in enumerate(lines, 1):
        print(f"{i}. {line}", end='')
    file.close()

if __name__ == "__main__":
    # make_file_obj() # 파일 생성 및 쓰기 모드
    # append_content() # 기존 파일 뒤에 내용 이어 붙이기
    # read_file() # 파일 통째로 읽어오는 예제
    read_file_lines() # 한줄씩 읽어오는 예제
    




