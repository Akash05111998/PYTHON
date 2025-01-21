from datetime import datetime

def calculate_age():
    """
    Calculate the age
    """
    try:
        
        birth_date_input = input("Enter your birth date (YYYY-MM-DD): ")
        
        birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")

        today = datetime.today()

        
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        
        if birth_date > today:
            raise ValueError("The birth date cannot be in the future.")
        else:
            print(f"You are {age} years old.")

    except ValueError as ve:   
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
if __name__ == "__main__":
    calculate_age()
