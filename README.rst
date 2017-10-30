Indigo Scripts
==============

To be copied to ``/Library/Application Support/Perceptive Automation/Indigo 7`` as described here:

- http://wiki.indigodomo.com/doku.php?id=indigo_7_documentation:plugin_guide#indigo_support_folder_structure

And to be executed as described here("You can drop Python scripts and AppleScripts into this folder and they will show up in your plugin's sub-menu on the new “Plugins” menu. "):

- http://wiki.indigodomo.com/doku.php?id=indigo_7_documentation:plugin_guide#menu_items_folder

Also see:

- http://wiki.indigodomo.com/doku.php?id=indigo_7_documentation:plugin_scripting_tutorial

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


::

     ~/Developer/aclarknet/indigo-scripts > master > bin/python garage_door_status.py
    Door is closed
    Door is open
    Time is 1506603461.545657
    Door is closed
    Time is 1506603471.546791
    Door is closed
    Time is 1506603481.548479
    Door is closed
    Time is 1506603491.549773
    Door is closed
    Time is 1506603501.551779
    Door is closed
    Time is 1506603511.554742
    Door is closed
    Time is 1506603521.555243
    Door is closed
    Time is 1506603531.557129

