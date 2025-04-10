# FIBONACCI GENERATOR

# The Fibonacci series is a sequence where each number is
# the sum of the two preceding numbers, defined by a
# mathematical recurrence relationship.


num = int(input("enter the first n number :"))#Asking the user how many terms of the sequence they want

#define function
def fib_generator(n):
    prev_num = 0
    curr_num = 1

    fib = "0, 1"

    # Check if the number of terms is valid
    if(n == 0):
        return 
    elif(n == 1):
        print("Fibonacci sequence up to 1 term:")
        return fib[0]
    elif(n < 0):
        return "Negative numbers are not allowed"
    
    for i in range(2, n):
 
        #update values
        prevprev_num = prev_num
        prev_num = curr_num
        curr_num = prevprev_num + prev_num

        fib = fib+", "+str(curr_num)
    print(f"Fibonacci sequence up to {n} terms:")
    return fib                

print(fib_generator(num))          