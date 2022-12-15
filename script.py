#You are completely free to change this variables to check your algorithm.
num1 = 6 
num2 = 28

#Function to check whether two numbers are friendly pairs or not.
def isFriendlyPair():
    sum1 = 0
    sum2 = 0


    if num1 < 1 or num2 < 1 or num1 == num2 or not isinstance(num1, int) or not isinstance(num2, int):
        return "Invalid"
    else:
        for divisor in range(1, num1 + 1):
            if num1 % divisor == 0:
                sum1 += divisor

        abundancy1 = sum1 / num1


        for divisor in range(1, num2 + 1):
            if num2 % divisor == 0:
                sum2 += divisor

        abundancy2 = sum2 / num2


        if abundancy1 == abundancy2:
            return True
        else:
            return False
            
print(isFriendlyPair())