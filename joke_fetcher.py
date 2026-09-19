import requests

def get_joke():

    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code==200:
        data = response.json()
        return data["setup"], data["punchline"]
        
            
    else:
        #return None for both setup and punchline if it fails
        return None, None
        


while True:
    user_choice = input("Do you want to continue?(yes/no): ").strip().lower() 
    if user_choice == "yes":
        setup, punchline = get_joke()
        if setup is None:
            print("Failed to fetch a joke")
        else:
            print(setup)
            print(punchline)    
        
    elif user_choice == "no":
        print("Goodbye")
        break
        
    else:
        print("Invalid Input.Please type yes or no.") 
         
