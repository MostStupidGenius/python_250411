# 함수(function)
# 함수란 반복적으로 사용할 코드 덩어리, 블록을
# 특정 이름을 붙여서 쉽게 호출하여 사용하기 위해
# 미리 만들어두는 부품같은 기능적 요소를 가리킨다.
# 함수의 구성요소
# 1. 함수명
# 2. 매개변수(parameter)
# 3. 함수 코드블록(body)
# 4. 반환값(return)
# 두 값을 전달받아서 그 합을 반환하는 함수
def add(num1, num2): # 매개변수의 선언
  # 외부에서 전달받을 값이 무엇인지 모르기 때문에
  # 그 값을 가리킨 변수를 정해주어야 한다. -> 매개변수
  
  # 함수의 내부, body에서는 전달받은 매개변수를 활용하여
  # 수행할 기능을 작성, 구현해야 한다.
  # 이때 되돌려줄 값이 있다면 미리 변수를 만들어두는 게 좋다.
  result = num1 + num2 # 수행할 코드 작성

  # 함수를 호출, 사용한 쪽에서 활용할 수 있는 값을 되돌려주려면
  # return 예약어 뒤에 되돌려 줄 값을 적어주면 된다.
  return result
  # return의 역할
  # 1. 함수에서 그 결과값을 되돌려주는 역할
  # 2. 함수를 종료하고 코드의 흐름을 함수 호출부로 넘기는 역할
  # -> return을 만난 이후의 코드는 실행되지 않는다.
  # 마치 반복문에서 break와 같이 코드의 흐름이 호출부로 넘어가게 된다.

# 함수를 정의(def)하는 것만으로는 실행되지 않는다.
# 함수명과 함께 필요한 매개변수의 값을 전달해주면
# 함수가 실행된다.
result = add(3, 7)
print(result)

# 사칙연산을 수행하는 3 개의 함수 작성
# 1. 첫번째 매개변수에서 두번째 매개변수를 뺀 값을 반환하는 함수
def sub(num1, num2):
  result = num1 - num2
  return result

# 2. 순서대로 곱한 값을 반환하는 함수
def multi(num1, num2):
  result = num1 * num2
  return result

# 3. 순서대로 나눈 값을 반환하는 함수
# 단, 두번째 매개변수가 0이면(if) return 0를 수행
def divide(num1, num2):
  # 만약 num2의 값이 0이라면
  if num2 == 0:
    return 0 # return 예약어를 만나면
    # 그 아래의 코드는 실행하지 않기 때문에
    # 굳이 else를 쓰지 않아도 된다.
  result = num1 / num2
  return result
  # 한줄 코드
  # 만약 num2가 0이라면 0을 result에 할당하고
  # 아니라면 num1 나누기 num2를 result에 할당해라
  result = 0 if num2 == 0 else num1 / num2
  return result

print(sub(10, 3)) # 7
print(multi(3, 7)) # 21
print(divide(32, 8)) # 4.0
print(divide(8, 0)) # 0

# 기능을 수행한 뒤 반환값 없이 종료하는 함수
# 이름과 나이를 입력하면 소개문을 출력하는 함수
def introduce(name :str, age :int) -> None: # 매개변수 뒤에 콜론:과 함께
  # 타입을 적어주면 해당 매개변수에 타입힌트를 남길 수 있다.
  # 매개변수 소괄호() 뒤에 ->와 함께 타입을 적어주면
  # 어떤 값을 반환할지 힌트를 줄 수 있다.
  # None은 반환하는 값이 없음을 의미한다.
  print(f"이름은 {name}이구요, 나이는 {age}살입니다.")
  # return 없이 함수를 끝내면 된다.(return 작성은 선택)
  # 다만, 중간에 함수를 종료해야 하는 경우,
  # return 뒤를 비우면
  # return의 두 가지 기능 중 함수 종료 기능만 이루어진다.
  return 
  print("실행되지 않는 부분")

introduce("홍길동", 30)
introduce("이준상", 40)
introduce("이준상2", 50)
introduce("이준상3", 20)
introduce("이준상4", 10)