Indigo Scripts
==============

Task #1
-------

Write a Python script that does the following: Notify owner and administrative users via text message (which can be done via the email function in Indigo) if the garage door has been left open for more than 15 minutes. If open for 30 minutes (and if between 12 midnight and 8am) then send another notification and close the garage door.

::

    # Pseudocode
    Is garage door open?
        #If garage door closed, go to END, otherwise next
        #time_opened = now
            Loop 1
                If open longer than 15 minutes?
                    Send email/text to admins
                    Loop 2
                        If open longer than 30 minutes?
                        Send email/text to admins alerting them it’s closing
                        If between 12AM and 8AM then Close garage door
                    if garage door closed, exit loop 2, else loop
            if garage door closed, exit loop 1, else loop
    END

Installation and usage from Terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    alias indigohost='/Library/Application\ Support/Perceptive\ Automation/Indigo\ 7/IndigoPluginHost.app/Contents/MacOS/IndigoPluginHost'
    git clone git@github.com:aclarknet/indigo-scripts.git
    cd indigo-scripts
    export INDIGO_ADMINS=aclark@aclark.net,

Start
~~~~~

::

    indigohost -x garage_door_status.py

Stop
~~~~

::

    CTRL-Z
    kill -9 %1
