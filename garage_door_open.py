# Is garage door open?
#     #If garage door closed, go to END, otherwise next
#     #time_opened = now
#         Loop 1
#             If open longer than 15 minutes?
#                 Send email/text to admins
#                 Loop 2
#                     If open longer than 30 minutes?
#                     Send email/text to admins alerting them it’s closing
#                     If between 12AM and 8AM then Close garage door
#                 if garage door closed, exit loop 2, else loop
#         if garage door closed, exit loop 1, else loop
# END

import time

class GarageDoor():
    def __init__(self):
        self.position = 'CLOSED'

garage_door = GarageDoor()

while garage_door.position == 'CLOSED':
    print("Door is closed")
    time.sleep(10)
    garage_door.position = 'OPEN'
    print("Door is open")
    time_opened = time.time()
    print("Time is %s" % time_opened)
    while garage_door.position == 'OPEN':
        time.sleep(10)
        garage_door.position == 'CLOSED'
        print("Door is closed")
        time_closed = time.time()
        print("Time is %s" % time_closed)
