@rem ******************************************************************************
@rem This script is used to set up the VMARGS properties BASED ON THE CONF FILES   
@rem ******************************************************************************
@echo At the first time configure the Classapath 
CALL "%WORKSPACE%\wlst\setWLSEnvironment.cmd"
@echo off
@echo After the classpath configuration call the ANT task.
@echo Execute the Ant Task
ant createVMArgsConfig -buildfile "%WORKSPACE%\build.xml" -Dbuild.env=server -DconfigEnv=%1 -DconfigAction=%2
@echo Ant task executed

:finish
