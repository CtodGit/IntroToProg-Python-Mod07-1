# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demonstrating use of Exception Handling and Pickling
# ChangeLog (Who,When,What):
# SNunn,5.28.2020,Created code to complete assignment 7
# ---------------------------------------------------------------------------- #

# Import modules
import sys
import pickle

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
STR_FILE_NAME = "C:\\_PythonClass\\Assignment07\\ToDoFile.dat"  # Binary data file
strChoice = ""  # Captures the user option selection
strStatus = ""  # Captures the status of an processing functions


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """
    @staticmethod
    def read_data_from_fileb(file_name):
        """ Reads data from a binary file into a list of dictionary rows
        :param file_name: (string) with name of file:
        :return: (list) of dictionary rows
        """
        errMsg = ''
        try:
            file = open(file_name, "rb")
        except FileNotFoundError:
            input("*** " + file_name + " does not exist.  Please create it and rerun this program.  Press Enter key to exit.")
            sys.exit()
        except:
            input("*** Something is wrong with " + file_name + ". Please investigate and rerun this program.  Press Enter key to exit.")
            sys.exit()
        try:
            fileData = [pickle.load(file)]
        except EOFError:
            errMsg = []
        except:
            input("*** Something is wrong with " + file_name + ". Please investigate and rerun this program.  Press Enter key to exit.")
            sys.exit()
        file.close()
        if errMsg == []:
            return errMsg
        else:
            return fileData
    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        list_of_rows.append({"Task": task, "Priority": priority})
        return list_of_rows, 'Success'
    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        for dict in list_of_rows:
            if dict["Task"].lower() == task.lower():
                list_of_rows.remove(dict)
        return list_of_rows, 'Success'
    @staticmethod
    def write_data_to_fileb(file_name, list_of_rows):
        file = open(file_name, "wb")
        pickle.dump(unPklList, file)
        file.close()
        return list_of_rows, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        print(list_of_rows)
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
unPklList = Processor.read_data_from_fileb(STR_FILE_NAME)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(unPklList)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        # TODO: Add Code Here # Done
        task = input("What is the task name you would like to add? ")
        priority = input("What is the task priority you would like to add? ")
        Processor.add_data_to_list(task, priority, unPklList)

        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        # TODO: Add Code Here # Done
        task = input("What is the task name you would like to remove? ")
        Processor.remove_data_from_list(task, unPklList)

        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            # TODO: Add Code Here! # Done
            Processor.write_data_to_fileb(STR_FILE_NAME, unPklList)

            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            # TODO: Add Code Here! # Done
            unPklList = Processor.read_data_from_fileb(STR_FILE_NAME)  # read file data
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit
