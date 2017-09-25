while 1:
    string=input("Eneter your string: ")
    reverse=string[::-1]
    print("Reverse order is : ",reverse)

    if(string==reverse):
        print('yes it is an palindrome')

    else:
        print('No it is not a palindrome')

