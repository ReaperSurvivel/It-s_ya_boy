import fileinput, os.path, datetime

x = 1



def Notetaking():
    date = str(datetime.datetime.now())
    file = input("Type the filename for the file:")
    tempname = str(file)
    
    txt = input("Type whatever you want using <br> for new lines:")

    if os.path.isfile(file):
        
        # Read in the file
        with open(file, 'r') as file :
          filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(r'<p></p>', r'<p>'+ date +": "+ txt +'<br></p> <p></p>')
        
        
        # Write the file out again
        with open(tempname, 'w') as file:
          file.write(filedata)
        
        file.close()
        
    else:
        print("Incorrect filename, please try again.")
        
while (x == 1):
    Notetaking()
    x == 0
    ans = input("Do you wanna take another note?")
    if (ans == "Yes"):
        x == 1
    if (ans == "Y"):
        x == 1
    else:
        print("Shutting Down")
        quit()
