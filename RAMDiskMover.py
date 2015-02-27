import os,time,shutil, sys

PATH='C:\\Users\\miphilli\\Documents\\RAMDISK'
DESTINATION='C:\\Users\\miphilli\\Documents\\FireCaptures'
WAIT=10
#
# Main
#
print "Waiting for files to finish recording..."
print
while True:
    for R,D,F in os.walk(PATH):
            for f in F:
                try:
                    #shutil.move(os.path.join(R,f),os.path.join(DESTINATION,os.path.split(R)[-1],f))
                    shutil.move(os.path.join(R,f),os.path.join(DESTINATION,f))
                    print f+" is OK for copy to "+DESTINATION
                except:
                    e = sys.exc_info()[0]
                    print e
                    print f+" is recording, waiting "+str(WAIT)+" sec to test again before moving..."
                    time.sleep(WAIT)
                        
