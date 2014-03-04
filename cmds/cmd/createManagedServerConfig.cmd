@rem *************************************************************************
@rem This script is used to set up the Managed Servers BASED ON THE CONF FILES   
@rem *************************************************************************
@echo At the first time configure the Classapath 
CALL "%WORKSPACE%\cmds\setWLSEnvironment.cmd"
@echo off
@echo After the classpath configuration call the ANT task.
@echo Execute the Ant Task
ant createManagedServerConfig -buildfile "%WORKSPACE%\build.xml" -Dbuild.env=server -DconfigEnv=%1 -DconfigAction=%2
@echo Ant task executed

:finish