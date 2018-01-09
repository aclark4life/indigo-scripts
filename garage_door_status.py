import os
import time

EMAIL = os.environ.get('INDIGO_NOTIFY_EMAIL', 'aclark@aclark.net')
SUBJECT = "Garage Door Status Update"

elapsed_time = 0

indigo.server.sendEmailTo(
    EMAIL, subject=SUBJECT, body='Waiting for garage door')  # Send mail

while True:
    garage_door = indigo.devices[252434934]  # Large garage door for cars
    state = garage_door.states[u'binaryInput1.ui']  # Open or closed
    start_time = time.time()  # https://stackoverflow.com/a/3620972
    message = ("%s is %s (%s)" %
               (garage_door.name, state,
                elapsed_time))  # "Door is open", or "Door is closed"
    if state != 'closed':  # If the garage door is not closed
        elapsed_time = time.time() - start_time
        indigo.server.sendEmailTo(
            EMAIL, subject=SUBJECT, body=message)  # Send mail
        indigo.server.log(message)  # Log message
        print(message)  # Print to screen
        time.sleep(60)  # Don't flood
    else:
        elapsed_time = 0
        print(message)  # Print to screen
        time.sleep(60)  # Don't flood
