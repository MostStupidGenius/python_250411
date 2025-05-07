# part2_inheritance.py
# 상속(inheritance)
# 상속이란, 클래스의 특성과 기능을 그대로 물려받아서
# 재사용할 수 있게 해주는 시스템을 가리킨다.
# 상속을 하는 쪽을 부모클래스, super클래스 등으로 부르며
# 상속을 받는 쪽을 자식클래스, sub클래스 등으로 부른다.

# 자식클래스는 부모클래스로부터 받은 특성이나 기능을
# 그대로 사용할 수도 있지만, 변경하거나 새로운 내용을 추가하는 등의
# 동작도 가능하다.

# 상속을 받는 방법
# 클래스를 선언할 때 클래스 이름 뒤에 소괄호() 안에
# 상속받고자 하는 부모클래스 이름을 적어주면 된다.

# 예시: Animal 부모 클래스와 상속받은 Dog, Cat 클래스
class Animal():
    def __init__(self, name):
        self.name = name
    
    def bark(self): # 짖는, 소리치는 기능
        print(f"{self.name}이 소리내어 웁니다.")

# Dog 클래스는 Animal클래스의 특성과 기능을 그대로 물려받는다.
class Dog(Animal):
    # 상속받은 내용 중 변경한 내용과
    # 새로 추가한 내용만 작성하면 된다
    # 기존 Animal클래스의 bark 기능을 수정하겠다.
    def bark(self):
        # return super().bark() # 부모클래스의 bark()기능을 그대로 사용
        # 메서드의 내용을 바꿔서 부모로부터 받은 기능을 변경
        print(f"{self.name}은 멍멍 짖습니다.")
        # 오버라이드는 같은 이름의 메서드면서 같은 개수의 매개변수를 가져야만
        # 오버라이드가 성립된다.
        # 이때 메서드의 이름과 매개변수의 개수를 가리키는 명칭은
        # 바로 시그니처이다.
        # 즉, 시그니처가 같아야 같은 메서드로 취급한다.

class Cat(Animal):
    # Cat클래스는 부모로부터 받은 기능을 그대로 사용할 것이다.
    pass
    def bark(self):
        super().bark() # 부모클래스가 정의한 기능 수행
        # return을 하지 않으면 메서드가 종료되지 않기 때문에
        # 이어서 다른 작업을 수행할 수 있다.
        print(f"그리고 {self.name}은(는) 야옹하고 웁니다.")
    
    # 부모로부터 상속받지 않은 기능을 추가
    def sleep(self):
        print(f"고양이는 낮에 잠을 잡니다.")

if __name__ == "__main__":
    ani = Animal("동물1")
    ani.bark() # 부모클래스에서 정의한 기능 수행
    
    baduki = Dog("바둑이")
    baduki.bark() # 자식클래스에서 변경한 기능을 수행

    kong = Cat("콩")
    kong.bark() # 변경되지 않은, 상속받은 내용 그대로 기능 수행
    kong.sleep() # 부모로부터 상속받지 않은, 새로 정의한 기능 수행

    print("=" * 20)

    # Animal 클래스를 상속받은 객체들을 담은 리스트
    # 자식클래스가 부모클래스 타입으로 묶여서 관리되거나
    # 부모클래스 타입을 보유한 것으로 취급되는 성질을
    # 다형성(polymorphism)이라고 한다.
    animals: list[Animal] = [baduki, kong]
    
    for animal in animals:
        animal.bark() # 내부의 자식객체가 각자의 bark() 기능을 수행
        # 부모클래스타입으로 묶여서 관리되지만
        # 재정의(Override)한 기능은 재정의한 그대로 기능이 수행된다.

        # animal.sleep() # Cat클래스에만 존재하는 기능이기 때문에
        # Dog 객체에 없는 기능이므로 오류가 발생한다.
