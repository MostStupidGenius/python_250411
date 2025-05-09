# part3_except_handling.py
# 예외 처리
# 코드가 실행 중에 오류가 발생했을 때, 미리 예상한 오류인 경우
# 해당 되는 흐름으로 넘겨서 코드를 처리한 뒤
# 프로그램 종료를 하지 않고 이어서 코드가 실행되도록 하는 것을
# 예외라고 부르며, 이러한 예외를 정의하는 것을 예외 처리라고 한다.
# 비유: 비상 시 대응 요령, 지침
# try: except: finally:
# file = open('test1.txt', 'r')
# 없는 파일을 읽으려고 해서 에러가 발생했다.
try: # 예외처리 구문에 있어서 필수적인 부분
  # 오류가 발생할 수 있는 실행코드가 들어가는 부분
  file = open('test.txt', 'r')
  print("line 10")
  content = file.read()
  print("line 12")
  file.close()
  print('complete')
# except 오류 이름: # 해당 되는 오류가 발생했을 때
# 이 안의 코드가 실행된다.(선택)
except FileNotFoundError as e:
  print("파일을 찾을 수 없습니다.")
  print(e)
except Exception as e: # except 코드 블록은 elif문처럼
  # 여러 에러에 대해서 작성할 수 있으며
  # 그 중에서도 Exception이라는 녀석은 모든 예외를 가리킨다.
  # 즉, 모든 에러에 대해서 예외 처리를 하겠다는 의미이다.
  print(e)
  # 다만 Exception을 예외 처리하는 건 가능하면 하지 않는 것이 좋다.
  # 오히려 에러가 발생해서 프로그램이 종료되는 게 나을 때도 존재한다.
finally: # 위에서 오류가 발생했든 안 했든
  # 반드시 실행되는 코드 블록으로
  # except 혹은 finally 코드 블록 중 하나는 반드시 존재해야 한다.
  print("finally")

print("try-except구문 바깥쪽 코드")