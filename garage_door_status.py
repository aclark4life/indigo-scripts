# ------------------------------------------------------------------------------
# Pseudocode
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

# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# Multi-door support via http://forums.indigodomo.com/viewtopic.php?f=77&t=13579#p95041
# 
# # a list of your garage door I/O Linc IDs from Indigo
# garage_door_ids = [1053088701, 324932738] 
# 
# # variable that holds the value of the doors
# door_is_open = "closed"
# 
# # repeat for each ID in your list
# for id in garage_door_ids:
#     try:
#         # if the input is not true, it's open
#         if not indigo.devices[id].binaryInputs[0]:
#             # set the variable
#             door_is_open = "open"
#             
#             # stop the loop since we found an open door
#             break
#     except:
#         pass # device might not be availble for some reason
# 
# # Set the variable value - insert the Indigo ID of your variable
# indigo.variable.updateValue(1229620185, door_is_open)

# ------------------------------------------------------------------------------
# Sending email
#
# Via http://wiki.indigodomo.com/doku.php?id=indigo_6_documentation:plugin_scripting_tutorial#sending_emails
#
# indigo.server.sendEmailTo("aclark@aclark.net", subject="Subject Line Here", body="Some longish text for the body of the email")
#

# ------------------------------------------------------------------------------
# Turn on a light only if it's been off for longer than 1 minute:
#
# Via http://wiki.indigodomo.com/doku.php?id=indigo_6_documentation:plugin_scripting_tutorial#turn_on_a_light_only_if_it_s_been_off_for_longer_than_1_minute 
#
# from datetime import datetime
# lamp = indigo.devices[91776575] # "Hallway light"
# timeDelta = datetime.now() - lamp.lastChanged
# if not lamp.onState and timeDelta.seconds > 60:
#         indigo.device.turnOn(91776575)

# ------------------------------------------------------------------------------
# Log to the Indigo Event Log window all of the attributes/properties of the device "office desk lamp":
#
# Via http://wiki.indigodomo.com/doku.php?id=indigo_6_documentation:plugin_scripting_tutorial#log_to_the_indigo_event_log_window_all_of_the_attributes_properties_of_the_device_office_desk_lamp
#
# lamp = indigo.devices["office desk lamp"]
# indigo.server.log(lamp.name + ": \n" + str(lamp))

# import time
# while True: 
#   gd = indigo.devices[252434934]  # Large garage door for cars
#   state = gd.states[u'binaryInput1.ui']
#   msg = ("%s is %s" % (gd.name, state))
#   if state != 'closed':
#     indigo.server.sendEmailTo("aclark@aclark.net", subject="Garage Door Status Update", body=msg)
#     indigo.server.log(msg)
#     print(msg)
#   else:
#     print(msg)
#     time.sleep(60)
fathom:Python Scripts fathombuildingmanager$ vi garage_door_status.py 
fathom:Python Scripts fathombuildingmanager$ cat garage_door_status.py 
# ------------------------------------------------------------------------------
# Pseudocode
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

# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# Multi-door support via http://forums.indigodomo.com/viewtopic.php?f=77&t=13579#p95041
# 
# # a list of your garage door I/O Linc IDs from Indigo
# garage_door_ids = [1053088701, 324932738] 
# 
# # variable that holds the value of the doors
# door_is_open = "closed"
# 
# # repeat for each ID in your list
# for id in garage_door_ids:
#     try:
#         # if the input is not true, it's open
#         if not indigo.devices[id].binaryInputs[0]:
#             # set the variable
#             door_is_open = "open"
#             
#             # stop the loop since we found an open door
#             break
#     except:
#         pass # device might not be availble for some reason
# 
# # Set the variable value - insert the Indigo ID of your variable
# indigo.variable.updateValue(1229620185, door_is_open)

# ------------------------------------------------------------------------------
# Sending email
#
# Via http://wiki.indigodomo.com/doku.php?id=indigo_6_documentation:plugin_scripting_tutorial#sending_emails
#
# indigo.server.sendEmailTo("aclark@aclark.net", subject="Subject Line Here", body="Some longish text for the body of the email")
#

# ------------------------------------------------------------------------------
# Turn on a light only if it's been off for longer than 1 minute:
#
# Via http://wiki.indigodomo.com/doku.php?id=indigo_6_documentation:plugin_scripting_tutorial#turn_on_a_light_only_if_it_s_been_off_for_longer_than_1_minute 
#
# from datetime import datetime
# lamp = indigo.devices[91776575] # "Hallway light"
# timeDelta = datetime.now() - lamp.lastChanged
# if not lamp.onState and timeDelta.seconds > 60:
#         indigo.device.turnOn(91776575)

# ------------------------------------------------------------------------------
# Log to the Indigo Event Log window all of the attributes/properties of the device "office desk lamp":
#
# Via http://wiki.indigodomo.com/doku.php?id=indigo_6_documentation:plugin_scripting_tutorial#log_to_the_indigo_event_log_window_all_of_the_attributes_properties_of_the_device_office_desk_lamp
#
# lamp = indigo.devices["office desk lamp"]
# indigo.server.log(lamp.name + ": \n" + str(lamp))

# import time
# while True: 
#   gd = indigo.devices[252434934]  # Large garage door for cars
#   state = gd.states[u'binaryInput1.ui']
#   msg = ("%s is %s" % (gd.name, state))
#   if state != 'closed':
#     indigo.server.sendEmailTo("aclark@aclark.net", subject="Garage Door Status Update", body=msg)
#     indigo.server.log(msg)
#     print(msg)
#   else:
#     print(msg)
#     time.sleep(60)
