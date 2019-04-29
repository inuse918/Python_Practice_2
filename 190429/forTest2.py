user=int(input("정수를 입력하세요: "))

sum=1
for i in range(1,user+1):
    sum=sum*i

print("1 ~ ",user," 팩토리얼은 ",sum)