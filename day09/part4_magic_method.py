# part4_magic_method.py
# 매직 메서드
# 파이썬 언어에서 미리 정해놓은 특정 동작을 수행 할지를 
# 정해놓은 특수한 메서드다.
# __init__ : 객체를 생성할 때 초기값을 세팅하게 도와주는
# 특수한 메서드

# __new__ : 객체를 생성할 때 동작할 내용을 작성하는 메서드
class Car:
    def __init__(self, brand):
        self.brand = brand
        print("초기화")

    def __new__(cls):
        print("객체 생성")
        cls.print_something() # 객체와 무관한 기능을 수행
        # 객체 정보 없이 동작할 기능을 미리 수행해놓을 수 있다.

    def print_something():
        print("자동차")

if __name__ == "__main__":
    bongo = Car()
    # __new__ 매직 메서드가 __init__ 매직메서드보다
    # 먼저 호출되어 값을 전달받는다.
    # 때문에 없는 매개변수인 brand의 값을 전달받기 때문에
    # 기대하지 않은 값이라는 오류를 일으킨다.

    # __init__ 혹은 __new__ 매직 메서드 중 하나만 사용해야 한다.
    # init은 객체를 생성하는 클래스에서 사용한다.
    # new는 객체 생성없이 클래스의 기능만 사용하고자 할 때
    # -> self없는 메서드만 정의한 경우에 사용한다.

    # bongo.name = "봉고차" # init이 동작하지 않아서
    # self.name이 선언된 적이 없기 때문에 오류가 발생한다.
    # print(bongo.name)
