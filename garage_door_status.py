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

# import time
# 
# class GarageDoor():
#     def __init__(self):
#         self.position = 'CLOSED'
# 
# garage_door = GarageDoor()
# 
# while garage_door.position == 'CLOSED':
#     print("Door is closed")
#     time.sleep(10)
#     garage_door.position = 'OPEN'
#     print("Door is open")
#     time_opened = time.time()
#     print("Time is %s" % time_opened)
#     while garage_door.position == 'OPEN':
#         time.sleep(10)
#         garage_door.position == 'CLOSED'
#         print("Door is closed")
#         time_closed = time.time()
#         print("Time is %s" % time_closed)


# Via http://forums.indigodomo.com/viewtopic.php?f=77&t=13579#p95041

# a list of your garage door I/O Linc IDs from Indigo
garage_door_ids = [1053088701, 324932738] 

# variable that holds the value of the doors
door_is_open = "closed"

# repeat for each ID in your list
for id in garage_door_ids:
    try:
        # if the input is not true, it's open
        if not indigo.devices[id].binaryInputs[0]:
            # set the variable
            door_is_open = "open"
            
            # stop the loop since we found an open door
            break
    except:
        pass # device might not be availble for some reason

# Set the variable value - insert the Indigo ID of your variable
indigo.variable.updateValue(1229620185, door_is_open)
