def multiplication(a):

    for i in range(1, 11): 
        x = a * i
        print(f"{a} * {i} = {x}")
        if x >= 40:
            break 

def main():
    try:
        a = int(input("Enter a number (a): "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return
    
    multiplication(a)

if __name__ == "__main__":
    main()

