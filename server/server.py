import socket
import os
import redis


# class of server
class Server:
    def __init__(self, ip, port):

        self.ser = socket.socket()
        self.ser.bind(
            (ip, port)
        )

        self.ser.listen(1)
        self.my_redis = redis.Redis(host="my-db", port=6379)
        self.working = False


    # function sending information to user
    def sender(self, user, text):
        user.send(text.encode('utf-8'))

    # function of starting work with user
    def start_server(self):
        while True:
            user, addr = self.ser.accept()
            print(f'Client connected:\n\tIP: {addr[0]}\n\t Port:{addr[1]}')
            self.get_from_user(user)

    # function get information from user and work with it
    def get_from_user(self, user):
            self.sender(user, 'You`re connected! Good luck!')
            self.working = False

            while self.working:
                try:
                    information = get_information()
                    user.send(information)
                except:
                    pass
            self.working = False


def get_information():
    return b""

if __name__ == "__main__":
    Server('127.0.0.1', 6000).start_server()
