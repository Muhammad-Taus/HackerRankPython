
if __name__ == '__main__':
    n = int(input().strip())

    # Check the conditions and print the result
    if n % 2 == 1 or (n % 2 == 0 and 6 <= n <= 20):
        print("Weird")
    elif n % 2 == 0 and (2 <= n <= 5 or n > 20):
        print("Not Weird")
    else:
        print("Invalid input")

