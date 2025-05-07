# part3_inherit_multi.py
# 다중 상속
# 하나의 클래스는 여러 클래스를 상속받을 수 있다.
# 이때 상속받는 여러 클래스에 같은 이름의 메서드가 존재하면
# 상속받은 순서에 따라 우선순위가 적용되어
# 먼저 상속받은 클래스의 메서드를 상속받는다.
# class 자식클래스(부모1, 부모2,...):
class Mammal():
    def __init__(self, name):
        self.name = name
    def mammaling(self): # 젖을 먹이다.
        print("포유류는 젖을 먹입니다.")
    
    def not_breathing_in_water(self):
        print("포유류는 물속에서 숨을 쉴 수 없습니다.")

class Swimming():
    def swim(self):
        print("이 동물은 수영할 수 있습니다.")
    
    # 두 부모 클래스에 같은 이름의, 같은 매개변수 개수를 가지는
    # 메서드가 있는 경우
    # 먼저 상속받은 부모클래스의 메서드를 상속받는다.
    def not_breathing_in_water(self):
        print("이 동물은 물속에서 숨을 쉴 수는 없습니다.")

class Dolphin(Swimming, Mammal):
    pass

if __name__ == "__main__":
    dol = Dolphin("돌고래1")
    dol.mammaling() # 부모1로부터 받은 기능
    dol.swim() # 부모2로부터 받은 기능
    dol.not_breathing_in_water() # 두 부모 클래스에 모두 존재하는 메서드
    # 먼저 상속받은 부모 클래스의 메서드를 상속받아 수행한다.