Packer Templates
================

This directory houses some [Packer](http://packer.io/) templates for
generating Amazon Machine Images (AMI) for use within the Beatport
infrastructure.

Overview
--------

There are three image types:

1. The foundation images produce just minimal a OS installation.
2. The base images produce an image containing all dependencies for each
   application type.
3. The baked images have everything completely installed and are the
   golden images that can be launched as part of the deployment pipeline.

To ensure consistency between development and production environments,
we'd like to control the generation of our foundation Ubuntu images rather
than rely on builds from third parties. That said, until we have the
foundation image process fully sorted out, we'll start off by using the
upstream [Ubuntu Cloud Images](http://cloud-images.ubuntu.com/) .

Usage
-----

### AMI Builder

Assuming that you already have Packer installed, you'll additionally need
to have your AWS credentials exported into the appropriate environment
variables:

    $ export AWS_ACCESS_KEY="<your-access-key-here>"
    $ export AWS_SECRET_KEY="<your-secret-key-here>"

Then you can clone this repo, change into the packer directory and build
any of the available templates.

    $ git clone https://github.com/sitterfied/sitterfied.git
    $ cd sitterfied/packer/

There are helper scripts in the packer directory to handle the entire
process for you, all you have to do is run them with the proper arguments
(run them with no arguments to print out a help message). Here are some
example usages where you'd replace the arguments with the desired values:

    $ ./generate-foundation-image REGION
    $ ./generate-base-image -r REGION -c CONTAINER -p PROJECT
    $ ./generate-baked-image -r REGION -c CONTAINER -p PROJECT

Packer will launch an AMI as specified in the corresponding template,
perform the provisioning tasks, take a snapshot and then output the
details for the newly-created AMI. It does not manage the removal of old
AMIs or snapshots.
