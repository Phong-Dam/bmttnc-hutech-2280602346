import socket
import ssl
import threading

# Server information
server_address = ('localhost', 12345)

def receive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print("Receive:", data.decode('utf-8'))
    except:
        pass
    finally:
        ssl_socket.close()
        print("Connection closed.")

# Create socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Create SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE  # Không kiểm tra chứng chỉ máy chủ (không khuyến nghị cho production)

# Wrap the socket with SSL
ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')

# Connect to server
ssl_socket.connect(server_address)

# Start a thread to receive data from the server
receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))
receive_thread.start()

# Send data to the server
try:
    while True:
        message = input("Enter message: ")
        ssl_socket.send(message.encode('utf-8'))
except KeyboardInterrupt:
    print("\nClient interrupted.")
finally:
    ssl_socket.close()
