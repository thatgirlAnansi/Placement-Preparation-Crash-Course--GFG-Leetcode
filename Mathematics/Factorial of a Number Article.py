Factorial of a Number

What is the factorial of a number?
Factorial of a non-negative integer is the multiplication of all positive integers smaller than or equal to n. For example factorial of 6 is 6*5*4*3*2*1 which is 720. 
A factorial is represented by a number and a  ” ! ”  mark at the end. It is widely used in permutations and combinations to calculate the total possible outcomes. A French mathematician Christian Kramp firstly used the exclamation.
 


Let’s create a factorial program using recursive functions. Until the value is not equal to zero, the recursive function will call itself. Factorial can be calculated using the following recursive formula. 

n! = n * (n – 1)!
n == 1 if n = 0 or n = 1







// Java program to find factorial of given number
class Test {
	// method to find factorial of given number
	static int factorial(int n)
	{
		if (n == 0)
			return 1;

		return n * factorial(n - 1);
	}

	// Driver method
	public static void main(String[] args)
	{
		int num = 5;
		System.out.println("Factorial of " + num
						+ " is " + factorial(5));
	}
}
