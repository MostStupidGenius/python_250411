# part5_module.py
# 모듈이란 클래스, 함수, 변수 등을 모아놓은 단위를 가리킨다.
# 기본적으로 모든 .py 파일은 하나의 모듈로 인식한다.
# import 파일이름
import part4_file_expand
# import를 하면 해당 모듈을 실행한다.
# 그래서 if __name__ == "__main__": 코드 블록이 없으면
# 모든 코드 실행되어서 테스트 코드까지 노출될 가능성이 생긴다.

print(part4_file_expand.file_name)

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from day10 import part1_magic_method_practice as p1
print(p1.Coordinator(1, 1))