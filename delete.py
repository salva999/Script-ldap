import ldap
import csv
import ldap.modlist as modlist
import os
import sys

#Abrir conexión
l=ldap.initialize("ldap://rajoy.salvador.gonzalonazareno.org:389")

#Usuario y contraseña del usuario con privilegios para crear objetos
username = "cn=admin,dc=salvador,dc=gonzalonazareno,dc=org"
contraseña = "admin"

#Autentificación con el usuario admin
l.simple_bind(username, contraseña)

#Pregunta para decidir borrar usuarios y equipos
respuesta = input('¿Borrar Usuarios? S/N ')
if respuesta == 'S' or respuesta == 's':
    #Leer fichero csv de manera estructurada
    with open ('usuarios.csv', newline='') as csvfile:
        r = csv.reader(csvfile, delimiter=':')
        for i in r:
            #Creamos el comando para borrar los usuarios y ejecutamos el comando
            deleteDN = 'ldapdelete -D "cn=admin, dc=salvador, dc=gonzalonazareno, dc=org" -w admin -h localhost -p 389 "cn=%s, dc=salvador, dc=gonzalonazareno, dc=org"' % i[3]
            os.system(deleteDN)
    print('Usuarios Borrados o inexistentes')
respuesta2 = input('¿Borrar equipos? S/N ')
if respuesta2 == 'S' or respuesta2 == 's':
    #Leer fichero csv de manera estructurada
    with open ('equipos.csv', newline='') as csvfile:
        r = csv.reader(csvfile, delimiter=':')
        for i in r:
            #Creamos el comando para borrar los usuarios y ejecutamos el comando
            deleteDN = 'ldapdelete -D "cn=admin, dc=salvador, dc=gonzalonazareno, dc=org" -w admin -h localhost -p 389 "ipHostNumber=%s, dc=salvador, dc=gonzalonazareno, dc=org"' % i[1]
            os.system(deleteDN)
    print('Equipos Borrados o inexistentes')
#Termina el programa
else:
    l.unbind_s()
    sys.exit()

l.unbind_s()
