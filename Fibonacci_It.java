// Function: Iteratively find the n-th Fibonacci Number
public class Fibonacci_It {
  public static void main(String[] args){
    long startTime = System.nanoTime();
    for (int i =1; i <= 36; i++) {
      fibonacci(i);
    }
    long stopTime = System.nanoTime();
    long elapsedTime = stopTime - startTime;
    System.out.println("Java: Time taken for Fibonacci (Iterative) is: " + elapsedTime + " nanoseconds");
  }

  public static int fibonacci(int n) {
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
}
