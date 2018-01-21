import os
import time

# Configure email
EMAIL_ADDRESS = os.environ.get('INDIGO_NOTIFY_EMAIL', 'aclark@aclark.net')
EMAIL_SUBJECT = "Garage Door Status Update"

# Send first message to email address and server log
message = 'Waiting for garage door to open or close'
indigo.server.sendEmailTo(
    EMAIL_ADDRESS, subject=EMAIL_SUBJECT, body=message)  # Send mail
indigo.server.log(message)  # Log message
print(message)  # Print to screen

# Keep track of time
elapsed_time = 0
start_time = time.time()  # https://stackoverflow.com/a/3620972

while True:
    garage_door = indigo.devices[252434934]  # Large garage door for cars
    state = garage_door.states[u'binaryInput1.ui']  # Open or closed
    message = ("%s is %s (%s)" %
               (garage_door.name, state,
                elapsed_time))  # "Door is open", or "Door is closed"
    if state != 'closed':  # If the garage door is not closed
        elapsed_time = time.time() - start_time
        if elapsed_time > 900:  # 15 minutes
            indigo.server.sendEmailTo(
                EMAIL_ADDRESS, subject=EMAIL_SUBJECT,
                body=message)  # Send mail
            indigo.server.log(message)  # Log message
            print(message)  # Print to screen
            time.sleep(60)  # Don't flood
        if elapsed_time > 1800:  # 30 minutes
            # Close door here
            indigo.server.sendEmailTo(
                EMAIL_ADDRESS, subject=EMAIL_SUBJECT,
                body=message)  # Send mail
            indigo.server.log(message)  # Log message
            print(message)  # Print to screen
            time.sleep(60)  # Don't flood
    else:
        start_time = time.time()  # Reset time tracking
        elapsed_time = 0  # Reset time tracking
        print(message)  # Print to screen
        time.sleep(60)  # Don't flood
