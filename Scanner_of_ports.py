"""
Autor Parfait TOLEFO
e-mail parfaittolefo23@gmail.com
tel: +229 61474698/ +229 52422809
"""
import socket,sys
while 1:
    try:
        site=sys.argv[1]
        demande=sys.argv[2:]
    except:
        print("Veuillez renseigner un nom de site valable\n")
        sys.exit((1))
    if len(demande)==0:
        demande=range(1,1000)
    if len(site)<=1:
        print("Veuillez renseigner un nom de site valable\n")
        sys.exit((1))  
    print("**************** Scannage en cours *******************")
    for ports in demande:      
        try:
            ports=int(ports)
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((site,ports))
            print("\n{} --> ouvert".format(ports))
            s.close()
        except socket.error:
            print("\n{} --> fermer".format(ports))
            pass