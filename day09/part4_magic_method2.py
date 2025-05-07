# part4_magic_method2.py
# __del__ 매직메서드
# del을 이용하여 객체를 소멸시킬 때(객체를 삭제)
# 어떤 동작을 수행한 뒤 객체를 소멸시킬지 정의한 특수 메서드다.
class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def __del__(self):
        # 객체가 삭제될 때 수행할 동작 정의
        print("객체 삭제")
    
    # 객체의 문자열 표현을 위한 메서드들
    # __str__
    # __repr__
    # str()함수에 객체가 전달되거나 print()함수에
    # 전달되어 문자열로 표현되는 경우에 호출되는 메서드들이다.
    def __str__(self) -> str: # 문자열 타입을 반환
        return f"{self.brand} is __str__"
    
    def __repr__(self) -> str:
        return f"{self.brand} is __repr__"

if __name__ == "__main__":
    bongo = Car("봉고차")
    # del bongo # 객체 삭제
    # print(bongo.brand) # 객체가 삭제되었기 때문에
    # 해당 객체에 더이상 접근할 수 없다.
    print("=" * 20)
    # 문자열 표현 매직 메서드 사용
    print(bongo) # 둘 다 __str__ 매직메서드 호출
    print(str(bongo))
    # __str__ 매직메서드와 repr 매직메서드 중
    # str 매직메서드가 우선순위가 더 높아서
    # 동시에 정의된 경우, str에 정의된 값이 반환된다.
    # repr()함수에 객체를 전달할 경우에는
    # repr매직메서드로 정의한 값이 반환된다.
    print(repr(bongo))

    # 위에서 del로 객체를 삭제하지 않은 경우
    # 현재 .py파일의 실행이 종료되는 때에
    # 소멸자가 호출된다.