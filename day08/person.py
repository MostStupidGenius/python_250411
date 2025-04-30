# person.py
# Person 클래스를 정의할 파이썬 파일
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print(f"my name is {self.name}. and i eat {food}")

print("filename: ", __name__) # person
if __name__ == "__main__":
    hong = Person("홍길동", 30)
    hong.eat("스파게티")