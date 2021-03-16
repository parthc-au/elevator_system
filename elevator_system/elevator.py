"""
This module is core of elevator simulation.
"""
import time


class Elevator:
    """
    This class contains all the members and methods which are used to simulate the elevator.
    """
    def __init__(self):
        self.min_floor = 0
        self.max_floor = 100
        self.current_floor = 0
        self.going_up = True
        self.request_log = []
        self.requested_floor = set()
        self.request_log_history = {}

    def set_max_floor(self, max_floor):
        """
        This Function sets the maximum value for the Floor.
        :param max_floor: Set the maximum floor for the elevator.
        :return:
        """
        self.max_floor = max_floor

    def move_up(self):
        """
        This function moves 1 floor up from the current floor.
        :return:
        """
        self.current_floor += 1
        self.log("UP_1")
        print(f"Elevator is at {self.current_floor}")

    def move_down(self):
        """
        This function moves 1 floor down from the current floor.
        :return:
        """
        self.current_floor -= 1
        self.log("DOWN_1")
        print(f"Elevator is at {self.current_floor}")

    def check_next_move(self):
        """
        This function checks what next move should be till it consumes all the elevator requests.
        :return:
        """
        while self.requested_floor:
            # It is synchronous implementation of elevator system. Once the simulation start's,
            # it will consume all the requests before returning to main menu.
            # It is an implementation of traditional elevator algorithm.
            if self.current_floor in self.requested_floor:
                self.log("OPEN_DOOR")
                self.log("CLOSE_DOOR")
                self.log(f"Request for {self.current_floor} is complete")
                self.request_log_history[len(self.request_log_history) + 1] = self.request_log
                self.request_log = []
                self.requested_floor.remove(self.current_floor)
            elif max(self.requested_floor) > self.current_floor:
                self.move_up()
            elif min(self.requested_floor) < self.current_floor:
                self.move_down()

    def add_request(self, request):
        """
        This function will add elevator requests to the pending list of elevator requests.
        Requests can be either single request or list of requests separated by comma(,).
        :param request: list of requests or single request between 0 and max floor.
        :return:
        """
        if isinstance(request, set):
            self.requested_floor.update(request)
        elif isinstance(request, int):
            self.requested_floor.add(request)

    def start_elevator(self):
        """
        It is the entry point to start the elevator simulation.
        :return:
        """
        self.check_next_move()
        return True

    def stop_elevator(self):
        """
        It is exit point for the elevator. If no more requests are pending in the current run,
        this method gets called.
        :return:
        """
        print(f"No more request to serve. Elevator is stooped at {self.current_floor}")

    def issue_call(self, floor):
        """
        This method let's user to set the current floor for the elevator. Elevator's moves will be
        displayed on the console.
        :param floor: New Floor position of the elevator.
        :return:
        """
        temp_request_log = []
        if self.current_floor == floor:
            pass
        elif self.current_floor > floor:
            for _ in range(self.current_floor - floor):
                temp_request_log.append("DOWN_1")
        elif self.current_floor < floor:
            for _ in range(floor - self.current_floor):
                temp_request_log.append("UP_1")
        temp_request_log.append("OPEN_DOOR")
        temp_request_log.append("CLOSE_DOOR")
        temp_request_log.append(f"Elevator has come on floor {floor}")
        self.current_floor = floor
        print(', '.join(temp_request_log))

    def visualize_monitor(self):
        """
        This method let's user to see current elevator floor and pending elevator requests.
        :return:
        """
        print(f"Current Floor is: {self.current_floor}")
        print(f"Total pending elevator request : {len(self.request_log)}")

    def consume_elevator_requests(self):
        """
        This method let's user to see how elevator is moved when each request is served.
        :return:
        """
        for _, value in self.request_log_history.items():
            print(', '.join(value))
        self.request_log_history = dict()

    def log(self, message):
        """
        This method maintains the log for each elevator move.
        :param message: The message which gets logged. Example "UP_1"
        :return:
        """
        self.request_log.append(message)
        print(message)
        time.sleep(1)
