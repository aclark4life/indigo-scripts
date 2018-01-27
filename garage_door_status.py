import os
import time

email_address = os.environ.get('INDIGO_NOTIFY_EMAIL', 'aclark@aclark.net')
email_subject = 'Garage Door Status Update'
email_message = 'Waiting for garage door to open or close'

indigo.server.sendEmailTo(
    email_address, subject=email_subject, body=email_message)
indigo.server.log(email_message)

time_elapsed = 0
time_start = time.time()  # https://stackoverflow.com/a/3620972

while True:
    door_obj = indigo.devices[252434934]
    door_state = door_obj.states[u'binaryInput1.ui']

    email_message = ("%s is %s (%s)" % (door_obj.name, door_state,
                                        time_elapsed))

    if door_state != 'closed':
        time_elapsed = time.time() - time_start

        indigo.server.sendEmailTo(
            email_address, subject=email_subject, body=email_message)
        indigo.server.log(email_message)

        if time_elapsed > 900:  # 15 minutes
            indigo.server.sendEmailTo(
                email_address, subject=email_subject, body=email_message)
            indigo.server.log(email_message)
            time.sleep(60)

        if time_elapsed > 1800:

            # XXX Actually close the door here

            indigo.server.sendEmailTo(
                email_address, subject=email_subject, body=email_message)
            indigo.server.log(email_message)
            time.sleep(60)
    else:
        time_start = time.time()  # Reset time tracking
        time_elapsed = 0
        time.sleep(60)
