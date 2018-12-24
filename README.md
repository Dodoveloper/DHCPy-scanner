# DHCPy scanner

## Purpose
DHCPy scanner is a simple script written in Python which helps you find
potential DHCP rogue servers in your local network.
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

After the setup is complete, just launch the script with **_python scanner.py_**.
You will need to execute it with admin privileges, as DHCP uses TCP ports 67 and
68 to perform communications.
### Some examples
DHCPy scanner prints various information on the terminal, such as server's IP,
subnet mask, DNS IP, offered IP, lease time and more.
### Future updates
