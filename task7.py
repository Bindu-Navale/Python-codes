#program to read and print the contents of the file.
try:
    with open("Sample.txt","r") as file:
        print("Reading the content of the file")
        content=file.readlines()
        i=1
        for line in content:
            print(f"line{i} : {line}")
            i+=1
except FileNotFoundError:
    print("file doesn't exist")
