with open("test.txt","r") as file:
    test=file.read()
    print(test)

A=open("Test2.txt","x")

with open("Test2.txt","w") as file:
    file.write("Hello, World!")

