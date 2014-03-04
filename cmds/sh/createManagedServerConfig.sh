#!/bin/sh
#*****************************************************************************
# This script is used to set up the Managed Servers BASED ON THE CONF FILES   
#*****************************************************************************
WORKSPACE=$(cd ../../$(dirname $0) && pwd);

echo "#*********STARTING ENVIRONMENT CONFIGURATION**********#";
source $WORKSPACE/cmds/sh/setWLSEnv.sh;
echo "#*********FINISHED ENVIRONMENT CONFIGURATION**********#";

echo "#*********STARTING MANAGED SERVER CONFIGURATION**********#";
echo "Execute the ant task";
ant createManagedServerConfig -buildfile "$WORKSPACE/build.xml" -Dbuild.env=server -DconfigEnv=$1 -DconfigAction=$2
echo "Finished the ant task execution";
echo "#*********FINISHED MANAGED SERVER CONFIGURATION**********#";

exit 1;