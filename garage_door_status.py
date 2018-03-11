import os
import time

INDIGO_ADMINS = os.environ.get('INDIGO_ADMINS', [
    'aclark@aclark.net',
])


def send_mail(**kwargs):
    indigo.server.sendEmailTo(
        kwargs['email_to'],
        subject=kwargs['email_subject'],
        body=kwargs['email_message'])
    indigo.server.log(kwargs['email_message'])


# ------------------------------------------------------------------------------

email_subject = 'Garage Door Status Update'
email_message = '%s: Waiting for garage door to open...' % email_subject

for email_to in INDIGO_ADMINS:
    indigo.server.sendEmailTo(
        email_to, subject=email_subject, body=email_message)
indigo.server.log(email_message)

time_elapsed = 0
time_start = time.time()  # https://stackoverflow.com/a/3620972

while True:
    door_obj = indigo.devices[252434934]
    door_state = door_obj.states[u'binaryInput1.ui']

    # email_message = ("%s is %s (%s)" % (door_obj.name, door_state,
    #                                     time_elapsed))

    email_message = 'Garage door has been open for %s. '
    email_message += 'Please check camera and close if needed.'

    if door_state != 'closed':
        time_elapsed = time.time() - time_start

        if time_elapsed > 300:  # 5 minutes
            email_message = email_message % '5 minutes'
            for email_to in INDIGO_ADMINS:
                send_mail(
                    email_to=email_to,
                    subject=email_subject,
                    body=email_message)
            indigo.server.log(email_message)
            time.sleep(300)

        if time_elapsed > 900:  # 15 minutes
            email_message = email_message % '15 minutes'
            for email_to in INDIGO_ADMINS:
                send_mail(
                    email_to=email_to,
                    subject=email_subject,
                    body=email_message)
            indigo.server.log(email_message)
            time.sleep(300)

        if time_elapsed > 1800:
            email_message = email_message % '30 minutes'
            for email_to in INDIGO_ADMINS:
                send_mail(
                    email_to=email_to,
                    subject=email_subject,
                    body=email_message)
            # XXX Actually close the door here
            indigo.server.log(email_message)
            time.sleep(300)
    else:
        time_start = time.time()  # Reset time tracking
        time_elapsed = 0
        time.sleep(60)
