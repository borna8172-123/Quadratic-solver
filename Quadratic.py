import math





def solvequadratic():

    PolynomialValues = list(map(float,input("enter the values, A, B and C for the quadratic").split()))
    A = PolynomialValues[0]
    B = PolynomialValues[1]
    C = PolynomialValues[2]


    try:

      Answer1 = (-B + math.sqrt(B * B - 4 * A * C))/2 * A
      Answer2 = (B - math.sqrt(B * B - 4 * A * C))/2 * A

    except ValueError:
        print("This Quadratic has complex roots")
    else:

       return Answer1,Answer2
       

def mainenu():

   print("1: solve Quadratic"
   print("2: exit")

   choice = input("choose an option")

   if choice == "1":
      print(solvequadratic())
   if choice == "2":
      print("okay goodbye")



mainenu()
