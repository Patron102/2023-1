#1
'''
import bb #bb를 불러오겠다.

bb.bb01()
bb.bb02()
bb.bb03()

print(bb.cnt)
'''

#2
'''
import bb as b #bb를 불러오고 b라고 줄이겠다.

b.bb01()
b.bb02()
b.bb03()

print(b.cnt)
'''

#3
'''
from bb import * #해당 모듈에 있는 모든 것을 쓰겠다.

bb01()
bb02()
bb03()

print(cnt)
'''

#4
from bb import bb01, cnt #해당 모듈에서 원하는 것만 쓰겠다.
bb01()
print(cnt)
bb02() #안불러와서 오류 발생
bb03() #안불러와서 오류 발생