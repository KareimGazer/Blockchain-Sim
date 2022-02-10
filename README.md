# Blockchain-Sim
a simulation of a bitcoin attack

## Abstract

Information security has become ubiquitous in this era. in this project we try to demonstrate a simple example of detection of malware based on its observed behaviour in the memory.

## The Problem
its required to identify and stop a process which allocates 200 MB in the heap for 10 seconds and deallocates them for another 10 seconds

## Solution
we observe the changes in memory usage by each processes in the systems and identify the one which allocates 200M for 10 seconds and then deallocates them for another 10 seconds. we must take into consideration that some other processes can do the same behaviour by chance so the test should be repeated multiple times to make sure that the identfied processes is indeed the malicious one.

## Main Idea
the following steps:
- collect the system info in a csv file
- clean the data and focus on the memory behaviour
- analyze the processes twice every 10 seconds so that we can notice the specific behaviour
- from the analysis process we get a list of suspicious processes
- we repeated the analysis processes again and take the intersection of the processes list
- we repeat that multiple times to make sure that our desicion is correct and the list of processes didn't happen by chance
- we stop that processes

## Getting started
To get started: 
### Installation
The script is written in python 3 to download it do the following: 
- `sudo apt-get update`
- `sudo apt-get install -y python3-pip`
we use libraries: itertools, time, random, haslib
which are preinstalled when python3 is downloaded.

### Usage
- download the files
- open a terminal and run `python3 BC.py`

### Sample Output
- attacker has 30 percent of the network compute capacity
 ![30 percent 1](https://github.com/KareimGazer/Blockchain-Sim/blob/main/screenshots/30/1.PNG?raw=true)
 ![30 percent 2](https://github.com/KareimGazer/Blockchain-Sim/blob/main/screenshots/30/2.PNG?raw=true)
 
- attacker has 45 percent of the network compute capacity
 ![45 percent 1](https://github.com/KareimGazer/Blockchain-Sim/blob/main/screenshots/45/1.PNG?raw=true)
 ![45 percent 2](https://github.com/KareimGazer/Blockchain-Sim/blob/main/screenshots/45/2.PNG?raw=true)
 
- attacker has 55 percent of the network compute capacity
 ![55 percent 1](https://github.com/KareimGazer/Blockchain-Sim/blob/main/screenshots/55/1.PNG?raw=true)
 ![55 percent 2](https://github.com/KareimGazer/Blockchain-Sim/blob/main/screenshots/55/2.PNG?raw=true)
 
- attacker has 60 percent of the network compute capacity
![60 percent](https://github.com/KareimGazer/malware-detector/blob/main/screenshots/60/1.PNG?raw=true)

Hence, we estimate that the attacker need at least 50 percent of the network compute capacity to forge a branch.

## The Nitty-Gritty Details
The program is divided into 3 functions and a driver code which uses them: 


## Folder Structure

Refer to the following table for information about important directories and files in this repository.

```
Blockchain-Sim
├── screenshots    screen shots of runnig the program.
├── README.md      main documentation.
└── BC.py          simulation program.
```
