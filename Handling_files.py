try:
#creating a file in python
    with open ("my_file.txt","w") as file:
#Writing some word lines in th efiles
        file.write("Hello!, am itumbi a PLP Student 2024 cohort\n")
        file.write("12345\n")
        file.write("I like typing some random writings like 7&$123 , it sounds funny to me\n")
    print("f'my_file.txt' created and written successfully.")

#Reading the files
    with open ("my_file.txt","r") as file:
#reading and printing the cntent of the file
        content=file.read()
    print("Contents of 'my_file.txt':")
    print(content)

#Appending additional lines to the file
    with open("my_file.txt","a"):
    #Appending three more lines
       file.write("Appending line4\n")
       file.write("Appending line5\n")
       file.write("Appending line6\n")
    print("Data appended to 'my_file.txt' successfully.")

except FileNotFoundError:
    Print("File 'my_file.txt' not found.")
except PermissionError:
    print("Permission denied to access the file.")
except Exception as e:
    print("An error occured:",e)

    # Reading the files again
file = open("my_file.txt", "r")
content = file.read()
print("Contents of 'my_file.txt':")
print(content)
file.close()  # Don't forget to close the file after reading its contents
