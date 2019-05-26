# Medical Distributed Ledger Technology 

Programming with Advanced Computer Languages - Python

26 May 2019

**Team Snakes**: Benjamin Cook, Dominik Eitljörg, Johanna Husson, Christopher Newson, Dean van der Merwe.

## Description

This project creates a distributed ledger technology (DLT) to store patient data. The intended users are physicians who need to access and modify patients’ files during or after a medical consultation, to register diagnoses and prescribe medications. Pharmacists are also potential users, to register medications bought by a given patient. The blockchain architecture ensures traceability of all actions undertaken on a patient file by alerting the user when a file has been tampered with. 

A patient file is stored as a dictionary. A hashing algorithm, which assigns a cryptographic key to its input (here, the input being a dictionary), ensures the integrity of patient data because: 1- It is impossible to have the same hash for two different inputs; 2- The exact same patient dictionary produces the same hash; 3- Conversely, any change to the dictionary modifies the hash. 

A blockchain (BC) is automatically created when the program is started. The blockchain is only stored as long as the program is running. Every block includes an index number, the previous block’s hash and the hash of the patient data. Whenever the user changes his data, a new block is created with a new hash. Hashes of every action are saved in a list which can be visualised by the user. 

When starting the program, the user is prompted to either add a new patient file or load an existing file. In the latter case, the code checks the hashes from the previous blocks and uses this to verify whether the data was once created within the program or if it was created / altered by some third party. 


![Overview Architecture](https://user-images.githubusercontent.com/42732444/58156193-d8184d80-7c75-11e9-8620-4d5ce8b65fc1.png)
 
*Figure 1: Visualisation of our blockchain technology for patient data.*

The patient data itself is not stored on the blockchain, only the hash identifying it is stored. Therefore, a user cannot see the content of a patient file, but can only see the resulting hash to verify data has not been tampered with. 

## Limitations
There are various limitations to this program, both in regards to the blockchain itself and to the funcitoning of this program itself.

We could increase "tamper-proofness" by storing the patient data itself on an individual blockchain but here the limits of blockchain technology could be reached quite quickly (for an extended article on blockchain limitations see [this link](https://malcoded.com/posts/storing-data-blockchain/ "Blog Post on Blockchain Limitations").

## Instructions
*Code has to be downloaded and run offline*
1.	Run the program to create a blockchain:
	1.	You are asked to enter the first patient’s information. A new block is created. 
	2.	You can later add new patients' files (Option 1). Every new file creates a new block on the BC. 
	3.	Alternatively, you can load an existing patient file to modify it (Option 2). In case of modification, a new hash is created and a new block is added to the blockchain. *Text Files must be saved in the working directory"
	4.	Finally, you can visualise the list of hashes stored on the blockchain (Option 3). 
2.	Test the ability of the program to identify a corrupted file:
	1.	After having run the program a first time and entered at least one patient dictionary (let’s call it abcde1234) in it, log out of the program (Option 4). Your patient file (abcde1234) is stored locally on your computer. 
	2.	Start a new program and try to load the patient file you had created on the previous program (abcde1234). Receive a message *“File couldn’t be verified with existing blockchain entries"*: the new hash does not correspond to any hash loaded on your current blockchain. 
	3.	Run program a first time ⇒ file stored locally. Close program. 
	4.	Run program a second time ⇒ try to load file. Corrupted. 
3.	Terminate the program (Option 4)
	1.	The blockchain is lost when the program is terminated. 

## Requirements

None, all libraries come installed with Python. The program was tested for functionality in **XYZ**.

## Limitations
Various factors limit the real-life usability of the code:
* The blockchain can not be saved and accessed at a later point, thus it is not distributed
* Hash is created each time the code is run and can load previous data, however only into the new hash
