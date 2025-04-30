# part3_class_practice.py
# 실습1. 학생(Student) 클래스를 만들고
# 이름(name), 점수(kor, math, eng)를 세 개 전달 받아서
# 각각 클래스의 속성으로 저장한 뒤
# 객체.name, 객체.score['kor']와 같은 방식으로
# 값을 출력하는 내용을 작성해보자.

# 1. 클래스 만들기
# name: 문자열
# score: dict 자료형으로 작성
class Student():
# 2. __init__ 메서드 작성해보기
  def __init__(self, name: str, score: dict, kor, math, eng):
    self.name = name 
    self.score = score
    self.score2 = {
      'kor': kor,
      'math': math,
      'eng' : eng
    }

# 3. if __name__ == "__main__":
# 코드 블록에 객체화 Student()와
# 객체의 정보를 출력하는 내용 작성
if __name__ == "__main__":
  score = {
    'kor': 80, 
    'math': 90,
    'eng' : 75
  }

  hong = Student('홍길동', score, 90, 91, 92)
  print(hong.name)
  print(hong.score['kor'])

  print(hong.score2['kor'])