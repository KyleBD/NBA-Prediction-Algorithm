import plot_allseason_regression

def list_options():
    print("1: 'Historical' (Used to get ELO of Teams from past 25 seasons) \n")
    print("2: 'HistoricalReg' (Used to get the ELO of past 25 season teams, and Win percentage regressed to the mean) \n")
    return 

def parse_command(input):
    if input == "Historical":
        plot_allseason_regression.get_raw_data_historic()
    if input == "HistoricalReg":
        plot_allseason_regression.get_regressed_data_historic()
    else:
        print("Error: Invalid command")

    return

if __name__ == "__main__":
    list_options()

    command = input("Please enter your desired command: ")
    
    parse_command(command)
    print("\n")


