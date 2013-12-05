General system architecture
============================

The System consists of two main pieces - an api server running django, and responsible for serving content json and some registration pages, and the main client application which is an ember.js application.


Getting The api installed
====================


1. Install the pip package manager
  Most distrobutions come with easy_install - an obsolute python package manager. Either using your systems package manager (apt/yum/brew) or easy_install, install pip.
  on debian this would be:
	  # aptitude install python-pip


2.  Install Virtual Environment and virtual env wrapper (optional)
	Virtual Envrionment/wrapper are tools that keep different python applications isolated from each other. Because we're installing a bunch of specific versions of packages, this is pretty useful to keep your sanitiy intact.
	on debian:

		$ sudo apt-get install python-virtualenv

	    $ sudo apt-get install virtualenvwrapper
		(see http://roundhere.net/journal/virtualenv-ubuntu-12-10/ for specific instructions on ubuntu, although you no longer need to modify your bashrc)


3. Install the Database
   The api uses postgres to store data.

	on debian:
	$ sudo apt-get install postgresql-dev-X.Y postgresql-contrib


4. If you installed Virtual Evn and the wrapper, create the virtual evrionment
   $ mkvirtualenv sitterfied

5. Install the python dependencies
   The python packages in requirements.txt will be automatically installed on the production server on a push. For devlopment install the packages in  requirements-dev.txt, which come with a lot of debugging/profiling tools.

   $ pip install -r requirements-dev.txt


6. Create the local database and user
   Postgres comes with a couple handy shell tools - I prefer to use those. You can also do this in raw sql if you prefer.
   $ createuser sitterfied  -P -- use sitterfied as password
   $ createdb sitterfied -O sitterfied --encoding=UTF8

7. Create the inital databse tables
   Use django's sync db and south's migrate to create the inital tables. Syncdb is a one shot deal, and south is a tool for managing database versions

   $ python manage.py syncdb
   $ python manage.py migrate


8. Start the server
   $ python manage.py runserver

If all went well, the server should now be running. browse to localhost:8000 and you should see the welcome page.


Building the client
===================
For devlopment, the client is built on demand using requireJs. This leads to long load times and is not ideal for production.

So to get around that, we precompile the application and serve it as a single js file.
The single largest bottleneck is the inital download of this js file. The build process will handle minification, but ensure you serve the file gzipped.

The tools for building the application live in the build folder - running the build.sh file will kick it all off

Ensure you have both node and java installed on your system

Once you run the build.sh file -

1. Using R.js to combine the files
  This process is run by node - it's possible to use rhino via java, but it is several orders of magnatude slower to do so.
  The r.js file contains the logic to to the build process, and build level settings are controlled in the app.build.js file.

2. Minifying the file with the closure compiler
   This process is java - the google closure complier will minify and optimize javascript. This is optional, but greatly recommended.

the final output (sitterfied-min.js) is placed into sitterfied/static_source/js


Building the client side templates
==================================

The client side templates are precompiled and included in the combined sitterfied.js file. Less http requests

There's a python script at the base of the application (templates.py) that will watch the folders containing the templates,
and recompile them after every change.

to get this script running you must install node and two dependencies - watchdog, a python library to watch your file system, and node-ember-precompile, to actually precompile the templates.

install watchdog via
 $ pip install watchdog

install ember-precompile via
$ sudo npm -g install https://github.com/gabrielgrant/node-ember-precompile/archive/compat-rc2.zip


Updating the database schema
============================
As you develop you will probably need to update the database schema.
We do this using south. Make you changes to the models.py file and then

$ python manage.py schemamigration app --auto

This will automatically generate a migration file which will move your schema.

To apply:

$ python manage.py migrate

This will automtically be done on production when you deploy


Deploying
====================================

We use dotcloud for hosting - so to start with, install the dotcloud CLI

$ pip install dotcloud

I've been keeping the complied sitterfied.js application out of git because there's very little value in version controlling it.
When you push, make sure to use rsync as a deployment method and it will move the updated build along with the django code.

$ dotcloud push --rync
