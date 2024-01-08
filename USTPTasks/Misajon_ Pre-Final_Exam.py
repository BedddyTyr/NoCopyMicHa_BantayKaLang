print("\nCS112: COMPUTER PROGRAMING 1 - PRE-FINAL EXAM")
print("Created by: KYNEHL SCOTT MISAJON")
print("\n ---------------------------")
print("\033[31m ENTER THE REQUESTED NUMBERS")
print("\033[32m    or enter '0' to quit \033[37m")
print(" ---------------------------")


def start():
    print("\n")
    rerunR1()


def primeNum(n):
    global result
    print(f"the prime numbers in between {R1} and {R2} are the following:")

    # To display the list
    for num in range(R1, R2 + 1):
        if num > 1:
            for i in range(2, num):

                # determines if it's a prime or not
                if num % i == 0:
                    break

            # Prints out the supposed prime number
            else:
                result = num
                print(result, end=" ")
    start()
    return


def rerunR1():
    global R1
    R1 = int(input("What number does the list start at?\n>> "))
    while R1 < 0:
        print("Enter a non-negative number.")
        rerunR1()
        break
    if R1 == 0:
        print("\033[31mprogram terminated")
    else:
        rerunR2()
    return


def rerunR2():
    global R2
    R2 = int(input("What number does the list end at?\n>> "))
    while R2 < R1:
        print("Enter a number greater than start number.")
        rerunR2()
        break
    primeNum(R2)
    return


start()
