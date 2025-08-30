try:
    # file = open('non_existent_file.txt', 'r') # Could cause FileNotFoundError
    # data = file.read()
    # result = 10 / 0
    my_list = [1, 2]
    print(my_list[5]) # Causes IndexError

except FileNotFoundError:
    print("The file wasn't found.")
except ZeroDivisionError:
    print("You divided by zero.")
except (IndexError, KeyError): # Catch multiple exceptions in one clause
    print("There was an index or key error.")
except Exception as e: # Catch ANY exception (Be careful!)
    print(f"An unexpected error occurred: {e}")