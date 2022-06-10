###
### Author: Sherali Ozodov
### Course: CSc 110
### Description: This program takes the name of a text file and index file,
### and then it will decrypt the text. The program reads in these two files, 
### and using the information stored within them, it will put the contents 
### back in the original order. The decrypted file should be saved to a file 
### named decrypted.txt. 

def decrypt(file_input,open_file,file_input_2,open_file_index,write_file):
    '''This function asks the user to write the name of encrypted file 
    and encrypted file index.Then these two files are opened, and the information
    in these file are stored on two lists. After reading the file information, 
    the decrypted file is put on 'decrypted.txt' file.
    '''
    open_file_list=[]
    index_list=[]
    for line in open_file.readlines():
        line=line.split('\n')
        open_file_list.append(line[0])
    for ind in open_file_index.readlines():
        ind=ind.split('\n')
        index_list.append(ind[0])
    new_list_dec = [0]*len(index_list)
    for v in range(len(open_file_list)):
        index=int(index_list[v])-1
        new_list_dec[index]=open_file_list[int(v)]
    for i in new_list_dec:
        write_file.write(i+'\n')
    open_file.close()
    open_file_index.close()
    write_file.close()
    
def main():
    file_input=input('Enter the name of an encrypted text file:\n')
    open_file=open(file_input,'r')
    file_input_2=input('Enter the name of the encryption index file:\n')
    open_file_index=open(file_input_2,'r')
    write_file=open('decrypted.txt' , 'w')
    decrypt(file_input,open_file,file_input_2,open_file_index,write_file)  
main()

