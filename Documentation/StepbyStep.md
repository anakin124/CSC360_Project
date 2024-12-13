# A Step by Step Guide to Replicate This Project
## Step 1: Setting up VMs
The first step will be to make 4 different vms. I will list the steps for what to download on each of the VM's here. When you first make these VM's you can use default VMWare settings and use NAT internet.
IMPORTANT NOTE: For VM's 1-4 the iso file should be the latest version of lubuntu.
### VM 1- HTTP Website Server
This VM will need the necessary software to host a website and will have to download the code from this repository.
It will need to download python which can be done from the terminal with this command. 
```
  sudo apt-get install python3
```
In order to set up the server itself we need to install apache2 -
```
  sudo apt install apache2 
```
Next we need to get flask for python - 
```
  sudo apt install python3-flask
```
The final dependency we have for the HTTP server is mod wsgi. This allows apache2 to run flask apps -
```
 sudo apt install libapache2-mod-wsgi-py3
```
### VM 2- HTTPS Website Server
To start repeat the steps from the HTTP server. In addition to this we will need to install OpenSSL in order to self-assign an SSL key.
```
  sudo apt install openssl
```

### VM 3- Client
Nothing needs to be done for the client as they will just be accessing websites hosted by the other VM's through any web browser on the VM.

### VM 4- Nefarious Packet Sniffer
You will need to install wireshark on this VM. To do so open a terminal and use this command -
```
  sudo apt-get install wireshark
```

## Step 2: Setting up the Network
To packet sniff an http protocol, there are a few steps. 
Begin a capture in wireshark when the user enters the website. 
Once the user has inputted his data, you can use wireshark to filter out http traffic and look at the captured packets. 
Identify the GET response message for the specified page and click on it.
At the bottom in the information page for the packet, there should be a section that it labeled hypertext transfer protocol (http). This is where all of the important page information is located.
Click on the arrow next to this section to display the page information.


## Step 3: Hosting the Websites
There are several steps that need to happen for both of the servers to host our websites. Firstly, we need to set up the directory for our flask app to run on apache. To do this copy all of the files from [here] (Website) to the /var/www/html file that should be on the machine after installing apache2. Next we need to enable the mod_wsgi module to make sure that the app works with apache2.
```
  sudo a2enmod wsgi
  sudo systemctl restart apache2
```
Now we need to create several files including an html.wsgi file in /var/www/html. It should look something like this.
```
import sys
sys.path.insert(0, "/path/to/your/flask/app")

from app import app as application  # Replace `app` with your Flask app's name
```
Next we create a html.conf file in /etc/apache2/sites-available/html.conf
```
sudo vim /etc/apache2/sites-available/html.conf
```
The files contents should look like this
```
<VirtualHost *:80>
    ServerAdmin webmaster@192.168.38.138
    ServerName 192.168.38.138  
    DocumentRoot /var/www/html

    # Serve static files from templates directory
    <Directory /var/www/html/templates>
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>

    # WSGI configuration for Flask
    WSGIDaemonProcess html python-path=/var/www/html
    WSGIScriptAlias / /var/www/html/html.wsgi

    <Directory /var/www/html>
        WSGIProcessGroup html
        WSGIApplicationGroup %{GLOBAL}
        Require all granted
    </Directory>
</VirtualHost>

```
The final step for the HTTP server is to enable the site.
```
sudo a2ensite html
sudo systemctl reload apache2
```
The steps for setting up our HTTPS server are almost identical to the above steps with several key differences. Firstly we need to self-assign an SSL key.
```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/mydomain.key -out /etc/ssl/certs/mydomain.crt
```
Now we need to edit the previous html.conf file in /etc/apache2/sites-available/ to enable the usage of HTTPS. The contents should like something like this.
```
<VirtualHost *:80> 
        ServerName 192.168.38.139 
        DocumentRoot /var/www/html 
        # Redirect HTTP to HTTPS 
        Redirect permanent / https://192.168.38.139 
</VirtualHost> 
<VirtualHost *:443> 
        ServerName 192.168.38.139 
        DocumentRoot /var/www/html 
        # SSL Configuration 
        SSLEngine on 
        SSLCertificateFile /etc/ssl/mydomain/mydomain.crt 
        SSLCertificateKeyFile /etc/ssl/mydomain/mydomain.key 
        # Serve static files from the templates directory 
        <Directory /var/www/html/templates> 
                Options Indexes FollowSymLinks 
                AllowOverride None 
                Require all granted 
        </Directory> 
        # WSGI configuration for Flask 
        WSGIDaemonProcess html python-path=/var/www/html
        WSGIScriptAlias / /var/www/html/html.wsgi 
        <Directory /var/www/html> 
                WSGIProcessGroup html 
                WSGIApplicationGroup %{GLOBAL} 
                Require all granted 
        </Directory> 
</VirtualHost>

```
Now we just need to enable SSL in Apache.
```
sudo a2enmod ssl
sudo a2ensite myflaskapp
sudo systemctl reload apache2
```
You should now be able to access both of thesee sites through a web browser by typing the IP address of the machine in the search bar.
## Step 4: Packet Sniffing
To packet sniff an http protocol, there are a few steps. 
Begin a capture in wireshark when the user enters the website. 
Once the user has inputted his data, you can use wireshark to filter out http traffic and look at the captured packets. 
Identify the GET response message for the specified page and click on it.
At the bottom in the information page for the packet, there should be a section that it labeled hypertext transfer protocol (http). This is where all of the important page information is located.
Click on the arrow next to this section to display the page information.
