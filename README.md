# Practical Demonstration of HTTPS's Added Security

## Overview
The purpose of this project is to simulate a real world environment where there is a person on a public internet attempting to input personal information into a website. There will also be a nefarious machine on this public network attempting to gain access to that personal information by using Wireshark. We will have this same setup on a web server hosting an HTTP website and another that is hosting an HTTPS website. We will then compare how easy it is for the malicious machine to gain personal information on both of them.
### Setup
5 VMs:
- VM1 - HTTP Website Server
- VM2 - HTTPS Website Server
- VM2 - Client that accesses both hosted websites
- VM3 - Nefarious packet sniffer
- VM4 - PFSense in order to put all of the vms on the same network

### Execution 
Host two websites that have some form of information intake from the users. One will be on HTTP and the other HTTPS. A client (VM3) will access both of them while on the same network as the nefarious packet sniffer (VM4) attempts to get the info.

### Goal 
Demonstrate the added safety that HTTPS provides while also familiarizing ourselves with the basics of website hosting and packet sniffing.

## Structure of Repo
### Website Code
We used flask to host the websites because it is very lightweight and easy to use considering it can take user input. The flask code and httml code for the websites can be found in the [Website](/Website) folder.
### Documentation
The documentation offers a detailed step by step guide for how you can replicate this project exactly, consolidated into a (relatively) brief markdown file. This file can be found [here](/Documentation/StepbyStep.md).
### Network Topology
Lastly we thought it was important to document what the network topolgy of all of these VM's along with the computer they are being hosted on looks like. We have the network topology diagram and explanation [here](/Documentation/NetworkTopology.md).
