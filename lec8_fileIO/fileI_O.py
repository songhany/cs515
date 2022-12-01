# Read from a file
def read_file(filename):
    myfile = open(filename, "r")
    contents = myfile.read()
    myfile.close()
    return contents

def read_file_v2(filename):
    with open(filename, "r") as f:
        return f.read()
    
# read lines of a file and store them in a list
def read_file_v3(filename):
    with open(filename, "r") as f:
        return f.readlines()
    
# Iterate through lines of a file
def read_file_v4(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line.strip())
            
# Write into a file            
def write_file(string, filename):
    myfile = open(filename, "w")
    myfile.write(string)
    myfile.close()
    
# Append into a file
def append_file(string, filename):
    myfile = open(filename, "a")
    myfile.write(string)
    myfile.close()

def read_preferences(filename):
    dic = {}
    with open(filename, "r") as f:
        for line in f:
            [username, singers] = line.strip().split(":")
            singersList = singers.split(",")
            dic[username] = singersList
    return dic










    
    
