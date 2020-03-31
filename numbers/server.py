import socket

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together
    print("Server on host " , host , "port " , port)

    # configure how many clients the server can listen to simultaneously
    server_socket.listen(2)
    conn_1, address_1 = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address_1))

    conn_2, address_2 = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address_2))

    score = [0,0]

    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data_1 = conn_1.recv(1024).decode()
        data_2 = conn_2.recv(1024).decode()
    
        reply_1 = "You: " + str(data_1) + ", your opponent: " + str(data_2)
        reply_2 = "You: " + str(data_2) + ", your opponent: " + str(data_1)
        
        if int(data_1) > int(data_2):
            reply_1 += ". You win! :-)"
            reply_2 += ". You loose! :-(" 
            score[0]+=1
        elif int(data_1) < int(data_2):
            reply_1 += ". You loose! :-(" 
            reply_2 += ". You win! :-)" 
            score[1]+=1
        else:
            reply_1 += ". Nobody wins."
            reply_2 += ". Nobody wins."
        
        conn_1.send(reply_1.encode())  # send data to the client
        conn_2.send(reply_2.encode())  # send data to the client

    #conn.close()  # close the connection

if __name__ == '__main__':
    server_program()
