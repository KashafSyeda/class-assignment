print("ALIEN LANGUAGE TRANSLATOR")
a = int(input("select any one \n 1- To convert Alien language into English \n 2- to convert English into Alien language \n 3- To Add words in Dictionary : "))

word_bank = {'foraeh':'hello', 'myuso geh noog iea':'nice to meet you', 'vio':'bye', 'un':'i am', 'fukki':'happy', 'cuja':'sad', 'umtuli': 'angry', 'quo quumg':'we want', 'kouso':'peace', 'quul':'war', 'geh laro':'to rule'}               

if a == 1 :
    print(word_bank[str(input("enter phrase in Alien language:  "))])

elif a == 2 :
    print(list(word_bank.keys())[list(word_bank.values()).index(str(input("enter word in english: \n")))])

elif a == 3:
    # Adding a new key value pair
    word_bank[str(input("enter it in Alien language:"))] = str(input("enter word in English: "))
    print("Updated word_bank is: ", word_bank)

else: 
    print("\nERROR")
