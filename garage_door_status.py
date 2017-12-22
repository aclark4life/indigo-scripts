import time

EMAIL="aclark@aclark.net"
SUBJECT = "Garage Door Status Update"

while True:
    door = indigo.devices[252434934]  # Large garage door for cars
    state = door.states[u'binaryInput1.ui']  # Open or closed
    start_time = time.time()  # https://stackoverflow.com/a/3620972  
    if state != 'closed':  # If the door is not closed
        elapsed_time = time.time() - start_time
        message = ("%s is %s (%s)" % (door.name, state, elapsed_time))  # "Door is open", or "Door is closed"
        indigo.server.sendEmailTo(EMAIL, subject=SUBJECT, body=message)  # Send mail
        indigo.server.log(message)  # Log message
        print(message)  # Print to screen
        time.sleep(60)  # Don't flood
    else:
        print(message)  # Print to screen
        time.sleep(60)  # Don't flood
