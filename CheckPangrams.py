def checkPangrams(String):
    flag = False
    alph=list("abcdefghijklmnopqrstuvwxyz")
    unq=[]

    for i in String:
        if i in alph and i not in unq :
            unq.append(i)


    if len(unq) == 26:
        flag = True
    return flag

if checkPangrams(list(input("Enter the String.:").lower())):
    print("It is a Pangram.")
else:
    print("It is not a Pangram.")