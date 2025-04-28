# 함수형 프로그래밍
# 람다식을 배우기 전에 함수형 프로그래밍을
# 먼저 배운다.
# map, filter, reduce

def jegop(num):
  return num ** 2

# 코드 실행부
if __name__ == "__main__":
  # map(함수, 이터러블)
  # 이터러블 객체(시퀀스)의 요소 하나하나에 같은 함수를 동작시켜
  # 그 결과 값으로 요소를 이루는 새로운 시퀀스를 생성하는 함수
  nums = [1, 2, 3, 4]
  jegop_nums = map(jegop, nums)
  # map, filter의 결과를 리스트처럼 요소로 보고자 한다면
  # 반드시 형변환해야 한다.
  print(list(jegop_nums))

  # filter
  # 전달된 조건식을 만족하는 요소만 뽑아서
  # 새로운 시퀀스를 반환하는 함수다.
  print(nums)
  filtered = filter(lambda x: x % 2 == 0, nums)
  print(list(filtered)) # [2, 4]

  # reduce
  # 전달된 함수의 동작을 수행하여 요소들을 순차적으로 처리,
  # 그 결과를 단일 값으로 줄여준다.
  # 이 함수는 functools 모듈에서 import 해야 한다.
  from functools import reduce
  numbers = list(range(1, 10+1))
  # 첫 요소부터 순차적으로 각 요소를 모두 더해
  # 총 합을 반환한다.
  sum_all = reduce(lambda x, y: x + y, numbers)
  # 0번째 요소를 x에 대입, 1번째 요소를 y에 대입하여
  # 그 결과 값을 다음 요소에 대해 함수 실행할 때
  # x에 대입한다. y에는 다음 요소 값이 들어간다.
  # 최종적으로 결과값은 단일 값이 나오게 된다.
  print(sum_all)
