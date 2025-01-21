from datetime import datetime, timedelta


parse_date = lambda date_str: datetime.strptime(date_str, '%d-%m-%Y')

while True:
    try:
        
        start_date_input = input("Enter start date (DD-MM-YYYY): ")
        end_date_input = input("Enter end date (DD-MM-YYYY): ")

        
        start_date = parse_date(start_date_input)
        end_date = parse_date(end_date_input)

        
        if end_date < start_date:
            raise ValueError("End date cannot be earlier than start date.")

        break  
    except ValueError as ve:
        print(f"Input error: {ve}. Please try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please try again.")


current_date = start_date

while current_date <= end_date:
    try:
        if current_date.isoweekday() <= 5:  
            task = input(f"Enter the task for {current_date.strftime('%Y-%m-%d')}: ").strip()
            
            if not task:  
                raise ValueError("Task cannot be empty. Please provide a valid task.")

            print(f"{current_date.strftime('%Y-%m-%d')}: {task}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Move to the next day
    current_date += timedelta(days=1)


