# part2_class_method.py
# 클래스 외부에 존재하는 기능 덩어리는 함수라고 부른다.
# 클래스 내부에 만든 함수는 메서드(method)라고 부른다.

# 클래스 내부에 만드는 메서드는
# 기본적으로 객체를 통해서만 사용이 가능하다
class Student:
  # 초기화 메서드(생성자)
  def __init__(self, name: str, age:int):
    self.name = name
    self.age = age
  
  # 객체가 할 수 있는 동작을 정의
  # 객체의 정보를 출력하는 메서드 만들기
  # ★self가 포함된 메서드
  def print_info(self):
    # 객체의 정보에 접근하려면 첫번째 매개변수로
    # 반드시 self를 넣어주어야 한다.
    print(f"my name is {self.name} and age is {self.age}")
  
  # 클래스 내부에 작성된 함수.
  # self 없이 작성되어 있다.
  # 이러한 함수는 클래스이름.함수이름() 와 같은 방식으로
  # 사용할 수 있다.
  def add(num1, num2):
    print(num1 + num2)

if __name__ == "__main__":
  kim = Student("김구", 40)
  kim.print_info() # 클래스 내부에 만든 기능 호출

  lee = Student("이순신", 30) # 다른 객체(대상)
  lee.print_info()

  # self가 없는 메서드 호출
  Student.add(3, 5) # 8
  # lee.add(3, 5) # error 발생
  # 객체.메서드()는 내부적으로 self라는 예약어가 같이 전달되기 때문에
  # 객체는 self를 필요로 하지 않는 메서드를 사용할 수 없다.
