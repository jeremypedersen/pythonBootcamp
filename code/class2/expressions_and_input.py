# Hi! I am a comment. I don't do anything, I just help
# you remember what your program does! You can write anything
# you want in a comment.

print("Hi! I am albert. I can help you add numbers. Please give me two numbers")

firstNumber = input("Enter the first number: ")
secondNumber = input("Enter the second number: ")

# Ok, let's make sure that we put in numbers, and
# not something else
try:
    firstNumber = float(firstNumber)
    secondNumber = float(secondNumber)
except:
    print("Ooops! One of those wasn't a number...")
    exit(-1)

answer = firstNumber + secondNumber

# Let's make the answer into something we can show 
# on the computer screen, that looks nice
output = "Ok, {} + {} = {}".format(firstNumber, secondNumber, answer)
print (output)