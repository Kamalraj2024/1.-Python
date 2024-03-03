class MultipleFunctions():
    def subfields():
        print("Sub-fields in AI are:")
        list1 = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for i in range(0,len(list1)):
            print(list1[i])
        return

    def oddEven():
        n = int(input("Enter a Number : "))
        if ((n%2)==0):
            print(n," is a Even Number")
        else:
            print(n,"is a Odd Number")
        return
    
    def Elegible():
        sex = input("Enter your Gender : ")
        age = int(input("Enter your Age : "))
        if (sex == 'male'):
            if(age >= 21):
                print("ELIGILE")
            else:
                print("NOT ELIGILE")
        else:
            if(age >= 18):
                print("ELIGILE")
            else:
                print("NOT ELIGILE")
    return
                
    def percentage():
        print("Enter five sujects marks")
        s1 = int(input("Subject1: "))
        s2 = int(input("Subject2: "))
        s3 = int(input("Subject3: "))
        s4 = int(input("Subject4: "))
        s5 = int(input("Subject5: "))
        total = s1+s2+s3+s4+s5
        percent = ((total / 500) * 100)
        print("Total : ",total)
        print("Percentage : ",percent)
    return

    def triangle():
        Height = int(input("Enter the Height:"))
        Breadth = int(input("Enter the Breadth:"))
        AT = (Height*Breadth)/2
        print("Area of Tringle: ",AT)
        Height1 = int(input("Enter the Height1:"))
        Height2 = int(input("Enter the Height2:"))
        Breadth1 = int(input("Enter the Breadth:"))
        PT =  Height1+Height2+Breadth1
        print("Perimeter of Tringle: ",PT)
    return
