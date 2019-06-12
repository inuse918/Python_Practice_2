def birthday(name):
    for i in range (1,5):
        if i==3:
            print("Happy Birthday, dear",name)
        else:
            print("Happy Birthday to you!")

user=input("이름을 입력하세요: ")
birthday(user)
