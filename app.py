from donations_pkg.homepage import show_homepage
from donations_pkg.user import (initate_db,
                                get_db,
                                login_user,
                                donate,
                                register,
                                show_donations)

# initate_db()
# print(show_homepage())

# [todo] initiate the database file
    # [todo] if file does not exist, create file with headers uname,password,total
    # [todo] add admin account to database through append
# [todo] set session to active = True
# [todo] set user_logged_in = False
# [todo] while active:

#           take choice of user
#           if choice == 1
#               - user auth funct
#               - if user == valid
                #   + user_loged_in = True
#                   + login user function
#               - else:
#                  - user isn't valid
#            elif choice == 2
#               - register_user function
#            elif choice == exit - then exit app
#            elif choice in [3,4]
#               + check if user is logged in, if not prompt user for login
                #+ else
                    # if 3
                        # + donate function
                    # elif 4 4
                        # + show donations functios
#           else:
#               print("not a valid choice")

def main():
    initate_db()
    user_db = get_db()
    active_session = True
    user_logged_in = False

    while active_session:
        show_homepage()
        print(user_db)
        try:
            choice = int(input("\nSelect an option: "))
            if choice == 5:
                active_session = False
                print('GoodBye!')
            elif choice == 1:
                username = input("\nProvide username: ")
                password = input("Provide password: ")
                user = login_user(user_db,username,password)
                user_logged_in = True
            elif choice == 2:

                register(user_db)
            elif choice == 3:
                if user_logged_in:
                    donate(user_db,user['username'])
                else:
                    print("\nPlease Login")
            elif choice == 4:
                if user_logged_in:

                    show_donations(user)
                else:
                    print("\nPlease login")
            else:
                print("Not a valid choice - try again")
        except ValueError:
            print(" Invalid Choice Try again")

main()
