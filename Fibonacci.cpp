// Implementing Fibonacci for C++
int fibonacci(int n);
#include <iostream>
#include <chrono>
using namespace std::chrono;

// This function recursively computes and returns the n-th Fibonacci number
int fibonacci(int n) {
  if (n<=1)
    return 1;
  else
    return (fibonacci(n-1) + fibonacci(n-2));
}
// This function finds and prints the first n Fibonacci numbers
void fibonacci_test(int n) {
  for (int i = 0; i <= n; i++)
    std::cout << fibonacci(i) << std::endl;

}
int main () {
  // Using C++'s chrono libary to find the time taken to find the first
  //35 Fibonacci numbers
  high_resolution_clock::time_point t1 = high_resolution_clock::now();
  fibonacci_test(35);
  high_resolution_clock::time_point t2 = high_resolution_clock::now();

  auto duration = duration_cast<milliseconds>( t2 - t1 ).count();
  std::cout << "C++: total time taken for fibonacci is " << duration << " milliseconds" << std::endl;

  return 0;
}
