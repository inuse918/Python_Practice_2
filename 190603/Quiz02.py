contacts={}
while True:
    name=input("입력) 이름을 입력하시오: ")
    if not name:
        break;
    tel =input("입력) 전화번호를 입력하시오: ")
    contacts[name]=tel


while True:
    name=input("검색) 이름을 입력하시오: ")
    if not name:
        break;
    if name in contacts:
        print(name,"의 전화번호는 ",contacts[name],"입니다. ")

