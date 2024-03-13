import socket
import threading
import os

HOST = '127.0.0.1'
PORT = 65432

def send_message(message, file_size):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Envie o tamanho do arquivo
    s.sendall(str(file_size).encode())

    # Envie o nome do arquivo
    filename = 'meu_arquivo.txt'
    s.sendall(filename.encode())

    # Envie os dados do arquivo
    with open(filename, 'rb') as f:
      data = f.read()
      s.sendall(data)

    # Receba dados do servidor em um loop
    while True:
      data = s.recv(1024)
      if not data:
        break
      print('Received from server:', data.decode())

def main():
  file_size = os.path.getsize('meu_arquivo.txt')
  thread = threading.Thread(target=send_message, args=("Hello, server!", file_size))
  thread.start()

if __name__ == '__main__':
  main()

print('Client closed')