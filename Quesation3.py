print("MY LIBIRARY")
a = int(input("press 1 for fiction book: \npress 2 for non-fiction books: "))
if a == 1:
    b = str(input("enter book name:"))
    if b == "comedy":
        print("shelf A")
    if b == "comic":
        print("shelf B")
    if b == "science fiction":
        print("shelf c")
    if b == "fantacy":
        print("shelf d")
    if b == "historical fiction":
        print("shelf E")
       
if a == 2:
    c =  str(input("enter book name:"))
    if c == "history":
        print("shelf F")
    if c == "arts":
        print("shelf G")
    if c == "science":
        print("shelf H")
    if c == "other":
        print("shelf I")
    else:
        print("ERROR")    
      