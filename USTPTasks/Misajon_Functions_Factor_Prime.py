def start():
    print("\n\033[34mHello User!\033[37m what do you want to do today?")
    choice = str(input("Find the smallest factor\033[32m (1) \033[37m"
                       "| Find all the prime numbers between two numbers\033[33m (2) \033[37m"
                       "\npress \033[31m[x]\033[37m if you want to quit\n>> "))

    if choice == "1":
        find_smallest_factor()
    elif choice == "2":
        prime_num()
    elif choice.lower() == "x":
        print("\033[32m\nokay, see you later!")
    else:
        print("user, that input is\033[31m invalid! \033[37m")
        start()


def find_smallest_factor():
    n = int(input("\nEnter a number: "))

    if n < 2:
        print("Invalid input. Enter a number greater than 2.")
        find_smallest_factor()
        return

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"The smallest factor of {n} is: {i}")
            rerun()
            return

    print(f"{n} is a prime number.")
    rerun()


def prime_num():
    r1 = int(input("\nEnter the starting number: "))
    if r1 < 0:
        print("Please input a non negative number")
        prime_num()
        return

    r2 = int(input("Enter the end number: "))
    if r2 < r1:
        print("Ending number must not be smaller than the starting number")
        prime_num()
        return

    print(f"the prime numbers in between {r1} and {r2} are the following:")

    for num in range(r1, r2 + 1):
        if num > 1:
            for i in range(2, num):

                if num % i == 0:
                    break

            else:
                result = num
                print(result, end=" ")

    print()
    rerun()


def rerun():
    print("\nWould you like to do it again user?")
    choice = str(input("Y | N\n"))

    if choice.upper() == "Y":
        start()
    elif choice.upper() == "N":
        print("See you next time user!")
    else:
        print("User, that input is invalid!")
        rerun()


start()
