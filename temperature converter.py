unit=input("Is this tempertaure in Celsius or Fahrenheit (C/f):")
temp=float(input("Enter the temperature:"))

if unit=="C":
    temp=round((9*temp)/5+32,1)
    print(f"The temperature in Fahrenheit is: {temp}degreeF")
elif unit=="F":
    temp=round((temp-32)*5/9,1)
    print(f"The temperature in Celsius is: {temp}degreeC")
else:
    print(f"{unit} is an invalid unit of measurement")
