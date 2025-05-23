# part4_generator.py
# 제너레이터(generator)
# 리스트 컴프리헨션처럼 여러 개의 요소를 가지고 와서
# 사용하는 목적으로 만들어진 문법이다.
# 하지만, 모든 요소를 만든 뒤에 동작하는 것이 아니라
# 필요할 때마다 해당 되는 요소를 그때그때 '생성'하여 반환한다는 점이
# 가장 크게 다른 점이다.
# 때문에 대량의 데이터를 다룰 때 유용하다.
# 소괄호() 안에 리스트 컴프리헨션과 같은 문법으로 작성한다.
gen = (e for e in range(1, 100+1))
next(gen)
for e in gen:
  # 각 요소를 임시 변수 e에 담아 사용한다.
  if e > 20: break
  print(e)
# 매 반복마다 요소를 생성하여 반복문을 실행하기 때문에
# 모든 요소를 만들어두는 리스트 컴프리헨션보다
# 메모리 효율적이며 수행속도가 더 빠르다.
