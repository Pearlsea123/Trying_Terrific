#==========================  Division Divine ======================
print("==========================  Division Divine ======================")
print("Wlcome to Diviion Divine")
print()

try:
    num1= int(input("Divident here: "))
    num2= int(input("Divisor here: "))
    result= num1/num2

except ValueError as Moonwatcher:
    print("Your problem is: ", Moonwatcher )
    print("You got the input wrong. You write a number - Sora")
    

except ZeroDivisionError as Sora:
    print("Your wrote the divisor wrong. Your error is: ", Sora)

except:
    print("you hae occured a error pleaase try again.")

else:
    print("the result is: ", result)
    print("I am Sora and my favourte Singer is Aurora, who sung Fly through Fire")

finally:
    print("hope you had a good time BYEEE- Sora")

print("BYYEE")