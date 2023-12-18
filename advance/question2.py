try :
    file = open("demo.txt" , "w")
    l1 = "first line in demo"
    l2 = "second line in demo"
    l3 = "third line in demo"
    file.write(l1+"\n")
    file.write(l2 + "\n")
    file.write(l3 + "\n")
    file.close()
    file = open("demo.txt","r")
    for words in 
except FileNotFoundError:
    print()