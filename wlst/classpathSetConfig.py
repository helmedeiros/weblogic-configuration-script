#### Utils Functions#################

## Added to get the BeanAlreadyExistsException 
from weblogic.descriptor import BeanAlreadyExistsException 

def addPropertySeparator(nameToAdd):
    separator = "_"
    return nameToAdd + separator

def connectToWebLogic():
    print '################################################################'
    print '    Trying to connect the Server: '+ wlHost + ':' + wlPort
    print '################################################################'
    ### Connect to the Administration Server
    try:
        connect(wlUsername,wlPassword,'t3://'+wlHost+':'+wlPort)
        return true
    except Exception, e:
        print "(-01) Error while trying to connect in: t3://"+wlHost+":"+wlPort+". Please verify the parameters."
 
def disconnectFromWebLogic():
    disconnect() 
    exit()
    
def startToEdit():
    edit()
    startEdit()
    cd('/')            
    
def saveActivate():
### Activate the changes
    try:
        save()
        activate()
    except Exception, e2:
        print "(-02) Error while trying to save and/or activate. Please verify the parameters for that and the error type below."
        print "Error Type:",sys.exc_info()[0]
        #print sys.exc_info()[0], sys.exc_info()[1]     
       
def setClassPath(managedServerName):
    import string
    startToEdit()
    print '===> Add classpath to  - ' + managedServerName
    serverClassPath      = eval(addPropertySeparator(managedServerName)+"serverClassPath").strip()
    startEdit()
    cd('/Servers/'+managedServerName+'/ServerStart/'+managedServerName)
    cmo.setClassPath(serverClassPath)
    cd('/Servers/'+managedServerName+'/SSL/'+managedServerName)
        
def configureClassPath(managedServersToCreate):
    import string
    managedServersList = string.split(managedServersToCreate,"|")
    if len(managedServersList)> 0 and managedServersList[0] != '' :
        for managedServerName in managedServersList:
            try:
                print "Managed Server Name: " + managedServerName
                print "Start to change"
                setClassPath(managedServerName.strip())                
                print "Save and Activate the changes."    
                saveActivate()
            except Exception, e:
               print e
               dumpStack()
    else:
        print "Please verify the value of property managedServersToCreate on WLST configuration file"
            
connStatus = connectToWebLogic()
if connStatus != None:    
    configureClassPath(managedServersToCreate)
    disconnectFromWebLogic()