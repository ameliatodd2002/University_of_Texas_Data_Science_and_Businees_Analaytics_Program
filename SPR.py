# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 00:48:39 2022

@author: Amelia Todd

Instructions:
    #type in command line pip install censusgeocode
"""

import censusgeocode as cg
#censusgeocode takes csv input with adresses and provides a new csv with previous information and a census tract number for each address
import pandas as pd

ogPath = 'data/addresses.csv'
#path to find input csv file
resPath = 'data/results.csv'
#path to put result csv file from censusgeocode
batchSize = 9999
#amount given to censusgeocode at a time

def batchRes(path):
    #program starts by passing ogpath to this function as path
    res = cg.addressbatch(path)
    #using function created below to send csv file input to census geocode and recieve output
    #uses ogpath as argument
    add = []
    #initializing list for addresses
    tr = []
    #initializing list for censustract
    sf = []
    #initializing list for state code
    cf = []
    #initializing list for county code
    b = []
    #initializing list for block code
    
    for r in res:
        #going through each adress and appending each relevant column to each list
        add.append(r['address'])
        #appending address for each entry
        tr.append(r['tract'])
        #appending census tract for each entry
        sf.append(r['statefp'])
        #appending state code label for each entry
        cf.append(r['countyfp'])
        #appending county code label for each entry
        b.append(r['block'])
        #appending each block label for each entry
    data = {'address': add, 'tract code': tr, 'state code': sf, 'county code': cf, 'block': b}
    #creating a dictionary with keys for each column we want with corresponding list
    df = pd.DataFrame(data)
    #using pandas to create a dataframe using the dictionary created above
    df.to_csv(resPath, mode='a')
    #creating csv file from the dataframe and sending to result path
    return 0

def batchProcess(path):
    #function to interact with API (censusgeocde)
    source_path = path
    #uses ogpath bc that is what is passed through it as argument in previous funtion
    for i,chunk in enumerate(pd.read_csv(source_path, chunksize=batchSize)):
        #reading csv using ogpath(source_path); defining chunksize as the batchSize defined at top of program (goes through 9999 enries at a time)
        #using for loop to go through each entry in the csv input fie and enumerating through it to keep track of entry number
        chunk.to_csv('data/subBatches/chunk{}.csv'.format(i), index=False)
        #for each bath, this returns the output into a new csv file with the route defined
        #this will create folder named data w folder inside named subBatches with outputs for each batch
        batchRes('data/subBatches/chunk{}.csv'.format(i))
        #passes the resulting folder back to the original function for it to sort through and organize
    return 0

if __name__ == '__main__':
    batchProcess(ogPath)
    #ogpath is passed through first function as an argument to provide path to find input csv file (ogpath defined at beginning)
