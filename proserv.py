#server side program in tcp
import socket
server_name='AAIT'
host='0.0.0.0'
port= 12341
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()
print(f'Server listening on {host}:{port}')
client_socket, client_address = server_socket.accept()
done=False
while not done:
    name = client_socket.recv(1024).decode()
    number = client_socket.recv(1024).decode()
    num = int(number)
    print(f'the client name is : {name}')
    print(f'the server name is : {server_name}')
    if (num>100):
        done=True
    else:
        numbr=input("Enter number between 1 and 100 : ")
       # nme=input("enter server name name: ")
        client_socket.send(server_name.encode('utf-8'))
        client_socket.send(numbr.encode('utf-8'))

        print(f'the recieved number is:{num}')
        print(f'the input number is:{numbr}')

        print(f'the sum of the recieved and the input number is:{num+int(numbr)}')
client_socket.close()
server_socket.close()