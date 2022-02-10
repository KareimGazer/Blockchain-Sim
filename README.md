# Blockchain-Sim
a simulation of a bitcoin attack

## Abstract
Information security has become ubiquitous in this era. in this project we try to demonstrate a simple example of detection of malware based on its observed behaviour in the memory.
crypto currency is of vital importance these days. It provides privacy, security, confidentiality, and decentralized transactions. In this project we demonstrate a basic example of the bit coin using the python programming language with the simulation of an attacker trying to forge the transcation history.

## Keeping track of branches
all blocks are stored in a hash table "python dictionary" indexed by their has value, and each block contains the hash of the previous block, so we can go backwards in the chain by using that previous hash to index into the hash table and repeat the process untill reaching the first block.

## N zeros
N is choosed to be 20 binary zeros or 5 hex zeros to produces a hash beginning of that number of zeros every one second.
in the program we use N = 5 because of the hexdecimal notation used in the python sha256 function which is equivalent to 20 binary zeros.

## Simulation
- The user gives the program a number of rounds "i.e. iterations" in every iteration both Alice and Darth try to produce a block so that Bob can use it. Bob watches the processes and compares the length of both branches of Alice and Drath and attach to the longest.
Darth starts with the block just before the last verified one and tries to forge a branch.
- the users gives the program the probability that the attacker "Darth" will manage produce a block in every round which corresponds to the percentage of the network computing power. for example if the attacker has half of the computers on the network it can mine in the next round with 50% chance.

- we keep giving the program these percentages until Darth produce a branch, then we know what percent of the network the attacker need or how much faster should the attacker be "both are equivalent".

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
![60 percent](https://github.com/KareimGazer/Blockchain-Sim/blob/main/screenshots/60/1.PNG?raw=true)

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
