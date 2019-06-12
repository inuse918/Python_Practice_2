phone_book={"손영재":"010-2345-6789"}
phone_book["이상연"]="010-1234-5678"

#print(phone_book)
#{'이상연':'010-1234-5678','손영재':'010-2345-6789'

for key in sorted(phone_book.keys()):
    print(key, phone_book[key])
