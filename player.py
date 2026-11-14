import socket
import threading
from player_class import Player

HOST = "127.0.0.1"  
PORT = 65432  


# Used to send messages to either server or player
def server_session(p1):
    while True:
        message = input("Type your message to the server: ")
        location = input("Send to server or other player [S/P]: ")
        if location == "S":
            s.send_game_message(message)
        elif location == "P":
            s.send_player_message(message)


# Prints out message form server
def server_listening(p1):
    while True:
        data = p1.Socket.recv(1024)

        print(f"Received {data.decode()!r}")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as Socket:
    Socket.connect((HOST, PORT))
    local_ip, local_port = Socket.getsockname()
    s = Player(Socket, local_ip, local_port)

    thread = threading.Thread(target=server_session, args=[s], daemon=True)
    thread1 = threading.Thread(target=server_listening, args=[s], daemon=True)

    thread.start()
    thread1.start()

    # Random waiting statement
    while True:
        w = 3