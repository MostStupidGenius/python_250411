# part4_magic_method3_oper.py
# 매직 메서드 중 연산자 메서드
# 이전의 매직 메서드들과 다르게 다른(other) 객체와의
# 상호작용을 전제로 한다.
# 매직메서드의 매개변수로 self뿐만 아니라 
# 다른 객체를 나타내는 other도 같이 전달된다.
# 그 외에 다른 매개변수를 정의할 수 없다.
class Number:
    def __init__(self, value: int):
        self.value = value # Number 클래스의 내부값
    
    # 내부값인 self.value를 연산에 활용할 예정입니다.
    # 더하기 연산
    # 다른 객체와의 더하기 연산을 했을 때
    # 다른 객체의 어떤 정보와 연산을 할지 정의하는 매직 메서드다.
    def __add__(self, other):
        result = self.value + other.value
        result = Number(result)
        return result

    def __str__(self):
        return f"{self.value}"

if __name__ == "__main__":
    num1 = Number(3)
    num2 = Number(7)
    result = num1 + num2
    print(result)
    print(num2 + result)