sum=0
while True:
    user = int(input("정수를 입력하시오: "))
    if user==0:
        break
    sum+=user
print("합은 ",sum,"입니다.")