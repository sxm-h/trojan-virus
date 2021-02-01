import socket
import os
import threading

DISCONNECT_MESSAGE = "!DISCONNECT"
FORMAT = "UTF-8"
HOST = "192.168.0.12"
PORT = 5050
ADDR = (HOST, PORT)
HEADER=64

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)


print("[LISTENING] Waiting for connections...")

server.listen()

def send(msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' *(HEADER - len(send_length))
	conn.send(send_length)
	conn.send(message)

while True:
	conn, addr = server.accept()
	print(f"[NEW CONNECTION] {addr}")

	run = True

	while run:
		command = input(">>")
		send(command)
		msg_length = int(conn.recv(HEADER))
		print(conn.recv(msg_length).decode(FORMAT))
	break
			


