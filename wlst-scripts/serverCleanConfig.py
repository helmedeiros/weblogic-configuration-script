## Added to get the BeanAlreadyExistsException 
from weblogic.descriptor import BeanAlreadyExistsException 

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
        #print e
        
def disconnectFromWebLogic():
    disconnect() 
    exit()

def startToEdit():
    edit()
    startEdit()
    cd('/')  

def saveActivate(managedServerName):
    try:
        save()
        activate()
        print "Managed Server "+managedServerName+" is removed SUCCESSFULLY!"
    except BeanAlreadyExistsException, e1:
        print "(-03) The Bean "+managedServerName+" already exists."
    except Exception, e2:
        print "(-02) Error while trying to save and/or activate =>> "+managedServerName+". Please verify the parameters for that and the error type below."
        print "Error Type:",sys.exc_info()[0]    
        
def removesManagedServer(managedServerName):   
    startToEdit()     
    ### Shutdown the Managed Server - NOTE: Need the Node Manager up and running
    print "Assuming the server is started."
    print "Shutdown the Managed Server - NOTE: Need the Node Manager up and running"
    try:
        shutdown(managedServerName)
    except Exception, e:
       print "(-06) Cannot shutdown the server using the Node Manager. Maybe already shutdown."     
    
    print "Removing the Managed Server " + managedServerName
    ### Remove the Managed Server
    cd('/Servers/'+managedServerName)
    cmo.setCluster(None)
    cmo.setMachine(None)
    
    # Remove references to Server Bean
    editService.getConfigurationManager().removeReferencesToBean(getMBean('/Servers/'+managedServerName))
    
    # Destroy the Server Bean
    cd('/')
    cmo.destroyServer(getMBean('/Servers/'+managedServerName))

def removeClusters(clusterName): 
        startToEdit()
        editService.getConfigurationManager().removeReferencesToBean(getMBean('/Clusters/'+clusterName))
        cd('/')
        cmo.destroyCluster(getMBean('/Clusters/'+clusterName))

def configureManagedServers(managedServersToCreate):
    import string
    managedServersList = string.split(managedServersToCreate,"|")
    if len(managedServersList)> 0 and managedServersList[0] != '' :
        for managedServerName in managedServersList:
            try:
                print "Managed Server Name: " + managedServerName
                print "Start to remove"
                removesManagedServer(managedServerName)  
                print "Save and Activate the changes."      
                saveActivate(managedServerName)
            except Exception, e:
                print "(-04) Cannot remove the "+managedServerName+". Please verify the parameters for that and the error type below."
                print "Error Type:",sys.exc_info()[0]    
                print e
    else:
        print "Please verify the value of property managedServersToCreate on WLST configuration file"

def configureClusters(clustersToCreate):
    import string
    clustersList = string.split(clustersToCreate,"|")
    if len(clustersList)> 0 and clustersList[0] != '' :
        for clusterName in clustersList:
            try:
                print "Cluster Name: " + clusterName
                print "Start to create"
                removeClusters(clusterName+"")
                print "Save and Activate the changes."    
                save()
                activate()
            except Exception, e:
                print "(-05) Cannot remove the "+clusterName+". Please verify the parameters for that and the error type below."
                print "Error Type:",sys.exc_info()[0],sys.exc_info()[1] 
                print e
    else:
        print "Please verify the value of property clustersToCreate on WLST configuration file"     

connStatus = connectToWebLogic()
if connStatus != None:           
    print "SERVER CLEAN CONFIGURATION RUNNING... "
    configureManagedServers(managedServersToCreate)
    configureClusters(clustersToCreate)
    disconnectFromWebLogic()