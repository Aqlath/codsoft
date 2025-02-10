def show(lst):
    print("**list**")
    if not lst:
        print("list is empty...")
    else:
        for idx,val in enumerate(lst,1):
            print(f"{idx} : {val} ")

def add(lst):
    a=input("Enter the task to add:")
    lst.append(a)
    print(f"{a} is added sucessfully..")

def remove(lst):
    show(lst)
    try:
        n=int(input("Enter the task number to remove:"))
        if 1<=n<=len(lst):
            rem=lst.pop(n-1)
            print(f"{rem} is removed sucessfully..")
        else:
            print("There is no task...")
    except ValueError:
        print("please enter the valid number!")



def mark_complete(lst,complete):
    show(lst)
    try:
        n=int(input("Enter the task number to mark:"))
        if 1<=n<=len(lst):
            mark=lst.pop(n-1)
            complete.append(mark)
            print(f"The {mark} is marked as completed")
            print("Completed tasks are: ", ', '.join(complete) if complete else "there is no task as complte..")
        else:
            print("There is no task...")
    except ValueError:
        print("please enter the valid number!")
    

def main():
    lst=[]
    complete=[]
    print("****TO-DO LIST****")
    print("1.show the list \n2.Add the task  \n3.Remove the task  \n4.Mark as complete \n5.Exit")
    while True:
        task=input("Enter the operation to do:")
        if task=='1':
            show(lst)
        elif task=='2':
            add(lst)
        elif task=='3':
            remove(lst)
        elif task=='4':
            mark_complete(lst,complete)
        elif task=='5':
            print("Good bye..!!")
            break
        else:
            print("invalid input...")
        
    
main()



    





