#import features required
import hashlib, json, sys
import hashlib as hasher
import pickle
import os
from random import random
import platform



###############################################################################################################
#
#---------------------------Patientdata functions starts here--------------------------------------------
#
###############################################################################################################



#create a new patient dictionary asking the 7 inputs from the patient and automatically saves it to working directory path
def create_patient_dict():
    surname = str(input("Please type your Surname: "))
    firstname = str(input("Please type your First name: "))
    birthdate = str(input("Please type your date of birth (DD.MM.YYYY): "))
    pat_id = surname[:2] + firstname[-2:] + '_' + str(int(random()*100000000))
    sex = str(input("Please type your sex (m or f): "))
    insurance = str(input("Please state your insurance type (private or public): "))
    smoke = str(input("Please state if you smoke (yes or no): "))
    sport = str(input("Please state how often you do sport a week: "))
    citizenship = str(input("Please state your country of citizenship: "))
    diagnoses = []
    print('Please list the diagnoses. Press <enter> to list the next diagnosis. If finished press <enter> again')
    i = 0
    while 1:
        i += 1
        diagnosis = input('Enter diagnosis %d: ' % i)
        if diagnosis == '':
            break
        diagnoses.append(diagnosis)
    print('Please repeat the process for medication prescribed to the patient')
    prescribed_meds = []
    i = 0
    while 1:
        i += 1
        meds = input('Enter medication %d: ' % i)
        if meds == '':
            break
        prescribed_meds.append(meds)
                          
    patientdict = {}

    for attribute in ('surname', 'firstname', 'birthdate', 'pat_id', 'sex', 'insurance',
                      'smoke', 'sport', 'citizenship', 'diagnoses', 'prescribed_meds'):
        patientdict[attribute] = locals()[attribute]

    # this saves the dictionary to the working directory either for Mac or Windows computer
    save_dict(patientdict)

    return patientdict

#save the patient dictionary to a desired .txt file (works for both Mac and Windows)-->name of file can be given as patient_ID; saves the dictionary created in create_patient_dict
def save_dict(patientdict):
    patient_ID = patientdict["pat_id"]
    path = os.getcwd()
    ostype = platform.system()
    if ostype == "Darwin":
        with open(path + '//' + patient_ID + ".txt", 'wb') as f:
            pickle.dump(patientdict, f, pickle.HIGHEST_PROTOCOL)
    elif ostype == "Windows":
        with open(path + '\\' + patient_ID + ".txt", 'wb') as f:
            pickle.dump(patientdict, f, pickle.HIGHEST_PROTOCOL)

#load a dictionary with the given patient_ID
def load_dict(patient_ID):
    path = os.getcwd()
    ostype = platform.system()
    if ostype == "Darwin":
        with open(path + '//' + patient_ID, 'rb') as f:
            return pickle.load(f)
    elif ostype == 'Windows':
        with open(path + '\\' + patient_ID, 'rb') as f:
            return pickle.load(f)

#lists all Patient files in the Python directory and gives you the option to select one
def select_file():
    a = os.listdir(os.getcwd())
    patient_datafiles = []
    for n in a:
        try:
            if n[4] == "_" and n[-4:] == ".txt":
                patient_datafiles.append(n)
        except:
            print("", end="")

    cot = 1
    for n in patient_datafiles:
        print("Patientfile Nr. %d: %s" % (cot,n))
        cot += 1

    choice = int(input("Which file do you want to select? Press *Number*: "))

    sel_file = patient_datafiles[(choice - 1)]

    return sel_file

#modify entries of dictionary; the dictionary has to be given in the function
def modify_dict(dictionary):
    print(dictionary)
    changes = input("Would you like to modify or add entries? press (mod/add): ")
    if changes == "add":
        attribute = input("What attribute would you like to add?: ")
        value = input("What should the value of this attribute be?: ")
        dictionary[attribute] = value

    elif changes == 'mod':
        response = 'n'
        while response == 'n':
            print('\n')
            print('Please type the corresponding title of the entry you wish to modify')
            for key, value in dictionary.items():
                print(key, value)
            modentry = input(': ')
            response = input('Is' + ' ' + modentry + ' ' + 'the entry you wish to modify? (y/n) ')
        if response == 'y':
            newvalue = input("What should the value of" + ' ' + modentry + ' ' + "have? ")
            d1 = {modentry: newvalue}
            dictionary.update(d1)

    print("dictionary has been modified")
    return dictionary

###############################################################################################################
#
#------------------------------------Blockchain function starts here ------------------------------------------
#
###############################################################################################################

#Creates Hash Values of a given input
def hashMe(msg=""):
    if type(msg)!=str:
        msg = json.dumps(msg,sort_keys=True)  # If we don't sort keys, we can't guarantee repeatability!
        
    if sys.version_info.major == 2:
        return unicode(hashlib.sha256(msg).hexdigest(),'utf-8')
    else:
        return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()

#define elements of BC
class Block:
    def __init__(self,index,data,previousHash):
        self.index = index
        self.data = BHRhash
        self.previousHash = previousHash
        self.hash = self.hashBlock()
#BC hashing function        
    def hashBlock(self):
        hash_list = [self.index,self.data,self.previousHash]
        hash_from_list = hashMe(hash_list)
        return hash_from_list

#prints it's data
def print_data(self):
    print(self.data)

#returns the value of data
def return_data(self):
    return self.data

#genesis block function
def createGenesisBlock():
    return Block(0, "Genesis Block", 0)

#next blocks creation function
def createNextBlock(prevBlock):
    currIndex = prevBlock.index + 1
    currData = BHRhash
    currHash = prevBlock.hash
    return Block(currIndex, currData, currHash)

#checks a hashvalue if it's stored in the Blockchain
def check_patient_hash(blockChain,pat_hash):
    for n in blockChain:
        if return_data(n) == pat_hash:
            return True
        
    return False




############################################################################################################
#
#---------------------------------------Program starts here-------------------------------------------------
#
############################################################################################################

print("")
print("Hello User, to start you need to create your first patient.")
print("First patient details:")

#blockchain hash list
BChashes = []
BHRhash = hashMe("Patient Zero")
blockChain = [createGenesisBlock()]
prevBlock = blockChain[0]
patient_dict = create_patient_dict()
BHRhash = hashMe(patient_dict)
print("Patient Hash: "+ BHRhash) #Evtl. delete in the final version
blockToAdd = createNextBlock(prevBlock)
blockChain.append(blockToAdd)
prevBlock = blockToAdd
print("Block %s has been added to the blockchain!" % (blockToAdd.index))
BChashes.append(blockToAdd.hash)



while_controll = 0
while while_controll == 0:
    print("Options: ")
    print("Nr.1: Add new patient")
    print("Nr.2: Load existing patient data set")
    print("Nr.3: Print Stored Hash Values")
    print("Nr.4: Stop program")
    first_choice = input("Press Number 1-4: ")

    if first_choice == "1":
        patient_dict = create_patient_dict()
        #hashes new information
        BHRhash = hashMe(patient_dict)
        print("Patient Hash: "+ BHRhash) #Evtl. delete in the final version
        blockToAdd = createNextBlock(prevBlock)
        blockChain.append(blockToAdd)
        prevBlock = blockToAdd
        print("Block %s has been added to the blockchain!" % (blockToAdd.index))
        BChashes.append(blockToAdd.hash)
        


    elif first_choice == "2":
        pat_id = select_file()
        patient_dict = load_dict(pat_id)
        BHRhash = hashMe(patient_dict)
        print("Patient Hash: "+ BHRhash)
        if check_patient_hash(blockChain,BHRhash):
            print("Patient data is verified")
            print(patient_dict)
            choice = input("Do you want to change the data? Press (y/n)")
            if choice == "y":
                patient_dict = modify_dict(patient_dict)
                BHRhash = hashMe(patient_dict)
                print("Patient Hash: "+ BHRhash) #Evtl. delete in the final version
                blockToAdd = createNextBlock(prevBlock)
                blockChain.append(blockToAdd)
                prevBlock = blockToAdd
                print("Block %s has been added to the blockchain!" % (blockToAdd.index))
                BChashes.append(blockToAdd.hash)
                save_dict(patient_dict)

        else:
            print("File couldn't be verified with existing blockchain entries")
            choice = input("Do you want to correct the data and verify it again? Press (y/n)")
            if choice == "y":
                patient_dict = modify_dict(patient_dict)
                BHRhash = hashMe(patient_dict)
                print("Patient Hash: "+ BHRhash) #Evtl. delete in the final version
                blockToAdd = createNextBlock(prevBlock)
                blockChain.append(blockToAdd)
                prevBlock = blockToAdd
                print("Block %s has been added to the blockchain!" % (blockToAdd.index))
                BChashes.append(blockToAdd.hash)
                save_dict(patient_dict)
       
    elif first_choice == "3":
        cot = 0
        for n in blockChain:
            print("Block Nr. " + str(cot) + " Hash: ", end="")
            print_data(n)
            cot += 1

    elif first_choice == "4":
        print("Are you sure you want to stop the program? If the Blockchain isn't saved all Patient Data can't be verifyed later")
        choice = input("Press (y/n)")
        if choice == "y":
            break

    else:
        print("Input was invalid")

print("Program is terminated")
print("----------------------------------------------------")
