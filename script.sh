#!/bin/sh
ldapsearch -x -h localhost '(&(objectClass=posixAccount)(uid='"$1"'))' 'sshPublicKey' | sed -n '/^ /{H;d};/sshPublicKey:/x;$g;s/\n *//g;s/sshPublicKey: //gp'
