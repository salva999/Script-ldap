# Script-ldap
Script para poblar ldap

Los script estan escritos en python3

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
