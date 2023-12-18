try :
    file = open("demo.txt" , "r")
    # file.read()
    cnt = 0
    content= file.read()
    for ele in content:
        if ele == "\n":
            cnt += 1
    print(cnt)
except FileNotFoundError:
    print("not found")