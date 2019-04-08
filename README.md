# Script-ldap
Script para poblar ldap

Script en python3

Para realizar el script en python para poblar ldap, instalamos el paquete siguiente:

`sudo apt install python-ldap`

Instalamos pip3 y el paquete necesario que nos permite importar el módulo ldap en python3:

`sudo apt install python3-pip`

`pip3 install pyldap`

Los Script y los ficheros csv deben estar en el mismo directorio.

Para ejecutar los Script:

Para añadir los usuarios y los equipos:

`python3 poblar.py`

Para eliminar los usuarios y los equipos:

`python3 delete.py`

Para la autentificación de los usuarios de ldap configuramos el fichero /etc/ssh/sshd_config:

`AuthorizedKeysCommand Ruta del Script.sh`
`AuthorizedKeysCommandUser nobody`

Permisos para el Script:

`chown root. script.sh`
`chmod 755 script.sh`

Reiniciamos servicio:

`systemctl restart sshd.service`
