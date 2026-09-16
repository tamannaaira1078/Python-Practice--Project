import csv
while True:
    print("=====CONTACT MANAGER=====")
    print("1.Show Contact\n2.Add Contact\n3.Search Contact\n4.Exit")
    try:
        choice = int(input("Choose an Option(1/2/3/4): "))
        if choice==1:
            print("**You Choose Show Contacts**")
            with open("contacts.csv", "r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                print(f"{'Name':<20}{'Phone':<12}{'Email':<35}")
                print("-"*50)
                for line in csv_reader:
                    print(f"{line['name']:<20}{line['phone']:<12}{line['email']:<35}")
                print("-"*50)    
        elif choice==2:
            print("**You Choose Add Contact**") 
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            
            with open("contacts.csv", "a", newline="") as csv_file:
                field= ["name", "phone", "email"]
                csv_writer = csv.DictWriter(csv_file, fieldnames=field)
                
                csv_writer.writerow({"name":name, "phone":phone, "email":email})
                print("Contact Saved Succesfully")
                
        elif choice==3:
            print("**You Choose Search Contact**") 

            name = input("Enter the name you are searching for: ")
            
            with open("contacts.csv", "r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                found=False
                for line in csv_reader:
                    if name.lower()==line['name'].lower():
                        found=True
                        print(f"{'Name':<12}{line['name']}")
                        print(f"{'Phone':<12}{line['phone']}")
                        print(f"{'Email':<12}{line['email']}")
                if not found:
                        print('Contact Not Found')    


        elif choice==4:
            print("You Choose to Exit Contact\nGoodbye")
            break  
        else:
            print("Invalid Input.TryAgain.") 
                  
        
        
    except ValueError:
        print("Invalid Input.Please try again")    
    
