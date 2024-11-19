def fizz_buzz():
    # ✅↓ Write your code here ↓✅
    for x in range(0, 101):
        if (x % 3 == 0 and x % 5 == 0):
            print("FizzBuzz")
        elif (x % 3 == 0):
            print("Fizz")
        elif (x % 5 == 0):
            print("Buzz")
        else:
            print(x)
    

# ❌↓ DON'T CHANGE THE CODE BELOW ↓❌
fizz_buzz()
