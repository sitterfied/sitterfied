Deployment
==========

This role creates a script which is used as part of the deployment
pipeline. This script is placed under _/usr/local/bin/_ and facilitates
the process of swapping out instances in an Auto Scaling Group for newer
instances.

Naming Conventions
------------------

To keep things consistent across all of the Beatport teams, the script assumes
a naming convention for the AWS resources. For starters, the container names,
environment names, and the deployment ID values match what has been established
in our
[shared infrastructure](../../../docs/aws-shared-infrastructure.md)
documentation.

If an AMI ID is not specified explicitly, the script will default to the
latest available **AMI** based on the format:

    ${container}-baked-${project}-${deployment_id}

The **Elastic Load Balancer** is expected to have the format:

    ${container}-${environment}-${project}

...the corresponding **Auto Scaling Group** is expected to have the same format:

    ${container}-${environment}-${project}

...and the **Launch Configuration** is expected to have the format:

    ${container}-${environment}-${project}-${deployment_id}

Example
-------

To swap out the production instance of the Jenkins master server, you
would issue the following command:

    $ deploy-image --region=us-west-1 --container=common --environment=prod --project=jenkins-master --iam=deployment-pipeline

Run `deploy-image --help` to get all of the command details and options.
