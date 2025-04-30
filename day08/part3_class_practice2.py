# part3_class_practice2.py
# 실습2
# 계산기 클래스 만들어 계산해보기
# Calculator
# 속성: 현재 계산결과를 담을 변수 하나
# 기능: 덧셈, 뺄셈, 곱셈, 나눗셈, 결과 출력

class Calculator():
    def __init__(self):
        self.result = 0 # 현재 계산결과를 담을 변수
    
    # 덧셈
    def add(self, num:int):
        self.result += num
        return self.result

    # 뺄셈
    def sub(self, num:int):
        self.result -= num
        return self.result

    # 곱셈
    def multi(self, num:int):
        self.result *= num
        return self.result
    
    # 나눗셈
    def divide(self, num:int):
        if num == 0:
            return 0
        self.result /= num
        return self.result
    
    # 계산 결과를 반환하는 기능
    def get_result(self):
        return self.result

if __name__ == "__main__":
    cal = Calculator()
    cal2 = Calculator()
    print(cal.get_result()) # 0

    cal.add(7) # 0 + 7
    # cal2.add(13) # 0 + 13
    cal.multi(9) # 7 * 9
    # cal2.multi(4) # 13 * 4
    cal.sub(3) # 63 - 3
    # cal2.sub(2) # 52 - 2
    cal.divide(6) # 60 / 6
    # cal2.divide(10) # 50 / 10
    print(cal.get_result()) # 10.0
    # print(cal2.get_result()) # 5.0