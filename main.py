while True :
    first_number=int(input("Enter first number : "))
    second_number=int(input("Enter second number : "))
    operation=input("Enter the operation : ")

    if operation == "+" :
        answer=first_number+second_number

    elif operation == "x" or operation == "X " :
        answer=first_number*second_number

    elif operation == "-" :
        answer=first_number-second_number

    elif operation == "/" :
        answer=first_number/second_number

    else :
        print("Invalid input. Try again")
        
    print(answer)

    retryorquit=input("Press enter if you would like to retry and press q to quit. ")

    if retryorquit == "q" :
        print("Thank you for using this calculator. ")
        break