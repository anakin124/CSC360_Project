# Practical Demonstration of HTTPS's Added Security

## Overview
The purpose of this project is to simulate a real world environment where there is a person on a public internet attempting to input personal information into a website. There will also be a nefarious machine on this public network attempting to gain access
to that personal information by using Wireshark. We will have this same setup on a web server hosting an HTTP website and another that is hosting an HTTPS website. We will then compare how easy it is for the malicious machine to gain personal information on both of them.
### Setup
Four VMs, potentially 5 with the addition of PFSense in order to put them all on the same subnet
- VM1 - HTTP website server and HTTPS 
- VM2 - Client that accesses both hosted websites
- VM3 - Nefarious packet sniffer
- VM4 - PFSense in order to put all of the vms on the same network

### Execution 
Host two websites that have some form of information intake from the users. One will be on HTTP and the other HTTPS. A client will access both of them while on the same network as the nefarious packet sniffer. We will then have that VM4 go through wireshark and try to access personal information. 

### Goal 
Demonstrate the added safety that HTTPS provides while also familiarizing ourselves with the basics of website hosting and packet sniffing.

## Structure of Repo
### Website Code
### Documentation
### Network Topology
