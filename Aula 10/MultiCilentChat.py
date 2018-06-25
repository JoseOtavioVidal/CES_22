# To create a multiple client chat, we have to use thread to allow multiple client, on each thread is a client
# So, we just have to modify alittle the multithread server example on the class notes
import socket
import threading
from time import ctime

def listenToClient(self, client, address):
    size = 1024
    while True:
        try:
            data = client.recv(size)
            if data:
                # Set the response to echo back the recieved data
                strdata = data.decode('utf-8')
                print(strdata)
                client.send((ctime() + ' ' + strdata).encode('utf-8'))
            else:
                raise error('Client disconnected')
        except:
            client.close()
            print("Exception")
            return False
    client.close()

if __name__ == "__main__":
    # inicialize the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 5000

    s.bind((host, port))
    s.listen(5)
    print("Server started")

    while True:
        #Take the client
        client, address = s.accept()
        print("Got connection from %s", address)
        threading.Thread(target=listenToClient, args=(client, address)).start()