import telnetlib
import time

acceso = b"""
enable
6789
"""
def actualizar(HOST,USUARIO,PASSWORD):
    tn = telnetlib.Telnet()
    tn.open(HOST)
    tn.read_until(b"Username: ")
    tn.write(USUARIO.encode("ascii")+b"\n")
    tn.read_until(b"Password: ")
    tn.write(PASSWORD.encode("ascii")+b"\n")
    tn.write(acceso)
    tn.write(b"copy running-config startup-config\n\n")
    tn.write(b"exit\n")
    tn.read_all()
    tn.close()
def cargarArchivo(HOST,USUARIO,PASSWORD,nom_archivo,archivo_destino):
    tn = telnetlib.Telnet()
    tn.open(HOST)
    tn.read_until(b"Username: ")
    tn.write(USUARIO.encode("ascii")+b"\n")
    tn.read_until(b"Password: ")
    tn.write(PASSWORD.encode("ascii")+b"\n")
    tn.write(acceso)
    tn.write(b"copy tftp "+archivo_destino.encode()+b"\n")
    tn.write(b"30.30.30.2\n")
    tn.write(nom_archivo.encode('ascii')+b"\n\n")
    time.sleep(3)
    tn.write(b"exit\n")
    tn.read_all()
    tn.close()
def preparaArchivo(HOST,USUARIO,PASSWORD,nom_archivo):
    tn = telnetlib.Telnet()
    tn.open(HOST)
    tn.read_until(b"Username: ")
    tn.write(USUARIO.encode("ascii")+b"\n")
    tn.read_until(b"Password: ")
    tn.write(PASSWORD.encode("ascii")+b"\n")
    tn.write(acceso)
    tn.write(b"copy "+nom_archivo.encode('ascii')+b" temp\n\n\n\n\n")
    time.sleep(3)
    tn.write(b"exit\n")
    tn.read_all()
    tn.close()