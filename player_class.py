import socket

# Class used for the players, mostly used to keep track of attributes
class Player:
    def __init__(self, Socket, IP, port):
        self.Socket = Socket
        self.IP = IP
        self.Port = port


    def send_player_message(self, message):
        sending_message = "P" + message
        self.Socket.sendall(sending_message.encode())

    def send_game_message(self, message):
        sending_message = "S" + message
        self.Socket.sendall(sending_message.encode())