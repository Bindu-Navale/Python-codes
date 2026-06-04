try:
    with open("output.txt","w") as file1:
        line=input("Enter the text to write in the file : ")
        file1.write(line+"\n")
        print("Data succesfully writen in the file")
    with open("output.txt","a") as file2:
        line=input("Enter the text to apend to the file : ")
        file2.write(line)
        print("Data is successfully appended to the file : ")

    with open("output.txt","r") as file3:
        print("Final content of the file : ")
        content=file3.readlines()
        for line in content:
            print(line)
except FileNotFoundError:
    print("File does not exist")
    
