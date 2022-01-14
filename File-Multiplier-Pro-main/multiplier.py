import os

def open_file(filename,mode_to_open):
    with open(r'{}'.format(filename),mode_to_open) as f:
        file_data=f.read()
        f.close()
    return file_data

def multiply_file(filename,number_of_copies=3,mode_of_writing='w',mode_of_reading='r'):
    part_of_file=filename.split('.')
    filetype=part_of_file[1]
    name_of_file=part_of_file[0]
    data=open_file(filename,mode_of_reading)
    for copy in range(number_of_copies):
        with open(name_of_file+' Copy ({})'.format(copy+1)+'.'+filetype,mode_of_writing) as f:
            f.write(data)
            f.close()

def remove_copies(filelocation,filename):
    files=[]
    parts_of_file=filename.split('.')
    fname=parts_of_file[0]
    for f in os.listdir(filelocation):
        if fname in f:
            files.append(f)
    for i in files:
        if 'Copy' in i:
            os.remove(filelocation+'\\'+i)
    

if __name__=="__main__":
    for option in ['1.File with Text (e.g. .py,.txt,.dat)','2.Media Files (e.g. .png,.jpg,.mp3)','3.Remove Copies','\n']:
        print(option)
    opt=int(input('Enter Option Number :'))
    if opt==1:
        file_to_open=input('Enter Filename to multiply :')
        copy_no=int(input('Enter Number of Copies: '))
        multiply_file(file_to_open,copy_no,'w','r')
    elif opt==2:
        file_to_open=input('Enter Filename to multiply :')
        copy_no=int(input('Enter Number of Copies: '))
        multiply_file(file_to_open,copy_no,'wb','rb')
    elif opt==3:
        print('Note:- This will remove all the copies\n')
        filelocation=input('Enter Original File Location (without including filename):')
        file_to_remove=input('Enter File Name:')
        remove_copies(filelocation,file_to_remove)
