import function as fn

def main():
    while True:
        user_id = input("Welcome to Malaysian Tax Input Program! Please Enter your user ID: ").strip()
        
        if fn.is_user_registered(user_id):
            while True:
                ic_last_4_digits = input("Enter the last 4 digits of your IC number: ").strip()
                if fn.authenticate_user(user_id, ic_last_4_digits):
                    print(f"Welcome {user_id}, you have successfully logged in.")
                    
                    while True:
                        try:
                            annual_income = float(input("Enter your annual income: "))
                            tax_relief = float(input("Enter your total tax relief amount: "))
                            break
                        except ValueError:
                            print("Invalid input. Please enter numeric values for income and tax relief.")
                            
                    tax_payable = fn.calculate_tax(annual_income, tax_relief)
                    print(f"Your tax payable is: RM{tax_payable:.2f}")
                    fn.save_to_csv(user_id, annual_income, tax_relief, tax_payable, 'user_data.csv')
                    
                    # Ask the user if they want to continue or exit
                    continue_choice = input("Do you want to calculate tax again? (yes/no): ").strip().lower()
                    if continue_choice != 'yes':
                        print("Exiting the program. Goodbye!")
                        return
                else:
                    print("Authentication failed. Please check your user ID and password.")
                    retry = input("Do you want to try again? (yes/no): ").strip().lower()
                    if retry != 'yes':
                        print("Exiting the program. Goodbye!")
                        return
        else:
            print("User not registered. Please register.")
            ic_number = input("Enter your IC number in 12 digits: ").strip()
            ic_last_4_digits = input("Re-enter the last 4 digits of your IC number: ").strip()
            if ic_number[-4:] == ic_last_4_digits:
                fn.register_user(user_id, ic_number)
                print("You can now log in.")
            else:
                print("The last 4 digits of the IC number do not match. Registration failed.")
                continue

if __name__ == "__main__":
    main()
