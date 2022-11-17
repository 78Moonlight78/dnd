import socket


# class client`s responsible for clients message and connecting with main server
class Client:
    def __init__(self, ip, port):
        self.cli = socket.socket()
        self.cli.connect((ip, port))

    # function responsible for connecting with server,establishes a connection with a server
    def connect(self):
        try:
            message = self.cli.recv(1024).decode('utf-8')
        except Exception as exp:
            print(f'ERROR:{str(exp)}')
            exit()
        if message == 'You`re connected!All correct':
            self.getting()
        else:
            exit()

    # function sending information to server
    def sender(self, text):
        self.cli.send(text.encode('utf-8'))

    # function get information from user and into server
    def getting(self):
        while True:
            try:
                response = self.cli.recv(1024)
                print(response.decode("utf-8"))
                break
            except Exception:
                pass


if __name__ == "__main__":
    Client("127.0.0.1", 6000).connect()
