
try:
    file = open("doc.txt","w")
    l1 = "Hello I am a file"
    l2 =  "Where you need to return the data string"
    l3 = "Which is of even length"
    file.write(l1 + "\n")
    file.write(l2 + "\n")
    file.write(l3)
    file.close()

    file  = open("doc.txt","r")
    words = file.read()
    split_words =words.split()
    res = []
    for ele in split_words:
        if len(ele) % 2 == 0:
            res.append(ele)
    ans = " ".join(res)
    print(f"string of even length: {ans}")
except FileNotFoundError:
    print("not found")