import tftpy
from telnet import preparaArchivo

def descargarArchivo(HOST,USUARIO,PASSWORD,nom_archivo,archivo_destino):
    preparaArchivo(HOST,USUARIO,PASSWORD,nom_archivo)
    client = tftpy.TftpClient(HOST, 69)  
    client.download("temp", archivo_destino)