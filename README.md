# DHCPy scanner

## Purpose
DHCPy scanner is a simple script written in Python which helps you find
potential DHCP rogue servers in your local network.
### How it works
It operates by acting as a common DHCP client: it builds a **DHCPDISCOVER** message
and broadcasts it in the local network. Then it gets every **DHCPOFFER** messages
and parses them to print various info on the terminal and on a log file.

DHCPy scanner can find rogue servers confronting their IP address with the one
specified in its input JSON file. You can also configure the JSON to send an
e-mail to the specified address if a rogue DHCP server has just been detected.
### How to use it
First rename the **input.example.json** to **input.json**, then replace the
`server_IP` field with your trusted DHCP server. This step is mandatory.

Optionally you can set the other parameters so that the scanner will be able to
send an e-mail when a rogue is found: if `mail_on`'s value is set to `true`, then
the sotfware will send the e-mail.

After the setup is complete, just launch the script with `python scanner.py`.
You will need to execute it with admin privileges, as DHCP uses UDP ports 67 and
68 to perform communications.
### Some examples
DHCPy scanner prints various information on the terminal, such as server's IP,
subnet mask, DNS IP, offered IP, lease time and more.
![random text](https://github.com/DodoIta/DHCPy-scanner/blob/readme/examples/imgs/scanner1.png "Normal Output")
![whatever text](https://github.com/DodoIta/DHCPy-scanner/blob/readme/examples/imgs/scanner2.png "Output With Rogue")
### To do
