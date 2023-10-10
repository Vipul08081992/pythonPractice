def sortString(String):
    List= String.split("-")
    List_New = sorted(List)

    print("-".join(List_New))

sortString("green-red-yellow-black-white")