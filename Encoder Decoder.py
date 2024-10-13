def encode(m,s):                                                    #ecoding function
    em=""
    for i in m:
        if i.isalpha():                                                    #checking for the letter or symbols
            if i.isupper():                                                    #checking for uppercase
                a = ord(i) + s
                if a > ord('Z'):                                                    #handling the for shifting after z
                    a = ord("A") + (a - ord("Z") - 1)
                em = em + chr(a)
            
            if i.islower():                                                    #checking for lower caser
                a = ord(i) + s
                if a > ord('z'):                                                    #handling values to before a
                    a = ord("a") + (a - ord("z") - 1)
                em = em + chr(a)

        else:
            em = em + i
    return em


def decode(m,s):                                                    #decoding function
     dm=""
     for i in m:
        if i.isalpha():                                                    #checking for the letter or symbols
            if i.isupper():                                                    #checking for uppercase
                a = ord(i) - s
                if a < ord('A'):                                                    #handling the for shifting after z
                    a = ord("Z") - (ord('A') - a - 1)
                dm = dm + chr(a)
            
            if i.islower():                                                    #checking for lower caser
                a = ord(i) - s
                if a < ord('a'):                                                    #handling values to before a
                    a = ord("z") - (ord('a') - a - 1)
                dm = dm + chr(a)
        else:
            dm = dm + i
     return dm


def shift():                                                    #shift funtion for correct input for shift
    while True:
        try:
            shift = int(input("Enter the number of letters to be shifted (0-25): ").strip())
            if 0 <= shift <= 25:                                                    #value of shift between 1 and 25
                return shift
            else:
                print("Please enter a shift value between 0 and 25.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for the shift.")

#main program
choice=1
while choice==1:                                                    #Menu driven program
    print("Encode a message(1)")
    print("Decode a message(2)")
    print("Exit the program(3)")
    a = int(input("enter the option:"))
    if a==1:
        m = (input("enter the message to be encoded:"))
        s= shift()
        print("generated code:",encode(m,s))
    elif a==2:
        m = (input("enter the message to be decoded:"))
        s= shift()
        print("generated code:",decode(m,s))
    elif a==3:
        print("Thank you for using the program!")
        choice=0
    else:
        print("invalid option")
