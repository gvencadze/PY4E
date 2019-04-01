def openfile():
    fname = raw_input("Enter file name: ")
    try:    
        fh = open(fname, 'r')
    except:
        print ("Error opening file", fname)
        quit() 
    return fh

def printit(f):
    for line in f:
        #print line.upper(), #Во всплывающем окне надо написать: words.txt
        print (line.upper().rstrip()) #comment to avoid new line in the end of print


fh = openfile()
printit(fh)

