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

def startManagedServer(managedServerName):
    try:
        ### Start the Managed Server - NOTE: Need the Node Manager up and running
        print "Start the Managed Server - NOTE: Need the Node Manager up and running"
        print "Starting "+managedServerName
        start(managedServerName)
        print managedServerName + " started."
    except Exception, e2:
        print "(-02) Error while trying to start the Server =>> "+managedServerName+". Please verify the parameters for that and the error type below."
        print "Error Type:",sys.exc_info()[0]
        #print sys.exc_info()[0], sys.exc_info()[1]
        print e2
    
def saveActivate(managedServerName):
### Activate the changes
    try:
        save()
        activate()
        print "Managed Server "+managedServerName+" created SUCCESSFULLY!"
        startManagedServer(managedServerName)
    except BeanAlreadyExistsException, e1:
        print "(-03) The Bean "+managedServerName+" already exists."
    except Exception, e2:
        print "(-02) Error while trying to save and/or activate =>> "+managedServerName+". Please verify the parameters for that and the error type below."
        print "Error Type:",sys.exc_info()[0]
        #print sys.exc_info()[0], sys.exc_info()[1]
        #print e
        
def createManagedServer(managedServerName):
    import string
    startToEdit()
    listenPortEnabled    = eval(addPropertySeparator(managedServerName)+"listenPortEnabled").strip()
    listenPortNumber     = eval(addPropertySeparator(managedServerName)+"listenPortNumber").strip()
    listenAdress         = eval(addPropertySeparator(managedServerName)+"listenAdress").strip()
    javaCompiler         = eval(addPropertySeparator(managedServerName)+"javaCompiler").strip()
    serverArguments      = eval(addPropertySeparator(managedServerName)+"serverArguments").strip()
    serverClassPath      = eval(addPropertySeparator(managedServerName)+"serverClassPath").strip()
    #sslListenPortEnabled = eval(addPropertySeparator(managedServerName)+"sslListenPortEnabled").strip()
    #sslListenPort        = eval(addPropertySeparator(managedServerName)+"sslListenPort").strip()
    #wldfDiagnosticVolume = eval(addPropertySeparator(managedServerName)+"wldfDiagnosticVolume").strip()
    targetMachineName    = eval(addPropertySeparator(managedServerName)+"targetMachineName").strip()
    targetCluster        = eval(addPropertySeparator(managedServerName)+"targetCluster").strip()
#    customKeyStore       = eval(addPropertySeparator(managedServerName)+"customKeyStore").strip()
#    customKeyStorePath   = eval(addPropertySeparator(managedServerName)+"customKeyStorePath").strip()
#    customKeyStoreType   = eval(addPropertySeparator(managedServerName)+"customKeyStoreType").strip()
#    customKeyStoreEncryptConfigFilePath = eval(addPropertySeparator(managedServerName)+"customKeyStoreEncryptConfigFilePath").strip()
#    customKeyStoreEncryptSecretFilePath = eval(addPropertySeparator(managedServerName)+"customKeyStoreEncryptSecretFilePath").strip()
#    customKeyStoreEncryptCredential     = eval(addPropertySeparator(managedServerName)+"customKeyStoreEncryptCredential").strip()
#    customTrustKeyStorePath             = eval(addPropertySeparator(managedServerName)+"customTrustKeyStorePath").strip()
#    customTrustKeyStoreType             = eval(addPropertySeparator(managedServerName)+"customTrustKeyStoreType").strip()
#    customTrustKeyStoreEncryptConfigFilePath = eval(addPropertySeparator(managedServerName)+"customTrustKeyStoreEncryptConfigFilePath").strip()
#    customTrustKeyStoreEncryptSecretFilePath = eval(addPropertySeparator(managedServerName)+"customTrustKeyStoreEncryptSecretFilePath").strip()
#    customTrustKeyStoreEncryptCredential     = eval(addPropertySeparator(managedServerName)+"customTrustKeyStoreEncryptCredential").strip()
#    serverPrivateKeyAlias                    = eval(addPropertySeparator(managedServerName)+"serverPrivateKeyAlias").strip()
#    serverPrivateKeyCredential               = eval(addPropertySeparator(managedServerName)+"serverPrivateKeyCredential").strip()
#    serverPrivateKeyConfigFilePath           = eval(addPropertySeparator(managedServerName)+"serverPrivateKeyConfigFilePath").strip()
#    serverPrivateKeySecretFilePath           = eval(addPropertySeparator(managedServerName)+"serverPrivateKeySecretFilePath").strip()
    
### Create the Managed Server
    cmo.createServer(managedServerName)

## SSL port configuration if needed 
#    if string.lower(sslListenPortEnabled) == "true":
#        cd('/Servers/' + managedServerName +'/SSL/'+ managedServerName )
#        cmo.setEnabled(true)
#        cmo.setListenPort(long(sslListenPort))
#    else:
#        if string.lower(sslStatus) == "false":
#            cd('/Servers/' + managedServerName +'/SSL/'+ managedServerName )
#            cmo.setEnabled(false)
            
    cd('/Servers/' + managedServerName)        
    cmo.setListenPort(long(listenPortNumber))
    cmo.setJavaCompiler(javaCompiler)
    cmo.setMachine(getMBean('/Machines/'+targetMachineName))
    cmo.setListenAddress(listenAdress)
    
#### Security configurations
#    cmo.setKeyStores(customKeyStore)
#    cmo.setCustomIdentityKeyStoreFileName(customKeyStorePath)
#    cmo.setCustomIdentityKeyStoreType(customKeyStoreType)
#    setEncrypted('CustomIdentityKeyStorePassPhrase', customKeyStoreEncryptCredential, customKeyStoreEncryptConfigFilePath, customKeyStoreEncryptSecretFilePath)
#    cmo.setCustomTrustKeyStoreFileName(customTrustKeyStorePath)
#    cmo.setCustomTrustKeyStoreType(customTrustKeyStoreType)
#    setEncrypted('CustomTrustKeyStorePassPhrase', customTrustKeyStoreEncryptCredential, customTrustKeyStoreEncryptConfigFilePath, customTrustKeyStoreEncryptSecretFilePath)    
#
#    ### SSL properties
#    cmo.setIdentityAndTrustLocations('KeyStores')
#    cmo.setServerPrivateKeyAlias(serverPrivateKeyAlias)
#    setEncrypted('ServerPrivateKeyPassPhrase', serverPrivateKeyCredential, serverPrivateKeyConfigFilePath, serverPrivateKeySecretFilePath)
    # clusterName receive the cluster mode if exists or "None" value. 
    targetCluster = targetCluster and targetCluster or None
    if targetCluster != None and targetCluster != '' :
        clusterObj = getMBean('/Clusters/'+ targetCluster)
        cmo.setCluster(clusterObj)
    activate()
    print '===> Created Managed Server - ' + managedServerName

    print '===> Add arguments and Classpath to  - ' + managedServerName
    startEdit()
    cd('/Servers/'+managedServerName+'/ServerStart/'+managedServerName)
    cmo.setArguments(serverArguments)
    cmo.setClassPath(serverClassPath)

    cd('/Servers/'+managedServerName+'/SSL/'+managedServerName)
#    if string.lower(sslStatus) == "true":
#        cmo.setEnabled(true)
#    else:
#        if string.lower(sslStatus) == "false":
#            cmo.setEnabled(false)
        
  #  cd('/Servers/'+managedServerName+'/ServerDiagnosticConfig/'+managedServerName)
  #  cmo.setWLDFDiagnosticVolume(wldfDiagnosticVolume)
 
def createClusters(clusterName): 
        startToEdit()
        cmo.createCluster(clusterName)
        cd('/Clusters/'+clusterName)
        cmo.setClusterMessagingMode('unicast')
    
def configureClusters(clustersToCreate):
    import string
    clustersList = string.split(clustersToCreate,"|")
    if len(clustersList)> 0 and clustersList[0] != '' :
        for clusterName in clustersList:
            try:
                print "Cluster Name: " + clusterName
                print "Start to create"
                createClusters(clusterName+"")
                print "Save and Activate the changes."    
                save()
                activate()
                print "Cluster "+clusterName+" successfully created" 
            except Exception, e:
                print "(-07) Cannot create the "+clusterName+". Please verify the parameters for that and the error type below."
                print "Error Type:",sys.exc_info()[0]
                print e
    else:
        print "Please verify the value of property clustersToCreate on WLST configuration file"
        
def configureManagedServers(managedServersToCreate):
    import string
    managedServersList = string.split(managedServersToCreate,"|")
    if len(managedServersList)> 0 and managedServersList[0] != '' :
        for managedServerName in managedServersList:
            try:
                print "Managed Server Name: " + managedServerName
                print "Start to create"
                createManagedServer(managedServerName.strip())
                print "Save and Activate the changes."    
                saveActivate(managedServerName.strip())
            except Exception, e:
                print "(-06) Cannot create the "+managedServerName+". Please verify the parameters for that and the error type below."
                print "Error Type:",sys.exc_info()[0]
    else:
        print "Please verify the value of property managedServersToCreate on WLST configuration file"
            
connStatus = connectToWebLogic()
if connStatus != None:
    print "SERVER CONFIGURATION RUNNING....."
    configureClusters(clustersToCreate)
    configureManagedServers(managedServersToCreate)
    disconnectFromWebLogic()