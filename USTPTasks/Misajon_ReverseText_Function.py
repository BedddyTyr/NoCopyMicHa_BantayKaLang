def reverseString(x):
    return x[::-1]


def strengOnli():
    userDef = input("Enter word: ")
    if not userDef.isalpha():
        print("Error Reported! Enter text only.\n")
        strengOnli()
    elif userDef.isalpha():
        print(reverseString(userDef))
    else:
        print("Error Reported! Enter text only.\n")
        strengOnli()


strengOnli()
