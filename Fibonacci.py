# Fibonacci in Python
import timeit
# Determine the n-th fibonacci number in a sequence using recursion
def fibonacci (num):
    if num <= 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
# Find the 35 first Fibonacci numbers
def fibonacci_test():
    for i in range (35):
        print fibonacci(i)
# Main
if __name__ == "__main__":
    # Using Python's timeit libary to find the time taken to find
    # the 35 first Fibonacci numbers
    # Numbers = 10 means I ran the test 10 times
    timetaken= timeit.timeit("for x in range(35): fibonacci(x)", "from __main__ import fibonacci",number=10)
    print timetaken
    # timetaken is the time (in microseconds) to run 10 iterations of the test
    # I want to find the average time per test in milliseconds so I divide
    # timetaken/10 * 1000 = timetaken * 100
    print "Average time taken to run fibonacci is: ", timetaken*100, "milliseconds"
