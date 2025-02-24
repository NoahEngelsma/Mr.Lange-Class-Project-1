print("***********************************************")

valid_username = "PV2 Noah Engelsma"
valid_password = "BravoEchoCharlie1"

names_list = ["SSG John Ramirez", "PFC Jane Doe", "CPT Michael Smith", "PV2 Noah Engelsma", "SGT Emily Johnson", "SPC David Brown", "1LT Sarah Wilson", 
              "MSG Robert Davis", "CPL Jessica Martinez", "MAJ William Taylor", "SGT Emily Johnson", "SPC David Brown", "1LT Sarah Wilson", "MSG Robert Davis",
              "CPL Jessica Martinez", "MAJ William Taylor", "SGT Emily Johnson", "SPC David Brown", "1LT Sarah Wilson", "MSG Robert Davis", "CPL Jessica Martinez",]

def login():
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == valid_username and password == valid_password:
            print("Access Granted")
            print(names_list)
        else:
            print("You Failed Login")




