###
### Author: Sherali Ozodov
### Course: CSc 110
### Description: This program encrypts the lines of a text file, and it first 
### ask the user to write a file to encrypt. It saves the encrypted version of the 
### text file to a file named encrypted.txt. The program encrypts an input file 
### by re-arranging the lines of the input file, based on indexes retrieved from 
### calling randint. The function also writes an index file. This file will contain
### the corresponding indexes of each line in the encrypted file. The number on 
### each line of the file is the line number that each shuffled line was on in 
### the original program. 

import random
def encryp(file_input,open_file,write_file,write_file_index):
    ''' This function first opens the the file written by the user,then
    it generated random numbers. The program encrypts an input file 
    by re-arranging the lines of the input file, based on indexes retrieved from 
    random numbers. 
    file_input is an input that asks user to write the name of a file
    open_file opens the file written by user.
    write_file opens the file 'encrypted.txt'.
    write_file_index opens the file 'index.txt'.
    '''
    random.seed(125)
    encr = []
    encr_2=[]
    index = []
    for line in open_file:
        encr.append(line)
        encr_2.append(line)
    ## it is gonna append original indexes of text file selected by the user to new_list    
    new_list=list(range(0,len(encr)))
    count = 0
    while count != 5*len(encr):
        r = random.randint(0, len(encr_2)-1)
        r_2= random.randint(0, len(encr_2)-1)
        a=encr[r]
        encr[r]=encr[r_2]
        encr[r_2]=a
        ## it is gonna swap indexes based on the random numbers generated
        b=new_list[r]
        new_list[r]=new_list[r_2]
        new_list[r_2]=b
        count += 1 
    for n in encr:
        write_file.write(str(n))
        index.append(n)
    for ii in new_list:
        write_file_index.write(str(ii+1) + '\n')  
def main():
    file_input=input('Enter a name of a text file to encrypt:\n')
    open_file = open(file_input, 'r')
    write_file = open('encrypted.txt', 'w')
    write_file_index = open('index.txt', 'w')
    encryp(file_input,open_file,write_file,write_file_index)
    open_file.close()
    write_file.close()
    write_file_index.close()
    
main()

    
