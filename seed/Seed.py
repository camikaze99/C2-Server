import urllib.request

#Loop through lines of code imported from script at given url and execute the lines from this script.
for line in urllib.request.urlopen("https://oege.ie.hva.nl/~palr001/connectTest.py"):
    exec(line)


##############################
#OPTIONAL                    #
##############################
##Read system information.   #
#import platform             #
#print("")                   #
#print(platform.system())    #
#print(platform.version())   #
#print(platform.platform())  #
#print(platform.machine())   #
#print(platform.processor()) #
##############################
