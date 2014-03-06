# weblogic-configuration-script

weblogic-configuration-script is a [Jython](http://www.jython.org/) set of scripts that abstract creation, management and monitor of Weblogic Server domains. It uses de [WLST - WebLogic Scripting Tool](http://docs.oracle.com/cd/E15051_01/wls/docs103/config_scripting/using_WLST.html) under the roof, creating an abstraction layer and a two-ways interface to easily integrate with tools like [jenkins](http://jenkins-ci.org/) into automatic proccesses.


## Dependencies

**[Jython](http://www.jython.org/)**

**[WebLogic](http://www.python.org/)**

**[WLST](http://docs.oracle.com/cd/E15051_01/wls/docs103/config_scripting/using_WLST.html)**

**[Apache ant](http://ant.apache.org/)**


## Usage

Start your project development with right foot. Proceed with **[weblogic installation](http://onlineappsdba.com/index.php/2011/12/11/how-to-install-weblogic-12c-1211-on-mac/)**, after that set everything using automated scripts, and let all your collegues with the same configuration pattern so you all can evolve it together, fixing what's needed from there.

1. Install weblogic:
	
	1. Download Weblogic Software wls1212_dev.zip and extract to folder 
	(~/oracle/weblogic/mw) – This directory is called Middleware Home (MW_HOME)

	2. Set JAVA_HOME, MW_HOME, and USER_MEM_ARGS	
	```shell
		export JAVA_HOME=/System/Library/Frameworks/JavaVM.framework/Versions/1.6/Home 
		export MW_HOME=~/oracle/weblogic/mw 
		export USER_MEM_ARGS="-Xmx1024m -XX:MaxPermSize=256m"
	```
	Note: Change middleware home directory (MW_HOME) to directory in which you have unzipped WebLogic zip file

	3. Configure Weblogic by running configure.sh
	```shell
		cd $MW_HOME
		./configure.sh
	```

	4. Set WLS Environment file (setWLSEnv.sh)
	```shell
		. $MW_HOME/wlserver/server/bin/setWLSEnv.sh
	```

	5. Create WebLogic Domain using GUI
	```shell
		$MW_HOME/wlserver/common/bin/config.sh
	```

	On Welcome screen, select Create a new WebLogic Domain
	Follow domain creation screens
	On warning “CFGFWK – 60893: The selected JDK version doesn’t match the jdk version pattern” click OK
	On create domain screen, when progress bar reaches 100% note down Domain Location and Admin Server URL

	Note: Directory /atul/oracle/weblogic/mw/user_projects/domains/base_domain is represented by variable $DOMAIN_HOME

	6. Start WebLogic Domain
	```shell
		cd $DOMAIN_HOME/bin
		./startWebLogic.sh
	```

	7. Access WebLogic Admin Server as http://hostname:admin_port/console
	http://localhost:7001/console

2. Configure managed server using scripts:

	```shell
		cd $WL_CONFIG_SCRIPT/cmds/sh/
		 ./createManagedServerConfig.sh LOCAL SET
	```