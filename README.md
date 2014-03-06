# weblogic-configuration-script

weblogic-configuration-script is a [Jython](http://www.jython.org/) set of scripts that abstract creation, management and monitor of Weblogic Server domains. It uses de [WLST - WebLogic Scripting Tool](http://docs.oracle.com/cd/E15051_01/wls/docs103/config_scripting/using_WLST.html) under the roof, creating an abstraction layer and a two-ways interface to easily integrate with tools like [jenkins](http://jenkins-ci.org/) into automatic proccesses.


## Dependencies

**[Jython](http://www.jython.org/)**

**[WebLogic](http://www.python.org/)**

**[WLST](http://docs.oracle.com/cd/E15051_01/wls/docs103/config_scripting/using_WLST.html)**

**[Apache ant](http://ant.apache.org/)**


## Usage

Start your project development with right foot. Proceed with **[weblogic installation](http://onlineappsdba.com/index.php/2011/12/11/how-to-install-weblogic-12c-1211-on-mac/)**, after that set everything using automated scripts, and let all your collegues with the same configuration pattern so you all can evolve it together, fixing what's needed from there.

1. Execute the managed server configuration using scripts:

	```shell
	cd $WL_CONFIG_SCRIPT/cmds/sh/
	./createManagedServerConfig.sh LOCAL SET
	```
	
## Setup

In order to run it locally you'll need a basic server setup.

1. Install **[WebLogic](http://onlineappsdba.com/index.php/2011/12/11/how-to-install-weblogic-12c-1211-on-mac/)**;
2. Access **[WebLogic Admin Server](http://localhost:7001/console)**;
3. Log into it with an admin credentials set during the install;
4. Open the conf/LOCAL_wlst.properties and fill it with your expected configuration;


## Contributing

1. Fork it!
2. Create your feature branch: ```git checkout -b my-new-feature```
3. Commit your changes: ```git commit -m 'Add some feature'```
4. Push to the branch: ```git push origin my-new-feature```
5. Submit a pull request :D
