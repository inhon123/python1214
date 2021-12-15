# try1.py
# 함수 정의
def divide(a,b):
    return a/b

# 함수 호출
try:
    result = divide(5,0)
    print("결과:{0}".format(result))
except ZeroDivisionError:
    print("0으로 나누면 안됩니다.")
except TypeError:
    print("0으로 나누면 안됩니다.")
finally:
    print("한번 더 체크(무조건 실행)")
print ("전체 코드 실행 종료")