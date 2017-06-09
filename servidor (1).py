import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1",50001)) # direccion ip y puerto, solamente asignado
s.listen(5)
Lista = []
Lista2 = []
def crear(alist,blist):
	while True:
		sock, addr = s.accept()
		nombre = sock.recv(1024) # recibe 1024 bites de datos, no puede recibir mas
		alist.append(sock)
		blist.append(nombre)
		CL = threading.Thread(target = streaming, args=(nombre,sock))
		CL.start()

def streaming(nombre,sock):
	while True:
		datos = sock.recv(1024)
		print(nombre, ':' , datos)


crear(Lista,Lista2)
	
