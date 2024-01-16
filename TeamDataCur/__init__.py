import plot_curseason_regression

def list_options():
    print("The Supported Commands are \n")
    print("1: 'Current' (Used to get ELO of Teams This season) \n")
    print("2: 'CurrentReg' (Used to get the ELO of current teams, and Win percentage regressed to the mean) \n")
    return 

def parse_command(input):
    if input == "Current":
        plot_curseason_regression.get_raw_data_current()
    if input == "CurrentReg":
        plot_curseason_regression.get_regressed_data_current()
    else:
        print("Error: Invalid command")

    return

if __name__ == "__main__":
    list_options()

    command = input("Please enter your desired command: ")
    
    parse_command(command)
    print("\n")


