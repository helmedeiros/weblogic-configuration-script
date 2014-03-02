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
        
def savePreviousArguments(managedServerName):
    from java.io import File
    from java.io import FileOutputStream
    from java.util import Properties
    from java.util import Date
    from java.text import SimpleDateFormat
    
    import string
    startToEdit()
    # parameter on the wsdl ant task call
    fileLocation = sys.argv[1].replace("\\","/")
    print "The backup file location is"
    print fileLocation
    try:
        dateFormat = SimpleDateFormat('_d_MMM_yyyy_HH_mm_ss')
        date = Date()
        formattedDate = dateFormat.format(date)
        print formattedDate
    except:
        print "The date cannot be created/formatted"
        
    try:    
        propsFile = File(fileLocation+ managedServerName + formattedDate+"_config.bkp");
        print propsFile.exists()
        if(propsFile.exists() == 0):
            propsFile.createNewFile()
    except:
        print "The file cannot be created on:"
        print propsFile.getAbsoluteFile()
        dumpStack()     
        
    previousProperties = Properties()
    print '===> Saving the  previous arguments - ' + managedServerName
    cd('/Servers/'+managedServerName)
    print "Getting the Classpath"
    classPath = cmo.getServerStart().getClassPath()
    print classPath
    if classPath == None:
        classPath = ""
    previousProperties.setProperty("classPath", classPath)
    print "Saving Arguments to file"
    previousProperties.store(FileOutputStream(propsFile),None)
    print '===> Saved arguments! Please verify the file on:'+ fileLocation + "in" + managedServerName 
        
def backupPreviousClassPath(managedServersToCreate):
    import string
    managedServersList = string.split(managedServersToCreate,"|")
    if len(managedServersList)> 0 and managedServersList[0] != '' :
        for managedServerName in managedServersList:
            try:
                print "Managed Server Name: " + managedServerName
                savePreviousArguments(managedServerName.strip())
            except Exception, e:
               print e
               dumpStack()
    else:
        print "Please verify the value of property managedServersToCreate on WLST configuration file"
            
connStatus = connectToWebLogic()
if connStatus != None:
    backupPreviousClassPath(managedServersToCreate)    
    disconnectFromWebLogic()