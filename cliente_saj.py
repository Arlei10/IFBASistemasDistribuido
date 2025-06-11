
import socket
import time
import random


HOST = '127.0.0.1'
PORT = 65432

SENSOR_ID = "Sensor SAJ"


def start_client():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
          
            client_socket.connect((HOST, PORT))
            print(f"[{SENSOR_ID}] Conectado com sucesso ao servidor em {HOST}:{PORT}")
        except ConnectionRefusedError:
            print(f"[{SENSOR_ID}] Erro: A conexão foi recusada.")
            return

        try:
            while True:
                
                temperatura = round(random.uniform(20.0, 38.0), 1)
                umidade = round(random.uniform(50.0, 75.0), 1)
                
               
                message = f"{SENSOR_ID};{temperatura};{umidade}"
                
               
                client_socket.sendall(message.encode('utf-8'))
                print(f"[{SENSOR_ID}] Dados enviados: Temp={temperatura}°C, Umid={umidade}%")
                
               
                ack = client_socket.recv(1024)
                print(f"[{SENSOR_ID}] Resposta do servidor: {ack.decode('utf-8')}")
                
                
                time.sleep(5)
        except (BrokenPipeError, ConnectionResetError):
            print(f"[{SENSOR_ID}] A conexão com o servidor foi perdida.")
        except KeyboardInterrupt:
            print(f"[{SENSOR_ID}] Encerrando o cliente.")
        finally:
            print(f"[{SENSOR_ID}] Conexão fechada.")

if __name__ == "__main__":
    start_client()