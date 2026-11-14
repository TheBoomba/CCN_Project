import socket
import threading
from player_class import Player


HOST = "127.0.0.1"  
PORT = 65432  

# Blocks until the two players are connected
def create_session(serversocket):
    serversocket.listen()
    p1 = serversocket.accept()
    player1 = Player(p1[0], p1[1][0], p1[1][1])
    p2 = serversocket.accept()
    player2 = Player(p2[0], p2[1][0], p2[1][1])
    print("hi")
    return (player1, player2)

# Sends the recieves a message and decides what to do with it
def client_session(player1, player2):
    with (player1.Socket):
        while True:
            data = player1.Socket.recv(1024)
            print(data.decode())
            if data.decode()[0] == "P":
                new_message = data.decode()[1:].encode()
                player2.Socket.sendall(new_message)
            if not data:
                break


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    p1, p2 = create_session(s)
    thread1 = threading.Thread(target=client_session,args=[p1, p2],daemon=True)
    thread2 = threading.Thread(target=client_session,args=[p2, p1],daemon=True)
    thread1.start()
    thread2.start()

    while True:
        if input() == "exit":
            break
    
            



            