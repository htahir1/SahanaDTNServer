Following steps are to be taken in order to properly install and configure the DTN Server

1. sudo apt-get update
2. sudo apt-get install build-essential
3. sudo apt-get install autoconf
4. sudo apt-get install libavahi-compat-libdnssd-dev
5. manually install dep
	i. sudo dpkg -i libdb4.6_4.6.21-16_i386.deb
	ii. sudo dpkg -i libdb4.6-dev_4.6.21-16_i386.deb
6. sudo apt-get install libexpat1-dev
7. sudo apt-get install mono-devel
8. sudo apt-get install tcl8.4
9. sudo apt-get install tcl8.4-dev
10. sudo apt-get install tcllib
11. sudo apt-get install tclreadline
12. sudo apt-get install tclx8.4-dev
13. sudo apt-get install zlib1g-dev
14. sudo apt-get install libxerces-c28
15. sudo apt-get install libxerces-c2-dev
16. sudo apt-get install db4.7-util
17. download berkeley db from http://www.oracle.com/technetwork/database/database-technologies/berkeleydb/downloads/index-082944.html
18. extract
19. get root access
20. enter the build_unix directory in extracted folder of berkeleyDB
21. enter the following commands:
	i. ../dist/configure
	ii. make
	iii. make install

22. Make a new directory called dtn2 in the home folder.
23. Install Mercurial: sudo apt-get install mercurial
24. Located in the dtn2 directory, download oasys using mercurial:
	hg clone http://dtn.hg.sourceforge.net/hgweb/dtn/oasys


25. Install oasys:
	-cd oasys
	./build-configure.sh
	CC=gcc CXX=g++ ./configure
	make
	make install

26. Located in the dtn2 directory, download DTN2 using mercurial:
	hg clone http://dtn.hg.sourceforge.net/hgweb/dtn/DTN2

27. Install DTN2:
	- cd DTN2
	- ./build-configure.sh
	- CC=gcc CXX=g++ ./configure -C
	- make
	- make install

---------CONFIGURATION----------

1. In the dtn2 directory created above, make a new folder:
	- mkdir foldername

2. Copy the dtn.conf file from DTN2/daemon/dtn.conf to the newly created folder
	- cp DTN2/daemon/dtn.conf /home/dtn2/foldername

3. Replace the dtn.conf file with dtn.conf here: https://github.com/htahir1/SahanaDTNServer
	- the local EID (endpoint id) is currently set to dtn://dtn-a.dtn/me2"
	- find and replace with the EID of your choice, if you feel like. 

4. Initializing the Database
	- go to the dtnd directory: cd /home/dtn2/DTN2/daemon
	- initialize the DB by running this command: dtnd -c /home/dtn2/foldername/dtn.conf --init-db
	- folloing statements would display in the terminal 

		[1429210766.492644 /dtnd notice] random seed is 492637
		[1429210766.492930 /dtnd notice] DTN daemon starting up... (pid 4719)
		[1429210766.529830 /dtnd notice] initializing persistent data store
		[1429210766.529958 /dtn/storage notice] creating new database directory /home/dtn2/celltoserv/db
		[1429210767.035431 /dtnd notice] closing persistent data store

	- run the daemon using the following command, always
		- dtnd -c /home/dtn2/foldername/dtn.conf



---------SQLite Installation--------

1. sudo apt-get install sqlite3
2. sudo apt-get install libsqlite3-dev

---------Sending/Receiving----------

1. For Sending
a. Open a new terminal and naviagate to the /home/dtn2/DTN2/apps/dtnsend# directory
b. Type the dtnsend command (details of which can be found in "/home/dtn2/DTN2/doc/manual/man_dtnsend.html")

	- dtnsend -s dtn://dtn-a.dtn/me2/prophet/ -d dtn://dtn-a.dtn/me2/ -t m -p "create"

4. For Receiving:
	- Goto this directory: /home/dtn2/DTN2/apps/dtnrecv
	- Replace the following files with the ones from this link: https://github.com/htahir1/SahanaDTNServer
		dtnrecv	
		dtnrecv.1	
		dtnrecv.c	
		dtnrecv.d	
		dtnrecv.o

a. Open a new terminal and naviagate to the /home/dtn2/DTN2/apps/dtnrecv# directory
b. Type the dtnrecv command (details of which can be found in "/home/dtn2/DTN2/doc/manual/man_dtnrecv.html")

	- ./dtnrecv dtn://dtn-a.dtn/me2/

5. To make any future editions possible, replace the 'Makefile' in /home/dtn2/DTN2/apps/ with the one here: https://github.com/htahir1/SahanaDTNServer

6. To make sure the data Received is properly inserted in the Sahana Eden Server download the SahanaInterface.py in /home/dtn2/DTN2/apps/dtnrecv from https://github.com/htahir1/SahanaDTNServer

--------Sahana Eden Deployment-----

1. Install Python and all the related important libraries using the following commands:
	- sudo apt-get install python-lxml
	- sudo apt-get install python-shapely
	- sudo apt-get install python-imaging
	- sudo apt-get install python-dateutil
	- installing the latest version of ReportLab
		- wget --no-check-certificate https://pypi.python.org/packages/source/r/reportlab/reportlab-3.1.44.tar.gz
		- tar zxvf reportlab-3.1.44.tar.gz
		- cd reportlab-3.1.44
		- python setup.py install

2. Clone web2py from GitHub
		- git clone --recursive https://github.com/web2py/web2py.git

3. Clone Sahana Eden from GitHub
		- git clone https://github.com/flavour/eden.git

4. Edit ../eden/modules/templates/000_config.py file
	- Comment out the "#FINISHED_EDITING_CONFIG_FILE = False" line
	- Save file

5. Go to ../web2py directory
6. Run the following command:
	- python web2py.py

7. Enter a password in the web2py web framwork and dont forget it!

8. After you click on the 'Start Server', a browswer window will open showing you the main web2py interface.

9. Click on the 'My Apps tab', Select 'eden'

10. Sahana Eden Humanitarian Management Platform page will open, proceed accordingly then. 
