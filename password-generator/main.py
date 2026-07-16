from generator import generator_password

def main():
    while True:

        try:
            password_length = int(input("Enter password length: "))

            if password_length <= 0:
                print("Password length must be greater than 0.\n")
                continue

            break
        except ValueError:
            print("Please enter a valid number.\n")
            

        uppercase=input("Include uppercase? (y/n): ").lower() == "y"

        
        numbers=input("Include numbers? (y/n): ").lower() == "y"
        
        symbols=input("Include symbols? (y/n): ").lower() == "y"

        password= generator_password(password_length,uppercase,numbers,symbols)
        print("Your password is :" + password)

        break

if __name__== "__main__":
    main()

        


    