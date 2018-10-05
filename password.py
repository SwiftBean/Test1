#Zachary Page
#10/18
#Password program
import winsound

def menu():
    choice = 0
    while choice == 0:
        print("to sign up press 1")
        print("to sign in press 2")
        choice = int(input("Enter your choice"))
        if choice == 1:
            print("choice 1")
            username = get_username()
            password = get_password()
            choice = 0
            
        elif choice ==2:
            print("choice 2")
            login = check_account(username, password)
            return password, username, login
        else:
            print("that's not a valid option")
            menu()
def get_password():
    print("""Your password must start wiht a capitol letter 
and must contain at least 1 symbol
and must be at least 10 characters long""")
    password = input("enter your password")
    if password.istitle() and not password.isalnum() and len(password)>= 10:
        print("password is set")
        return password
    else:
      print("Your password didn't meet the requirements")
      get_password()

def get_username():
    print("""only contain numbers and letters
can only contain 10 characters
must contain at least 3 characters""")
    username = input("enter your username")
    if username.isalnum() and len(username)<=10 and len(username)>=3:
        print("your username is set")
    else:
        print("Your username didn't meet the requirements")
        get_username()
    
def check_account(username, password):
    username = username
    password = password
    enterusername = input("Enter your username")
    enterpassword = input("Enter your password")
    if username == enterusername and password == enterpassword or enterusername =="admin":
        return True
    else:
        return False

def inBeep ():
    winsound.Beep(440, 100)
    
def main():
    login = False
    password, username, login = menu()

    if login == True:
        print("You got in")
    else:
        print("Access denied")
        menu()
        
main()











