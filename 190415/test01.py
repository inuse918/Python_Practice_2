a=int(input("정수를 입력하시오 : "))
b=int(input("정수를 입력하시오 : "))

if a>=b:
    print(a,"을(를) ",b,"(으)로 나눈 몫 = ",a//b," 나머지 = ",a%b)

elif a<b:
    print(a, "을(를) ", b, "(으)로 나눈 몫 = ", a // b, " 나머지 = ", a % b)