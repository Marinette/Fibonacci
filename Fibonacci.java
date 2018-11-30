// Function: Recursively find the n-th Fibonacci Number
public class Fibonacci {
  public static void main(String[] args){
    long startTime = System.currentTimeMillis();
    for (int i =0; i <= 35; i++) {
      System.out.println(fibonacci(i));
    }
    long stopTime = System.currentTimeMillis();
    long elapsedTime = stopTime - startTime;
    System.out.println("Time taken for Fibonacci (Java)is: " + elapsedTime + " milliseconds");
  }

  public static int fibonacci(int n) {
    if (n<=1)
      return 1;

    return (fibonacci(n-1) + fibonacci (n-2));
  }
}
