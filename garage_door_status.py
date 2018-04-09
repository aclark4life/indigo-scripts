import os
import time

INDIGO_ADMINS = os.environ.get('INDIGO_ADMINS', 'aclark@aclark.net')
if INDIGO_ADMINS and INDIGO_ADMINS.find(',') == -1:
    INDIGO_ADMINS = [INDIGO_ADMINS]
else:
    INDIGO_ADMINS = INDIGO_ADMINS.split(',')


def send_mail(**kwargs):
    for email_to in INDIGO_ADMINS:
        indigo.server.sendEmailTo(
            email_to, subject=kwargs['subject'], body=kwargs['body'])


# ------------------------------------------------------------------------------

email_subject = 'Garage Door Status Update'
email_message = 'Waiting for garage door to open...'
send_mail(body=email_message, subject=email_subject)
indigo.server.log(email_message)
indigo.server.log(
    "Sending notification emails to %s." % ','.join(INDIGO_ADMINS))

time_elapsed = 0
time_start = time.time()  # https://stackoverflow.com/a/3620972

while True:
    door_obj = indigo.devices[252434934]
    door_input_ui = door_obj.states[u'binaryInput1.ui']
    door_input_obj = door_obj.states[u'binaryInput1']
    door_output_obj = door_obj.states[u'binaryOutput1']

    # email_message = ("%s is %s (%s)" % (door_obj.name, door_input,
    #                                     time_elapsed))

    email_message = 'Garage door has been open for %s. '
    email_message += 'Please check camera and close if needed.'

    if door_input_ui != 'closed':
        time_elapsed = time.time() - time_start

        if time_elapsed > 300:  # 5 minutes
            email_message = email_message % '5 minutes'
            send_mail(body=email_message, subject=email_subject)
            indigo.server.log(email_message)
            time.sleep(300)

        if time_elapsed > 900:  # 15 minutes
            email_message = email_message % '15 minutes'
            send_mail(body=email_message, subject=email_subject)
            indigo.server.log(email_message)
            time.sleep(300)

        if time_elapsed > 1800:
            # email_message += ' Closing door.'
            email_message = email_message % '30 minutes'
            send_mail(body=email_message, subject=email_subject)
            # Actually close the door.
            # XXX
            indigo.server.log(email_message)
            time.sleep(300)
    else:
        time_start = time.time()  # Reset time tracking
        time_elapsed = 0
        time.sleep(60)
