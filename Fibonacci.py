# Determine the n-th fibonacci number in a sequence using recursion
def fibonacci (num):
    if num <= 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

# Main
if __name__ == "__main__":
    for i in range (35):
        print fibonacci(i)
