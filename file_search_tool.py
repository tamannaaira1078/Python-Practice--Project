import os
import re

def display_result(files):
    print("===== Search Results =====")
    count = 0
    
    for file in files:
        count+=1
        print(f"{count}.{file}")
    if not files:
        print("File not Found")  
    else:
        print(f"Total file found:{count}")     




def get_filename():
    file_name = input("Enter File name to Search: ").lower()
    matching_files=[]
    for file in os.listdir():
        if file_name==file.lower():
            matching_files.append(file)
    display_result(matching_files)       
       
    

def get_extension():
    file_ext = input("Enter File Extension: ").lower().strip()
    matching_files=[]
    for file in os.listdir():
        if file.lower().endswith(file_ext):
            matching_files.append(file)

    display_result(matching_files) 


def get_keyword():
    while True:
        keyword = input("Enter Search Keyword: ").lower()
        if keyword=="":
            print("Keywords Cannot be empty!")
            continue
        else:
            break


    matching_files=[]
    for file in os.listdir():
        if keyword in file.lower():
            matching_files.append(file)
    display_result(matching_files)

def get_regex():
    while True:
        pattern = input("Enter Regex Pattern: ")
        try:
            re.compile(pattern)
            break
        except re.error:
            print("Invalid Regex!")
            continue 
    matching_files = []
    for file in os.listdir():
        if re.search(pattern, file):
            matching_files.append(file)
            
    display_result(matching_files)
while True:
    print("===== FILE SEARCH TOOL =====")
    print("1.Search by filenames. \n2.Search by Extensions.\n3.Search using Keyword.\n4.Search Using Regex.\n5.Exit")
    try:
        choice = int(input("Choose an Option(1/2/3/4/5): "))
    except ValueError:
        print("Invalid Input")
        continue   
    if choice==1:
        print("You Choose Filename Option")
        get_filename()
    elif choice==2:
        print("You Choose Extension Option")
        get_extension()  
    elif choice==3:
        print("You Choose Keyword Option")
        get_keyword()
    elif choice==4:
        print("You Choose Regex Option")
        get_regex() 
    elif choice==5:
        print("You Choose Exit Option")
        break             