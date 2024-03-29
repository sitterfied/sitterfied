#!/bin/sh -eux

if [[ $PACKER_BUILDER_TYPE = 'virtualbox-ovf' ]]; then
	dd if=/dev/zero of=/EMPTY bs=1M
	rm -f /EMPTY
	# Block until the empty file has been removed, otherwise, Packer
	# will try to kill the box while the disk is still full and that's bad
	sync
fi
