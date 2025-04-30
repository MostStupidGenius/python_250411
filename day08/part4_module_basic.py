# part4_module_basic.py
# 모듈(module)
# 모듈이란 클래스, 함수, 변수 등을 하나의 파일에 
# 묶어서 관리하는 단위를 가리킨다.
# 혹은 클래스 하나가 하나의 모듈이 되기도 한다.
# 이러한 모듈은 다른 파이썬 파일에서 불러오기(import)로
# 그 기능이나 변수 등을 재사용할 수 있다.

# 같은 폴더 내에 있는 person.py 파일의
# Person 클래스를 가져와보자.
import person # 파일 통째로 가져오는 방법
# 이때 .py 확장자는 작성하지 않는다.
# 혹은 해당 파일에서 특정 클래스, 변수 등만 가져올 수도 있다.
# 이때는 from 뒤에 모듈 경로를 작성하고
# import 뒤에 가져올 대상(클래스, 변수) 등을 작성한다.
from person import Person
# from person import Person

if __name__ == "__main__":
    # 모듈로 임포트하는 경우에는
    # 그 내부의 요소를 사용할 때, 모듈.요소와 같은 방식으로
    # 접근해야 한다.
    kim_cs = person.Person('김철수', 35)
    
    # from 모듈 import 클래스
    # 모듈에서 특정 클래스, 변수 등을 명시적으로 작성하여
    # 임포트 했다면 그 이름 그대로 사용이 가능하다.
    kim = Person('김정은', 40)
    kim.eat('피자')

    # 만일 같은 이름 때문에 두 변수가 충돌, 덮어쓰기의 위험이 있다면
    # 별칭(alias)기능을 통해 가져올 때 새로운 이름을 부여하여
    # 구분하여 사용할 수 있다.
    # import 가져올녀석 as 별칭
    from person import Person as P
    park = P('park', 25)
    park.eat('cola')

