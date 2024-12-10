# A Step by Step Guide to Replicate This Project
## Step 1: Setting up VMs
The first step will be to make 5 different vms. I will list the steps for what to download on each of the VM's here. When you first make these VM's you can use default VMWare settings and use NAT internet. This will be changed later but makes it easy to install the required softwares.
IMPORTANT NOTE: For VM's 1-4 the iso file should be the latest version of lubuntu. For VM5 the iso should be the latest version of PFSense.
### VM 1- HTTP Website Server
This VM will need the necessary software to host a website and will have to download the code from this repository.
It will need to download python which can be done from the terminal with this command. 
```
  sudo apt-get install python3
```
Now that you have python installed you can do one more command to download the necessary folder from this repo with -
```
  wget https://github.com/anakin124/CSC360_Project/Website
```
This only contains the necessary files for the website. In order to set up the server itself we need to install apache2 -
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

### VM 5- PFSense
Install the iso of PFSense and use default settings.

## Step 2: Setting up the Network

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
    ServerName yourdomain.com

    WSGIDaemonProcess myflaskapp python-path=/path/to/your/flask/app:/path/to/your/venv/lib/python3.x/site-packages
    WSGIScriptAlias / /path/to/your/flask/app/app.wsgi

    <Directory /path/to/your/flask/app>
        Require all granted
    </Directory>

    Alias /static /path/to/your/flask/app/static
    <Directory /path/to/your/flask/app/static>
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
The final step for the HTTP server is to enable the site.
```
sudo a2ensite html
sudo systemctl reload apache2
```
The steps for setting up our HTTPS server are almost identical to the above steps with several key differences. Firstly we need to self-assign an SSL key.
```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt
```
Now we need to edit the previous html.conf file in /etc/apache2/sites-available/ to enable the usage of HTTPS. The contents should like something like this.
```
<VirtualHost *:80>
    ServerName yourdomain.com
    Redirect / https://yourdomain.com/
</VirtualHost>

<VirtualHost *:443>
    ServerName yourdomain.com

    WSGIDaemonProcess myflaskapp python-path=/path/to/your/flask/app:/path/to/your/venv/lib/python3.x/site-packages
    WSGIScriptAlias / /path/to/your/flask/app/app.wsgi

    <Directory /path/to/your/flask/app>
        Require all granted
    </Directory>

    Alias /static /path/to/your/flask/app/static
    <Directory /path/to/your/flask/app/static>
        Require all granted
    </Directory>

    SSLEngine on
    SSLCertificateFile /etc/ssl/certs/apache-selfsigned.crt
    SSLCertificateKeyFile /etc/ssl/private/apache-selfsigned.key

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
Now we just need to enable SSL in Apache.
```
sudo a2enmod ssl
sudo a2ensite myflaskapp
sudo systemctl reload apache2
```
## Step 4: Packet Sniffing
