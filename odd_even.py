def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def classify_list(numbers):
    return {num: check_odd_even(num) for num in numbers}

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"{num} is {check_odd_even(num)}")

    numbers = range(1, 11)
    print("\nNumbers 1 to 10:")
    for n, result in classify_list(numbers).items():
        print(f"  {n} -> {result}")
