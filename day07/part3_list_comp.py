# part3_list_comp.py
# 리스트 컴프리헨션(list comprehension)
# 직전에 배웠던 map, filter를 적용하여 리스트를 생성하는
# 새로운 문법이다.
# 리스트를 만들 때처럼 대괄호[] 안에
# 한 줄로 적는 for문을 작성해준다.
# [표현식 for 임시변수 in 이터러블]
# 이터러블 객체의 각 요소를 임시변수에 담아서
# 표현식의 결과를 새로운 요소로 하는 리스트를 반환(map)

# 매개변수 뒤에 = 대입연산자로 값을 넣는 것은
# 해당 매개변수에 값을 세팅하지 않더라도
# 기본값을 대신 쓸 수 있도록 하는 것을 의미한다.
def make_list(start:int, end:int, jegop:int = 1): # start부터 end까지의 값을 가지는
  # 리스트를 반환하는 함수
  result = [e ** jegop for e in range(start, end+1)]
  return result

def make_list_with_filter(start, end):
  # 만약 해당 요소를 2로 나눴을 때 나머지가 0이라면
  # 해당 요소를 새로운 리스트의 요소로 넣어라.
  result = [e for e in range(start, end+1) if e % 2 == 0]
  return result

def test1():
  # 1부터 100까지의 range 객체를 대상으로
  # 각 요소에 3을 곱한 값이 짝수인 요소만 골라서
  # 각 요소에 2를 곱한 값으로 이루어진
  # 새로운 리스트를 반환해라.
  result = [e * 2 for e in range(1, 100+1) if (e * 3) % 2 == 0]
  return result

if __name__ == "__main__":
  # my_list = make_list(1, 10)
  # print(my_list)
  # my_list_2 = make_list(1, 10, 2) # 제곱으로 바꾸어 리스트를 만든다.
  # print(my_list_2)
  # my_list_filtered = make_list_with_filter(1, 100)
  # print(my_list_filtered)
  result = test1()
  print(result)
