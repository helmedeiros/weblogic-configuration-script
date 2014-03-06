#!/bin/sh
#*****************************************************************************
# This script is used to set up the VMARGS properties BASED ON THE CONF FILES   
#*****************************************************************************
WORKSPACE=$(cd ../../$(dirname $0) && pwd);

echo "#*********STARTING ENVIRONMENT CONFIGURATION**********#";
source $WORKSPACE/cmds/sh/setWLSEnv.sh;
echo "#*********FINISHED ENVIRONMENT CONFIGURATION**********#";

echo "#*********STARTING MANAGED SERVER VM ARGS CONFIGURATION**********#";
echo "Execute the ant task";
ant createVMArgsConfig -buildfile "$WORKSPACE/build.xml" -Dbuild.env=server -DconfigEnv=$1 -DconfigAction=$2
echo "Finished the ant task execution";
echo "#*********FINISHED MANAGED SERVER  VM ARGS CONFIGURATION**********#";

exit 1;