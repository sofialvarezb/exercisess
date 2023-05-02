Exercises=int(input("Enter the number of the exercise you want to run: "))

if Exercises == 1:
  #Calculate the area of a triangle
  Base=int(input("Enter the base of the triangle: "))
  height=int(input("Enter the height of the triangle: "))
  Area=Base*height/2
  print("The area of the triangle is: ",Area)
elif Exercises == 2:
  #Addition of two numbers
  first=int(input("Enter a number: "))
  second=int(input("Enter another number: "))
  addition=first+second
  print("The sum of the 2 numbers is: ",addition)
elif Exercises == 3:
  #The square of a number
  Number=int(input("Enter a number: "))
  Square=Number*Number
  print("The square of the number is: ",Square)
elif Exercises == 4:
  #Sum of 1234 y 532
  number1= 1234
  number2= 532
  Sum=number1+number2
  print("The sum of 1234 + 532 is: ",Sum)
elif Exercises == 5:
  #subtract between 1234 and 532
  number1=1234
  number2=532
  subtract=number1-number2
  print("the result of the subtraction: 1234 - 532 is: ",subtract)
elif Exercises == 6:
    #Multiplication between 1234 and 532
  number1=1234
  number2=532
  multiplication=number1*number2
  print("the result of the multiplication: 1234 x 532 is: ",multiplication)
elif Exercises == 7:
  #Division between 1234 y 532
  number1=1234
  number2=532
  Division=number1/number2
  print("The result of the division: 1234 / 532 is: ",Division)
elif Exercises == 8:
  #Module of 1234 between by 532
  Number1=1234
  Number2=532
  Module=Number1%Number2
  print("The Module of 1234 between by 532 is: ",Module)
elif Exercises == 9:
  #Conversion from euros to dollars
  Euro=float(input("Enter the euro: "))
  Conversion=Euro*1.10
  print("in dollars that equals: ",Conversion)
elif Exercises == 10:
  #Area of a rectangle
  Broad=float(input("Enter the width of the rectangle: "))
  Height=float(input("Enter the height of the rectangle: "))
  Area=Broad*Height
  print("The area of the rectangle is: ",Area)
elif Exercises == 11:
  #area and perimeter of a square
  Lado=int(input("Enter the side of the square: "))
  #Area
  Area=Lado*Lado
  print("The area of the square is: ",Area)
  #Perimeter
  Perimeter=Lado*4
  print("The perimeter of the square is: ",Perimeter)
elif Exercises == 12:
  #Area and volume of a cylinder
  Radio=int(input("Enter the radius: "))
  Height=int(input("Enter the height: "))
  #Area
  Area=2*3.1416*Radio*(Radio+Height)
  print("the area of the cylinder is: ",Area)
  #Volume
  Volume=3.1416*Radio*Radio*Height
  print("The volume of the cylinder is: ",Volume)
elif Exercises == 13:
  #Area and length of a circle
  Radio=int(input("Enter the radius of the circle: "))
  #Lenght
  Lenght=2*3.1415926536*Radio
  print("The length of the circle is: ",Lenght)
  #Area
  Area=3.1415926536*Radio*Radio
  print("The area of the circle is: ",Area)
elif Exercises == 14:
  #average of three numbers
  numero1=int(input("Enter the first number: "))
  numero2=int(input("Enter the second number: "))
  numero3=int(input("Enter the third number: "))
  Promedio=(numero1+numero2+numero3)/3
  print("The average of the three numbers is: ",Promedio)