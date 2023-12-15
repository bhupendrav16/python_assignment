def grade(sub):
    s_sub = sum(sub)
    perc = (s_sub/500)*100
    gr = ""
    if perc >= 90 :
        gr += "Grade A"
    
    elif perc >= 80 and perc < 90:
        gr += "Grade B"
    elif perc >= 70 and perc < 80:
        gr += "Grade C"
    
    elif perc  >= 60 and perc <70:
        gr += "Grade D"
    
    elif perc >=40 and perc < 60:
        gr += "Grade E"
    
    return gr 

l = [int(input()) for i in range(5) ]
print(grade(l))
