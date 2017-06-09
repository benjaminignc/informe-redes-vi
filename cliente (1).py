import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",50001))

i = raw_input("Ingrese nombre: ")
s.send(i)


while True:
	datos = raw_input("Ingrese datos: ")
	s.send(datos)

s.close()
