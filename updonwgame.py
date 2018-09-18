from random import randint




while True :
    asd=randint(1,101)
    count = 0
    while True :
        n=int(input("수를 입력하시오 : "))

        if n > asd :
            count += 1
            print("down")

        elif n < asd :
            count += 1
            print("up")

        else :
            print("True")
            break

    print(count)

    a=input("종료하시겠습니까? y/n")

    if a=='n':
        continue
    else :
        break

