#!/bin/bash -eux

if [[ $PACKER_BUILDER_TYPE = 'virtualbox-ovf' ]]; then
	apt-get -y remove chef chef-zero
fi
