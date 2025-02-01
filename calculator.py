#THIS IS THE PYTHON CODE FOR CALCULATOR

#functions of calculator
def add(n):
    result=n[0]
    for i in n[1:]:
        result+=i
    return result

def sub(n):
    result=n[0]
    for i in n[1:]:
        result-=i
    return result

def multi(n):
    result=n[0]
    for i in n[1:]:
        result*=i
    return result

def div(n):
    result=n[0]
    for i in n[1:]:
        if i==0:
            return "zero division error (you cannot divide by zero)"
        else:
            result/=i
    return result

def modulo(n):
    result=n[0]
    for i in n[1:]:
        if i==0:
            return "zero division error (you cannot divide by zero)"
        else:
            result%=i
    return result

def main():
    print("hey..Welcome to calculator..! let's do some calculation..!!")
    while True:
        print("choose the operation to be performed.. \n1.ADDITION \n2.SUBTRACTION \n3.MULTIPLICATION \n4.DIVISION \n5.MODULUS \nNOTE:choose the number")
        choice=input("Enter the choice[1,2,3,4,5] from this:")

        if choice in ['1','2','3','4','5']:
            try:
                a=int(input("Enter the number of elements to perform operation:"))
                n=[]
                for i in range(1,a+1):
                    s=int(input(f"Enter the element (or) value {i}:"))
                    n.append(s)
            
                if choice=='1':
                    print(f"RESULT : {'+'.join(map(str,n))} = {add(n)}")
                    
            
                elif choice=='2':
                    print(f"RESULT : {'-'.join(map(str,n))} = {sub(n)}")
                    
            
                elif choice=="3":
                    print(f"RESULT : {'*'.join(map(str,n))} = {multi(n)}")
                    
            
                elif choice=='4':
                    print(f"RESULT : {'/'.join(map(str,n))} = {div(n)}")
                    
            
                elif choice=='5':
                    print(f"RESULT : {'%'.join(map(str,n))} = {modulo(n)}")
                    
            except ValueError:
                print("OOPS!!,PLASE MAKE SURE TO ENTER VALID NUMBER...")    
        else:
            print("INVALID SELECTION OF OPERATION..YOU SHOULD SELECT FROM (1/2/3/4/5)")   
        
        print("do you want to calculate more?")
        user=input("Enter the option (yes/no):").lower()
        if user=="no":
            print("THANKS FOR COMING...SEE YOU AGAIN..!!")
            break
        else:
            continue
            

    

            
main()

    





