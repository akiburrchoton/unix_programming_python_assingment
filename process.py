import sys
import re
from os import path


def __main__():
    option, file_path, memory_threshold = argv_available()
    rfile = read_log_file(file_path)

    if option == '-a': option_a(rfile)
    elif option == '-m': option_m(rfile)
    elif option == '-t': option_t(rfile)
    elif option == '-s': option_s(rfile, memory_threshold)
    elif option == '-v': option_v()

def argv_available():
    mem = 0
    option = sys.argv[1]
    log_file = sys.argv[-1]
    length = {'-a': 3, '-m': 3, '-t': 3, '-s': 4, '-v': 3}
    
    if option not in length.keys():
        print("Wrong Option", option)
        sys.exit(1)

    for key, value in length.items():
        if option == key and len(sys.argv)!=value:
            if key == '-s':
                if sys.argv[-1].isnumeric():
                    print("Missing the filename argument")
                else:
                    print("Missing  the  memory  threshold argument")
                sys.exit(1)
            else:
                print("Missing the filename argument")
                sys.exit(1)
        
        if option == key and option == '-s':
            mem = sys.argv[2]
            return option, log_file, mem
            
    #Check here if the file exists in the directory
    if not (path.exists(log_file)):
        print("The file does not exist")
        sys.exit(1)

    return option, log_file, mem


def read_log_file(log_file):

    #Opening the file
    f = open(log_file , "r")

    #Check if the file is readable
    if not f.readable():
        print("Sorry, the file cannot be read!")
        sys.exit(1)
    
    return f

#Function for option '-a'
def option_a(f):
    lines = [line.split () for line in f]
    
    # Check if the file is empty or not
    if len(lines) == 1:
        print("No processes found")
    else:
        lines.sort (key=lambda s: s[-1])
        for line in lines:
            print(*line)
        

#Function for option '-m'
def option_m(f):
    total_memory = 0

    lines = [line.split () for line in f]

    if len(lines) == 1:
        print("No processes found")
    else:
        for line in lines:
            for i in range(len(line)):
                if i == 1:
                    total_memory += int(line[i])

        print(f"Total memory size: {total_memory} KB")

#Function for option '-s'
def option_t(f):
    total_cpu_time = 0

    lines = [line.split () for line in f]

    if len(lines) == 1:
        print("No processes found")
    else:
        for line in lines:
            for i in range(len(line)):
                if i == 2:
                    total_cpu_time += int(line[i])

        print(f"Total memory size: {total_cpu_time} seconds")

#Function for option '-t'
def option_s(f, memory_threshold):
    lines = [line.split () for line in f]

    if len(lines) == 1:
        print("No processes found with the specified memory size")
        sys.exit(1)
    else:
        max = 0
        new_list = []

        for line in lines:
            for i in range(len(line)):
                if i == 1 and int(line[i])>=max:
                    max = int(line[i])
                    
                    
        if max<int(memory_threshold):
            print("No processes found with the specified memory size")
            sys.exit(1)
        else:  
            for line in lines:
                for i in range(len(line)):     
                    if i == 1 and int(line[i])>=int(memory_threshold):
                        print(*line)
                
#Function for option '-v'
def option_v():
    print("Name: Akibur Rahman")
    print("Surname: Choton")
    print("Assignment Completion Date: 10/10/2022")


__main__()