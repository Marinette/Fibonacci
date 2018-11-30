# Fibonacci in Python
import timeit
# Determine the n-th fibonacci number in a sequence iteratively
def fibonacci (num):
    if num < 2:
        return 1
    fibnum = 1
    f1 = 0
    f2 = 1

    for i in range(0,num):
        fibnum = f1 + f2
        f1=f2
        f2 = fibnum
    return fibnum

# Find the 35 first Fibonacci numbers
def fibonacci_test():
    for i in range (36):
        print (fibonacci(i))
# Main
if __name__ == "__main__":
    # Using Python's timeit libary to find the time taken to find
    # the 35 first Fibonacci numbers
    # Numbers = 10 means I ran the test 10 times
    timetaken= timeit.timeit("for x in range(36): fibonacci(x)", "from __main__ import fibonacci",number=10)
    print (timetaken)
    # timetaken is the time (in microseconds) to run 10 iterations of the test
    # I want to find the average time per test in nanoseconds so I divide
    # timetaken/10 * 1000000000 = timetaken * 100000000
    print ("Average time taken to run fibonacci is: ", timetaken*100000000, "nanoseconds")
