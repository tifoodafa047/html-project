def add(a: int, b: int) -> int:
    return a + b

def main():
    # change value of x
    x = 15
    
    y = 10
    result = add(x, y)
    print(f"The sum of {x} and {y} is {result}")

if __name__ == "__main__":
    main()