# Medical Distributed Ledger Technology 

Programming with Advanced Computer Languages - Python

26 May 2019

**Team Snakes**: Benjamin Cook, Dominik Eitljörg, Johanna Husson, Christopher Newson, Dean van der Merwe.

## Description

This project creates a distributed ledger technology (DLT) to store patient data. The intended users are physicians who need to access and modify patients’ files during or after a medical consultation, to register diagnoses and prescribe medications. Pharmacists are also potential users, to register medications bought by a given patient. The blockchain (BC) architecture ensures traceability of all actions undertaken on a patient file by alerting the user when a file has been tampered with. 

A patient file is stored as a dictionary. A hashing algorithm, which assigns a cryptographic key to its input (here, the input being a dictionary), ensures the integrity of patient data because: 1- It is impossible to have the same hash for two different inputs; 2- The exact same patient dictionary produces the same hash; 3- Conversely, any change to the dictionary modifies the hash. 

A BC is automatically created when the program is started. The BC is only stored as long as the program is running. Every block includes an index number, the previous block’s hash and the hash of the patient data. Whenever the user changes his data, a new block is created with a new hash. Hashes of every action are saved in a list which can be visualised by the user. 

When starting the program, the user is prompted to add a new patient file. After doing so he can also verify existing data, where the code checks the hashes from the previous blocks and uses this to verify whether the data was once created within the program or if it was created / altered by some third party. 


![Overview Architecture](https://user-images.githubusercontent.com/42732444/58156193-d8184d80-7c75-11e9-8620-4d5ce8b65fc1.png "Overview Architecture")
 
*Figure 1: Visualisation of our blockchain technology for patient data.*

The patient data itself is not stored on the BC, only the hash identifying it is stored. Therefore, a user cannot see the content of a patient file, but can only see the resulting hash to verify data has not been tampered with. 

## Instructions
*Code has to be downloaded and run offline. Settings have to allow the code to save a local copy of the patient data.*
1.	Run the program to create a BC:
	1.	You are asked to enter the first patient’s information. A new block is created. 
	2.	You can later add new patients' files (Option 1). Every new file creates a new block on the BC. 
	3.	Alternatively, you can load an existing patient file to modify it (Option 2). In case of modification, a new hash is created and a new block is added to the BC. *Text Files must be saved in the working directory.*
	4.	Finally, you can visualise the list of hashes stored on the BC (Option 3). 
2.	Test the ability of the program to identify a corrupted file:
	1.	First, run the program and enter at least one patient dictionary (let’s call it abcde1234) in it. Your patient file (abcde1234) is stored locally on your computer. The file name will start with the first two letters of the surname followed by the last two letters of the first name and end with a random number (e.g. John Doe's file would be "Dohn_86712950").
	2.	When in the menu use *Option 2* and try to load one of the patient test data sets (e.g. "Apsa_45673575"). Receive a message *“File couldn’t be verified with existing BC entries"*: the hash does not correspond to any hash loaded on your current BC. 
	3.	When you are given the option to edit the data and thereby verify it this will add it to the BC. Thus, select "y".
	4.	When given the option of modifying the current file or adding to it simply press *enter* to bypass the step, verify the data and add a new block to the BC.
	5.	The BC will now recognise that the data is verified and hasn't been tampered with if it is checked again.
3.	Terminate the program (Option 4)
	1.	The BC is lost when the program is terminated. 

## Requirements

None, all libraries come installed with Python. The program was tested for functionality in Spyder (Python 3.7) in Mac and Windows and PyCharm (Python 3.7) in Windows.

## Limitations

Some factors limit the real-life usability of the code:
* The BC cannot be saved and accessed at a later point, thus it is not distributed. However, the main building blocks remain the same and the distribution would be an additional add-on to this code.
* The hash is created each time the code is run. It can load previous data, however only into the new hash.
* We could increase "tamper-proofness" by storing the patient data itself on an individual BC but here the limits of BC technology could be reached quite quickly (for an extended article on BC limitations see [this link](https://malcoded.com/posts/storing-data-blockchain/ "Blog Post on Blockchain Limitations").

All of the above limitations could be avoided with more resources but in the scope of this project we think the program is sufficient to showcase a use of BC for medical patient records.
