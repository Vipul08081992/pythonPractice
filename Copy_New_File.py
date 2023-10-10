

with open("test.txt","r") as fr:
    lines=fr.readlines()
    #print(lines)
with open( "new_test.txt","w") as fw:
    count = 0
    for line in lines:
        if count == 4:
            count += 1
            continue
        else:
            fw.write(line)
        count += 1

with open(r"C:\Users\vipul\PycharmProjects\Pratice\new_test.txt","r") as fw:
    lines=fw.readlines()
    print(lines)