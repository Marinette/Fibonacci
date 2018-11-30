// Implementing Fibonacci for C++
int fibonacci(int n);
#include <iostream>
#include <chrono>
using namespace std::chrono;

// This function iteratively computes and returns the n-th Fibonacci number
int fibonacci(int n) {
  int fibnum = 1, f1=0, f2=1;
  if (n<2)
    return 1;

  for (int i = 2; i <= n; i++) {
    fibnum = f1+f2;
    f1=f2;
    f2= fibnum;
  }

  return (fibnum);
}
// This function finds and prints the first n Fibonacci numbers
void fibonacci_test(int n) {
  for (int i = 0; i <= n; i++)
    fibonacci(i);

}
int main () {
  // Using C++'s chrono libary to find the time taken to find the first
  //35 Fibonacci numbers
  high_resolution_clock::time_point t1 = high_resolution_clock::now();
  fibonacci_test(36);
  high_resolution_clock::time_point t2 = high_resolution_clock::now();

  auto duration = duration_cast<nanoseconds>( t2 - t1 ).count();
  std::cout << "C++: total time taken for fibonacci (iterative) is " << duration << " nanoseconds" << std::endl;

  return 0;
}
