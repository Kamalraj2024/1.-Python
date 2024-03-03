class multiFunction():
    def oddEven():
        num = int(input("Enter a value : "))
        if ((num%2)==0):
            print("Even")
            message = "Even"
        else:
            print("odd")
            message = "Odd"
        return message
    
    def AgeCategory():
        age = int(input("Enter a Age : "))
        if (age<18):
            print("Children")
            cate = "Chidren"
        elif(age<35):
            print("Adult")
            cate = "Adult"
        elif(age<59):
            print("Citizen")
            cate = "Citizen"
        elif(age>59):
            print("Senior Citizen")
            cate = "Senior Citizen"
        return cate
    
    def BMI():
        bmi = int(input("Enter the BMI Index : "))
        if(bmi<=18.5):
            print("Underweight")
        elif(bmi<=24.9):
            print("Normal range")
        elif(bmi<=29.9):
            print("Overweight")
        else:
            print("Obese")
