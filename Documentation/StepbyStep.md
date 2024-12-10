# A Step by Step Guide to Replicate This Project
## Step 1: Setting up VMs
The first step will be to make 4 different vms. I will list the steps for what to download on each of the VM's here. When you first make these VM's you can use default VMWare settings and use NAT internet. This will be changed 
later but makes it easy to install the required softwares.
### VM 1- HTTP Server
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

### VM 2- Client

### VM 3- Nefarious Packet Sniffer

### VM 4- PFSense

## Step 2: Setting up the Network

## Step 3: Hosting the Websites

## Step 4: Packet Sniffing
