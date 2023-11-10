print("***********************")
print("*    file handling    *")
print("***********************")
import os
while True:
    a=int(input("enter the choice:"))

    def f():
        print("1.create the file")
        print("2.read the file")
        print("3.list the file")
        print("4.edit the file")
        print("5.delete the file")
        print("6.stop the program")
    match a:
        case 1:
            name=input("enter the file name:")
            name=name+".txt"
            file=open(name,"w")
            file.write("thamarai")
            print("--------------------")
            print("file created sucessfully")
            print("--------------------")
            f()
            print("************************")
        case 2:
            print("reading the file")
            name=input("enter the file name:")
            name=name+".txt"
            file=open(name,"r")
            print(file.read())
            print("-------------------------")
            f()
            print("************************")
        case 3:
            path="D:\selvibca"
            files=os.listdir(path)
            for file in files:
                print(file)   
            f()
            print("************************")
            

        case 4:
            print("edit the file")
            name=input("enter the file name:")
            name=name+".txt"
            file=open(name,"a")
            (file.write("thamaraiselvi"))
            print("-------------------------")
            f()
            print("**************************")
        case 5:
            print("delete the file")
            name=input("enter the file name:")
            name=name+".txt"
            os.remove(name)
            print("file",name,"\ndeleted successfully")
            f()
            print("****************************")
        case 6:
            print("***stop the program***")
            break
        

    
