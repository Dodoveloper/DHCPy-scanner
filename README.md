# DHCPy scanner
DHCPy scanner is a simple script written in Python which helps you find
potential DHCP rogue servers in your local network.

### Requirements
Python 3 or above should be fine. Only standard libraries are used for this software.

### How it works
It acts as a common DHCP client: it builds a **DHCPDISCOVER** message
and broadcasts it in the local network. Then it gets and parses each **DHCPOFFER**
message received to print various info on the terminal and on a log file.

DHCPy scanner can find rogue servers by confronting their IP address with the one
specified in its input JSON file. You can also configure the JSON to send an
e-mail to the specified address if a rogue DHCP server has just been detected.

### How to use it
First rename the **input.example.json** to **input.json**, then replace the
`server_IP` field with your trusted DHCP server. This step is mandatory.

Optionally you can set the other parameters so that the scanner will be able to
send an e-mail when a rogue is found: if `mail_on`'s value is set to `true` and
the other fields are set correctly, then the sotfware will send an e-mail.

Here are the JSON's  fields in detail:
- `server_IP`: IP address of your trusted DHCP server;
- `mail_sender`: sender's e-mail address;
- `mail_receiver`: receiver's e-mail address;
- `mail_domain`: your e-mail provider's server address;
- `mail_pass`: your e-mail password;
- `mail_on`: a boolean, if set to true will send e-mail.

After the setup is complete, just launch the script with `python scanner.py`.
You will need to execute it with admin privileges, as DHCP uses UDP ports 67 and
68 to perform communications.

### Examples
DHCPy scanner prints various information on the terminal, such as server's IP,
subnet mask, DNS IP, offered IP, lease time and more. 

First I put my router's IP in the JSON file and the e-mail parameters (optional).
If I launch the script on my local network, it prints out the following:

![img1](https://github.com/DodoIta/DHCPy-scanner/blob/readme/examples/imgs/scanner1.png "Normal Output")

Now let's simulate the presence of a rogue DHCP server: to do this I use
_dnsmasq_ and I make it run. This is what happens when I execute the scanner:

![img2](https://github.com/DodoIta/DHCPy-scanner/blob/readme/examples/imgs/scanner2.png "Output With Rogue")

As you can see, the script detected two servers:
- the first one is my router: since its IP address matches the one in the JSON,
everything is OK.
- the second one is dnsmasq, which is correctly detected as a rogue; also, in
this case the script sent me a notification e-mail since I enabled the e-mail
sending and a rogue was found.

In both cases each server info is written on the log file, placed in the script's directory.

### To do
- Make the script run in the background and perform scans periodically
