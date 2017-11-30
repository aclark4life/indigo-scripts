import time

EMAIL="aclark@aclark.net"
SUBJECT = "Garage Door Status Update"

while True:
    door = indigo.devices[252434934]  # Large garage door for cars
    state = door.states[u'binaryInput1.ui']  # Open or closed
    message = ("%s is %s" % (door.name, state))  # "Door is open", or "Door is closed"
    if state != 'closed':  # If the door is not closed
      indigo.server.sendEmailTo(EMAIL, subject=SUBJECT, body=message)  # Send mail
      indigo.server.log(message)  # Log message
      print(msg)  # Print to screen
      time.sleep(60)  # Don't flood
    else:
      print(msg)  # Print to screen
      time.sleep(60)  # Don't flood
