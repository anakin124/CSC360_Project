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

## Step 4: Packet Sniffing
