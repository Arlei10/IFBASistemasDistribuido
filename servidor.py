import socket
import threading
import time

HOST = '0.0.0.0'
PORT = 65432

def handle_client(conn, addr):
    print(f"[NOVA CONEXÃO] {addr} conectado.")
    try:
        while True:
           
            data = conn.recv(1024)
            if not data: 
                break
            
            
            message = data.decode('utf-8')
            try:
               
                sensor_id, temperatura, umidade = message.split(';')
                
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

               
                print(f"[{timestamp}] [{sensor_id}] Dados recebidos: Temperatura={temperatura}°C, Umidade={umidade}%")
                
               
                conn.sendall(b'ACK: Dados recebidos')
            except ValueError:
                print(f"[AVISO] Dados mal formatados de {addr}: {message}")
    except ConnectionResetError:
        print(f"[CONEXÃO PERDIDA] A conexão com {addr} foi perdida.")
    finally:
     
        print(f"[FIM DA CONEXÃO] {addr} desconectado.")
        conn.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"[ESCUTANDO] Servidor está escutando em {HOST}:{PORT}")
    while True:
        conn, addr = server_socket.accept() 
      
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[CONEXÕES ATIVAS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()