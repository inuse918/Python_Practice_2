user=[]
sum=0
for i in range (5):
    ip=int(input("숫자를 입력하세요: "))
    user.append(ip)
    sum=sum+ip

print("평균은 ",sum/len(user),"입니다.")
