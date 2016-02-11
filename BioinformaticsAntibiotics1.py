
# coding: utf-8

# Notebook for First Problem
# This code can later and might be later exported as a python file for reuse by other programs

# In[1]:

import pandas as pd


# In[2]:

#Reading in Data and storing codon to aminoacid mapping in a dictionary.
codonData=pd.read_table("RNA_codon_table_1.txt",sep=" ",header=None)
codonData.head()


# In[3]:

#Defining Function to get Mapping from Pandas dataframe
def getCodonMappings(row,mappings={}):
    mappings[row[0]]=row[1]
#Hashtable to store mappings
geneticCode={}
#Applying function to dataframe to get mappings
codonData.apply(getCodonMappings,mappings=geneticCode,axis=1);#Semicolon suppresses output


# Reading in input file for the problem

# In[4]:

inputFile=open("test.txt")
inputText=inputFile.read()
#Printing out a snippet everything seems fine
print(inputText[0:10])


# In[5]:

#Creating a list of tuples with the start and end coordinate of each codon stored in each tuple.
codonLocationTuples=zip(range(0,len(inputText)-1,3),range(3,len(inputText),3))
outputString=""
for locs in codonLocationTuples:
    codon=(inputText[locs[0]:locs[1]])
    translatedCodon=geneticCode[codon]
    #If we encounter a stop codon we stop translation of genetic code
    if type(translatedCodon) is float:
        break
    else:
        outputString+=geneticCode[codon]
else:
    print("No premature stop codons were encountered. Yayyyy!")
print(outputString[0:10])#printing a snipped to see if everything is ok


# Writing output file. This was kind of easy compared to Java. It would have taken me way longer if I used Java. Nice

# In[6]:

outputFile=open("output.txt",'w')
outputFile.write(outputString)
#The write is not complete unless you close the file properly as in here. Make sure you do that
outputFile.close()
inputFile.close()

