# weblogic-configuration-script

weblogic-configuration-script is a [Jython](http://www.jython.org/) set of scripts that abstract creation, management and monitor of Weblogic Server domains. It uses de [WLST - WebLogic Scripting Tool](http://docs.oracle.com/cd/E15051_01/wls/docs103/config_scripting/using_WLST.html) under the roof, creating an abstraction layer and a two-ways interface to easily integrate with tools like [jenkins](http://jenkins-ci.org/) into automatic proccesses.


## Dependencies

**[Jython](http://www.jython.org/)**
**[WebLogic](http://www.python.org/)**
**[WLST](http://docs.oracle.com/cd/E15051_01/wls/docs103/config_scripting/using_WLST.html)**
**[Apache ant](http://ant.apache.org/)**

## Usage

Start your project development with **right foot** for that you can procceed with **[weblogic installation](http://onlineappsdba.com/index.php/2011/12/11/how-to-install-weblogic-12c-1211-on-mac/)**, after that set everything using automated scripts, and let all your collegues with the same configuration pattern and evolve it together, fixing what's needed from there. 

During the WebLogic installation wrote down the Weblogic Server Credentials, so you can configure it in the properly configuration property files, that are inside /conf.

After that create or double the file inside /conf specifying in file prefix, the abreviation for a given environment.

To run configuration just run the properly command inside cmds.