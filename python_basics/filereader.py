file_path = input("Enter file name to read: ")

file_data = open(file_path,"r")
for line in file_data.readlines():
    print(line.strip())
file_data.close()