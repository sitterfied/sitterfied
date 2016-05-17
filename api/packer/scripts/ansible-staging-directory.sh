#!/bin/bash -eux

if [[ $PACKER_BUILDER_TYPE = 'virtualbox-ovf' ]]; then
	USER='vagrant'
else
	USER='ubuntu'
fi

/usr/bin/install -d -o "$USER" -g "$USER" -m 0755 /tmp/packer-provisioner-ansible-local
