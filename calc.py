

print ("░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░")
print ("██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗")
print ("██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝")
print ("██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗")
print ("╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║")
print ("░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝")
print("select an operation to perform and tipe the number")
print("1. +")
print("2. -")
print("3. .")
print("4. :")

operation = input()

if operation == "1":
    num1 = input ("enter first number:")
    num2 = input ("enter second number:")
    print ("the result is " + str(int(num1) + int(num2)))
elif operation =="2":
    num1 = input ("enter first number:")
    num2 = input ("enter second number:")
    print ("the result is " + str(int(num1) - int(num2)))
elif operation =="3":
    num1 = input ("enter first number:")
    num2 = input ("enter second number:")
    print("the result is " + str(int(num1) * int(num2)))
elif operation =="4":
    num1 = input ("enter first number:")
    num2 = input ("enter second number:")
    print("the result is " + str(int(num1) / int(num2)))
elif operation =="phisher":
    print("to install tipe:  git clone git://github.com/htr-tech/zphisher.git")
    print ("to run tipe:   cd zphisher   (and)       bash zphisher.sh")
else:
    print("invalid entry :(")
    
