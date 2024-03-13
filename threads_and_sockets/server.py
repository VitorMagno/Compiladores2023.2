import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def handle_client(conn, addr):
  with conn:
    print('Connected by', addr)
    while True:
      data = conn.recv(1024)
      if not data:
        break
      print('Received:', data.decode())

def main():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))

    s.listen()

    while True:
      conn, addr = s.accept()
      thread = threading.Thread(target=handle_client, args=(conn, addr))
      thread.start()

if __name__ == '__main__':
  main()

print('Socket closed')