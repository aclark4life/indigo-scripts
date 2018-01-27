import os
import time

EMAIL_ADDRESS = os.environ.get('INDIGO_NOTIFY_EMAIL', 'aclark@aclark.net')
EMAIL_SUBJECT = "Garage Door Status Update"

message = 'Waiting for garage door to open or close'
indigo.server.sendEmailTo(EMAIL_ADDRESS, subject=EMAIL_SUBJECT, body=message)
indigo.server.log(message)
print(message)

elapsed_time = 0
start_time = time.time()  # https://stackoverflow.com/a/3620972

while True:
    garage_door = indigo.devices[252434934]
    state = garage_door.states[u'binaryInput1.ui']
    message = ("%s is %s (%s)" % (garage_door.name, state, elapsed_time))
    if state != 'closed':
        elapsed_time = time.time() - start_time
        if elapsed_time > 900:  # 15 minutes
            indigo.server.sendEmailTo(
                EMAIL_ADDRESS, subject=EMAIL_SUBJECT, body=message)
            indigo.server.log(message)
            print(message)
            time.sleep(60)
        if elapsed_time > 1800:
            # XXX Close door
            indigo.server.sendEmailTo(
                EMAIL_ADDRESS, subject=EMAIL_SUBJECT, body=message)
            indigo.server.log(message)
            print(message)
            time.sleep(60)
    else:
        start_time = time.time()  # Reset time tracking
        elapsed_time = 0
        print(message)
        time.sleep(60)
