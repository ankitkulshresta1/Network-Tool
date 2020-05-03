* This tool is based on python3.

* I created this for my L1 team, This tool has 2 buttons. 1 button to get the CPU utilization and 2nd tool is to get the interface status for Cisco switches.

* In the entry field, we need to put the IP for Cisco devices.

* "Get CPU" will going to give the output for "sh processes cpu | exclude 0.00"

* "Get Int" will going to give output for "sh int status".

* You have to set username and password for the device in the script manually.
		'username': 'admin',
                'password': 'admin'

* This script will only be going to work for Cisco.