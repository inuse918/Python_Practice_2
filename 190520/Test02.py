from random import randint

print("*****가위바위보게임*****")

while True:
    print("다음 중 하나를 선택하세요.")
    user = int(input("가위(0), 바위(1), 보(2), 종료(3) : "))
    if user==3:
        print("종료합니다.")
        break
    com = randint(0, 2)
    if com==0:
        print("컴퓨터는 가위를 냈습니다.")
        if user==0:
            print("비겼습니다.\n")
        elif user==1:
            print("이겼습니다.\n")
        elif user==2:
            print("졌습니다.\n")

    if com==1:
        print("컴퓨터는 바위를 냈습니다.")
        if user==0:
            print("졌습니다.\n")
        elif user==1:
            print("비겼습니다.\n")
        elif user==2:
            print("이겼습니다.\n")

    if com==2:
        print("컴퓨터는 보자기를 냈습니다.")
        if user==0:
            print("이겼습니다.\n")
        elif user==1:
            print("졌습니다.\n")
        elif user==2:
            print("비겼습니다.\n")


