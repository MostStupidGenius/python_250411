# part1_magic_method_practice.py
# 매직 메서드의 더하기 연산자를 이용하여
# 좌표값을 보유한 클래스의 연산에 활용하는 예제
import math # 수학적인 계산을 도와주는 라이브러리 가져오기

class Coordinator():
    def __init__(self, x: int, y: int):
        self.x = x # x 좌표값
        self.y = y # y 좌표값
    
    # 두 좌표의 값을 각각 더해서 새로운 좌표를 가진
    # Coordinator클래스 타입의 객체를 만들어 반환
    def __add__(self, other):
        return Coordinator(self.x + other.x, self.y + other.y)
    
    # 두 좌표 사이의 거리를 피타고라스의 정리로 구하여
    # 실수로 반환하는 함수
    def get_distance(self, other):
        x_distance = abs(self.x - other.x) # 두 좌표의 x 값 차이
        y_distance = abs(self.y - other.y) # 두 좌표의 y 값 차이
        return math.sqrt(x_distance ** 2 + y_distance ** 2)

    def __str__(self):
        return f"({self.x}, {self.y})"
    
if __name__ == "__main__":
    onezom = Coordinator(2, 3)
    other = Coordinator(3, 4)
    print(onezom + other) # (5, 7)
    print(onezom.get_distance(other)) # 루트2 1.4142135623730951




