"""
This module is to test the Elevator class.
Where user can provide the input in real time and interact with the system.
"""
import time
from elevator_system.elevator import Elevator


def validate_elevator_requests(elevator_requests, max_floor):
    """
    This method allows to validate each floor request entered by user.
    User can enter any values but the system
    determines and keeps only those entries which is integer and between 0 to max floor.
    :param elevator_requests: elevator requests entered by user.
    :param max_floor: the maximum floor of the building.
    :return: valid and invalid entries
    """
    print(elevator_requests)
    valid_enteris = set()
    invalid_enteries = set()
    elevator_requests = map(lambda x: x.strip(), elevator_requests)
    for i in elevator_requests:
        try:
            if int(i) and (0 <= int(i) <= max_floor):
                valid_enteris.add(int(i))
            else:
                raise ValueError
        except ValueError as _:
            invalid_enteries.add(i)
    return valid_enteris, invalid_enteries


def get_elevator_service_request(max_floor):
    """
    This method let's user to enter requests separated by comma(,).
    :param max_floor: Valid and invalid floor requests.
    :return:
    """
    elevator_requests = input(f"Enter Number of floors separated by space. "
                              f"\nOnly Positive numbers "
                              f"between 0 to {max_floor} accepted. "
                              f"Rest entries will be discarded.\n"
                              f"Enter values separated by comma(,) :").split(",")
    valid_enteris, invalid_enteries = validate_elevator_requests(set(elevator_requests), max_floor)
    return valid_enteris, invalid_enteries


def get_user_input(message):
    """
    This method let's user to get the input and allow user to provide the custom input message.
    :param message: Custom input message.
    :return: user's entered value.
    """
    while True:
        try:
            user_input = int(input(message))
            if user_input < 0:
                raise ValueError
            break
        except ValueError as _:
            print("Invalid Entry. Please enter positive value grater than 0")
            continue
    return user_input


def initialize_system():
    """
    This method let's user to initialize the system.
    :return:
    """
    print("Welcome to Elevator Simulation")
    print("Lets Set up the required details. First Input Maximum Floor in Building.")
    max_floor = 0
    while True:
        if max_floor > 0:
            break
        else:
            max_floor = get_user_input(
                "Please enter number of floors for the building for which elevator is required: ")
    return max_floor


def print_and_get_user_choice(elevator, max_floor):
    """
    This method let's user to enter one of the 4 possibilities.
    It can run elevator simulation, set current floor,
    visualize monitor and consume the requests.
    :param elevator:
    :param max_floor:
    :return:
    """
    while True:
        # This loop will continue till user enters value between 1 to 4
        print(f"Enter Your Choice.\n1.Enter a few elevator requests "
              f"and run the elevator simulation"
              f".\n2.Set Current Elevator Floor. "
              f"For the first time run,"
              f"elevator is at floor 0."
              f"\n3.Visualize Elevator Monitor."
              f"\n4. Consume elevator requests. "
              f"\n10 End Program")
        user_input = get_user_input("")
        if user_input == 1:
            valid_enteris, invalid_enteries = get_elevator_service_request(max_floor)
            elevator.add_request(valid_enteris)
            print(f"Theese entries {invalid_enteries} are not valid and hence discarded")
            status = elevator.start_elevator()
            if status:
                print("The Elevator requests have been complete")
        elif user_input == 2:
            get_floor = get_user_input("Enter the Floor where you wanna take elevator to: ")
            if 0 <= get_floor <= max_floor:
                elevator.issue_call(get_floor)
            else:
                print(f"Invalid Floor. Maximum Floor value allowed is {max_floor}")
                time.sleep(1)
        elif user_input == 3:
            elevator.visualize_monitor()
        elif user_input == 4:
            elevator.consume_elevator_requests()
        else:
            elevator.stop_elevator()
            print("Prgram is completing")
            break


def main():
    """
    This method let's program to initialize the system and get user inputs.
    :return:
    """
    max_floor = initialize_system()
    elevator = Elevator()
    elevator.set_max_floor(max_floor)
    # This method get's the user input and let it run till user presses exit
    print_and_get_user_choice(elevator, max_floor)


if __name__ == '__main__':
    # This is the starting point of the testing.
    main()
