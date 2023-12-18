def userprofile( username,password):
    new_pass = input("Please Re-Enter the password:")
    if new_pass != password:
        cnt = 3 
        correctcnt = 0
        for i in range(3):
            print("Password is incorrect, Please re-enter password, you have", cnt , "chance")
            cnt -= 1
            make_pass = input()
            if make_pass == password:
                break
            else:
                correctcnt +=1 
        if correctcnt >= 3 :
            return "Sorry Password authentication failed, you enter wrong password"
        else:
            return "welcome " +username



    return "welcome " + username

username = input("Enter the Username:")
password = input("Enter the Password:")
print(userprofile(username,password))