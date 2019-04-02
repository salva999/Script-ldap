import ldap
import csv
import ldap.modlist as modlist
import base64
import sys

try:
    #Abrir conexión
    l=ldap.initialize("ldap://rajoy.salvador.gonzalonazareno.org:389")
    #Usuario y contraseña del usuario con privilegios para crear objetos
    username = "cn=admin,dc=salvador,dc=gonzalonazareno,dc=org"
    contraseña = "admin"

    #Autentificación con el usuario admin
    l.simple_bind(username, contraseña)
except ldap.SERVER_DOWN:
    print('Error de conexión')
    sys.exit()

try:
    #Leer fichero csv de manera estructurada
    with open ('usuarios.csv', newline='') as csvfile:
        r = csv.reader(csvfile, delimiter=':')
        uidNumber=2000
        for i in r:
            #Creación del usuario
            dn = "cn=%s, dc=salvador, dc=gonzalonazareno, dc=org" % i[3]
            attrs={}
            attrs['objectClass'] = [b"inetOrgPerson",b"posixAccount",b"ldapPublicKey"]
            attrs['cn'] = bytes(i[3], 'utf-8')
            attrs['uid'] = bytes(i[3], 'utf-8')
            attrs['mail'] = bytes(i[2], 'utf-8')
            attrs['sn']= base64.b64encode(bytes(i[1], 'utf-8'))
            attrs['sshPublicKey'] = bytes(i[4], 'utf-8')
            attrs['loginShell'] = b"/bin/bash"
            attrs['homeDirectory'] = b"/home/"+bytes(i[3], 'utf-8')
            attrs['gidNumber'] = b"2000"
            attrs['uidNumber'] = bytes(str(uidNumber), 'utf-8')
            uidNumber=uidNumber+1

            #Ajuste del diccionario para que sea una entrada ldap
            ldif = modlist.addModlist(attrs)
            #Añade el usuario
            l.add_s(dn,ldif)
    print("Usuarios añadidos")

except ldap.STRONG_AUTH_REQUIRED:
    print('Error de Usuario o Contraseña')
    sys.exit()
except FileNotFoundError:
    print('Error no exite el fichero usuarios.csv')
    sys.exit()
except ldap.ALREADY_EXISTS:
    print('Error, usuarios existentes')
    sys.exit()

try:
    #Leer fichero csv para equipos
    with open ('equipos.csv', newline='') as csvequipos:
        n=csv.reader(csvequipos, delimiter=':')
        for e in n:
            #Creacion de equipos
            dn="ipHostNumber=%s, dc=salvador, dc=gonzalonazareno, dc=org" % e[1]
            equipos={}
            equipos['objectClass'] = [b"ipHost",b"ldapPublicKey",b"device"]
            equipos['cn'] = bytes(e[0], 'utf-8')
            equipos['ipHostNumber'] = bytes(e[1], 'utf-8')
            equipos['sshPublicKey'] = bytes(e[2], 'utf-8')
            #Ajuste del diccionario para que sea una entrada ldap
            ldifequipos = modlist.addModlist(equipos)
            #Añade los equipos
            l.add_s(dn,ldifequipos)
    print("Equipos añadidos")
except FileNotFoundError:
    print('Error no exite el fichero equipos.csv')
    sys.exit()
except ldap.ALREADY_EXISTS:
    print('Error, equipos existentes')
    sys.exit()

#Desconecta y libera los recursos de ldap
l.unbind_s ()
