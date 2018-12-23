# DHCPy scanner
A simple DHCP scanner written in Python 3

## Purpose
DHCPy scanner is a simple script written in Python which helps you find
possible DHCP rogue servers in your local network.
### How it works
It operates by acting as a common DHCP client: it builds a DHCPDISCOVER message
and broadcasts it in the local network. Then it gets every DHCPOFFER messages
and parses them to print various info on the terminal and on a log file.

DHCPy scanner can find rogue servers confronting their IP address with the one
specified in its input JSON file. You can also configure the JSON to send an
e-mail to the specified address if a rogue DHCP server has just been detected.
### How to use it
First rename the **input.example.json** to **input.json**, then replace the
_server_IP_ field with your trusted DHCP server. This step is mandatory.

Optionally you can set the other parameters so that the scanner will be able to
send an e-mail when a rogue is found: if _mail_on_'s value is set to "yes", then
the sotfware will send the e-mail; any other string should be considered as a no.
### Some examples
### Future updates
