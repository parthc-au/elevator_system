Elevator System
-
This is a private project set up as part of the interview process.

### Important Information
**Python Version**: 3.7

Simulated Elevator can perform following functions:
1. Elevator can go up or down
2. Elevator can display current floor
3. Elevator can show it's Computed Path to serve the inside or outside elevator requests
4. Elevator Controller can make explicit request to send Elevator to specific floor

*Note*: For simplicity, this elevator considers all the requests inside/outside same.

This is synchronous elevator simulation. Meaning at any time it is performing one request. The primary focus is correctly implementing the elevator algorithm.

**pylint score**:
```python
results = Run(['elevator_system/elevator.py','elevator_system/run.py'], do_exit=False)
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```
***Sample Test Cases***

*Note*: All the test cases listed below are run in continuation. For example, at the end of test case 1 elevator is at 5th floor so when we request elevator to go to 8th floor then it has to climb only three floors.

Case 1: 

Max_Floor: 10 

Elevator request type: Internal/external

Elevator request 1,2,4,5 

Output: UP_1, OPEN_DOOR, CLOSE_DOOR, Request for 1 is complete
UP_1, OPEN_DOOR, CLOSE_DOOR, Request for 2 is complete
UP_1, UP_1, OPEN_DOOR, CLOSE_DOOR, Request for 4 is complete
UP_1, OPEN_DOOR, CLOSE_DOOR, Request for 5 is complete

Case 2:

Elevator request: Go to floor 8

Output:  UP_1, UP_1, UP_1, OPEN_DOOR, CLOSE_DOOR, Elevator has come on floor 8

**How to use**

To run this program, use the python console and execute run.py