#Practicing Multi-line Strings.
def testMLStrings():
    print("Line one\nLine two\nLine three")
    multiLineSentence = """
    Line one
    Line two\n
    Line three
    """
    print (f"{multiLineSentence}")
    print (multiLineSentence)

def sliceStr():
    text = "Life is expensive"
    if "free" not in text:
        print("Life is not free!")
    else:
        print("Life is free")

    txt2 = "Hello, World!"
    print(txt2[2:5])

'''
This function reads a string and prints
out all the characteristics of that string.
'''
def isStr():
    string = input("Enter some random things: ")
    print(f"\"{string}\" is:")
    if string.isalnum():
        print("\tAlphanumeric")
    else:
        print("\tNot alphanumeric", end="")
        for aNChar in string:
            if not aNChar.isalnum():
                print(f"({aNChar})")
                break
    if string.isalpha():
        print("\tAlphabetical")
    else:
        print("\tNot alphabetical", end="")
        for aChar in string:
            if not aChar.isalpha():
                print(f"({aChar})")
                break
    if string.isdecimal():
        print("\tA decimal")
    else:
        print("\tNot a decimal", end="")
        for char in string:
            if not char.isdecimal():
                print(f"({char})")
                break
    if string.isdigit():
        print("\tDigits")
    else:
        print("\tNot all digits", end="")
        for myChar in string:
            if not myChar.isdigit():
                print(f"({myChar})")
                break
    if string.isidentifier():
        print("\tAn identifier")
    else:
        print("\tNot an identifier", end="")
        for iChar in string:
            if not iChar.isidentifier():
                print(f"({iChar})")
                break
    if string.isprintable():
        print("\tPrintable")
    else:
        print("\tNot printable", end="")
        for pChar in string:
            if not pChar.isprintable():
                print(f"({pChar})")
                break
    if string.istitle():
        print("\tQualified to be a title")
    else:
        print("\tNot qualified to be a title", end="")
        for tchar in string:
            if not tchar.istitle():
                print(f"({tchar})")
                break
    if string.islower():
        print("\tLowercase")
    elif string.isupper():
        print("\tUppercase")
    else:
        print("\tNot lowercase or uppercase", end="")
        for lchar in string:
                    if not lchar.islower():
                        print(f"({lchar})", end="")
                    if not lchar.isupper():
                        print(f"({lchar})")
                        break
    print(f"Capitalized version: {string.capitalize()}") 
    print(f"Casefold version: {string.casefold()}") 
    if "s" in string:
        x = int(string.find("s"))
        print(f"You have an \"s\", my favorite letter, {x} spaces from the beginning!")

if __name__ == "__main__":
#    testMLStrings()
#    sliceStr()
    isStr()
