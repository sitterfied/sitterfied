#!/bin/bash -eux

apt-get -y autoremove
apt-get -y clean

# empty out the temporary authorized keys
> /root/.ssh/authorized_keys
> /home/ubuntu/.ssh/authorized_keys
