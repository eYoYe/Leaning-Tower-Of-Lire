import math
import turtle

def main():
    print("This Program calculates the overhang length of the Leaning Tower of Lire." +
          "\nWhere every brick is represented as 1 unit."+
          "\nEach Brick it stacked on top of each other on a ledge and after each brick stacked"+
          "\nThe new brick is placed one half the way from the previous brick."
          "\nWhich will be demonstrated with a Turtle.")
          
    print("For Example, 50 brick will have a length of " + str(brick_laying(50))+ " units")
    count = input("How many Bricks do you wanna lay? ")
    print("The length of your Leaning Tower of Lire is "+ str(brick_laying(count)))


def brick_calulcation(n):
    n = int(n)
    n = 1/(2*n)
    return n
    

   


def brick_laying(count):
    count = int(count)
    calculation = []
    for count in range(count, 0, -1):
        n = count
        variable = brick_calulcation(n)
        calculation.append(variable)
    return sum(calculation)



main()
        
