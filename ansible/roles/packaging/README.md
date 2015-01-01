Packaging
=========

This role sets up the build tree in preparation to package the Beatport
API X application. It also creates shell scripts which can be run inside
of the source code directory in order to generate a package.

Overview
--------

In order to generate deb packages, there are a bunch of metadata files
required to be in place under a particular build directory hierarchy.
Applying this role will create that entire build tree for you under
_/usr/local/src/_ and populate the metadata files.

Additionally, build scripts are put under _/usr/local/bin/_ to assist in
converting the raw source code from our Git repository into a properly
versioned package.

### Versioning

Until we start officially managing release versions for the project, the
packages will use the following convention for their package versions.

    PACKAGE_VERSION=$(printf '0.%s.%s' "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)")

* The **major** number is hard-coded to "0" for now, so if/when we issue
  an official v1.0 release, it will be a newer release according to the
  package manager.

* The **minor** number is based on the number of commits, so this will
  always be increasing.

* The **micro** number is the short Git revision SHA1, so you can easily
  reference the exact commit each package was generated from.

Example
-------

To generate a package for the API X application, you should launch the
Vagrant developement environment virtual machine and run the build script.

    $ cd beatport-api-x/
    $ vagrant up
    $ vagrant ssh
    $ cd /opt/beatportapi/
    $ /usr/local/bin/generate-api-server-package
    $ ls beatport-api-server_*.deb
    beatport-api-server_0.313.98fa609.deb

_Note that the build scripts will set up a fakeroot environment and should
not be run by the root user._

Package Contents
----------------

To view the contents of a deb package, run the following:

    $ dpkg -c <path-to-package>.deb

This package creates a system user named "beatport" (if one does not
already exist) and contains the Django application code with all static
assets (images, css, javascript, etc.). The actual configuration and
management of Nginx, and uWSGI are handled elsewhere.
