
try:
    file = open("doc.txt","w")
    l1 = ["Hello I am a file "]
    l2 = "Where you need to return the data string"
    l3 = "Which is of even length"
    l = [l1,l2,l3]
    file.readline(l1)
    file = open("doc.txt","r")
    print(file.readline()) 

    
except FileNotFoundError:
    print(f"file not found")