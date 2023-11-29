def factorial():
    num = int(input('\nEnter number: '))
    def factor(num):
        if num == 1:return num
        else: return num * factor(num-1)
    print(f"The factorial of {num} is {factor(num)}")
    again = input("Again? y/n: ")
    if again.lower()== "y": factorial()
    elif again.lower()== "n":main()
    else: 
        print("Error input, try again")
        main()

def average():
    number = int(input("\nEnter a number: "))
    numList = []
    for x in range(1,number+1):
        num = int(input(f"Enter number: "))
        numList.append(num)
    print(f"Average is {round(sum(numList)/len(numList),2)}")
    again = input("Again? y/n: ")
    if again.lower()== "y": average()
    elif again.lower()== "n": main()
    else: 
        print("Error input, try again")
        main()

def main():
    print("\n[1] Factorial of a number\n[2] Average of numbers\n[3] to exit")
    choice = input("Enter your choice [1/2/3]: ")
    if choice == "1": factorial() 
    elif choice == "2": average()
    elif choice == "3": quit()

main()
