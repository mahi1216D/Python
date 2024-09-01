def evenodd(numbers):
    
    even_num = []
    odd_num = []
    
    for num in numbers:
        if num % 2 == 0:
            even_num.append(num)
        else:
            odd_num.append(num)
    
    print("Even numbers:", even_num)
    print("Odd numbers:", odd_num)

def main():
   
    a = 10, 15, 20, 30

    evenodd(a)

if __name__ == "__main__":
    main()
