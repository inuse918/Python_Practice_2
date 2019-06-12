heroes=[]
heroes.append("아이언맨")
heroes.append("닥터 스트레인지")
heroes.append("헐크")
print(heroes)
heroes.append("스파이더맨")
print(heroes)

heroes.insert(1,"배트맨")
print(heroes)

heroes.remove("닥터 스트레인지")
print(heroes)

if "배트맨" in heroes:
    heroes.remove("배트맨")

print(heroes.index("스파이더맨"))
