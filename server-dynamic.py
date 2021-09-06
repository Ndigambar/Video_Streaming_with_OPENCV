import socket 
import time
import threading

client_r_port=[]
client_s_port=[]
r_session=[]
s_session=[]
sock_s=[]
sock_r=[]
ip=''
c=-1
c1=-1
n=int(input("No of clients"))

for i in range(n):
    client_r_port.append(2024+i)

for i in range(n*n):
    client_s_port.append(3024+i)




def recieve(i):
    while True:
        data=r_session[i].recv(10000000)
        time.sleep(2)
        for j in range(n):
            data1=data
            c1=c1+1
            s_session[c1].send(data1)

            



for i in range(n):    
    sock_r.append(socket.socket())
    sock_r[i].setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)
    sock_r[i].bind((ip, client_r_port[i]))
    sock_r[i].listen()
    temp_r, r_addr = sock_r[i].accept()
    r_session.append(temp_r)

    for j in range(n):
        c=c+1
        sock_s.append(socket.socket())
        sock_s[c].setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)
        sock_s[c].bind((ip, client_s_port[c]))
        sock_s[c].listen()
        temp_s, s_addr = sock_s[c].accept()
        s_session.append(temp_s)

    recv_f=threading.Thread(target=recieve, args=[i])
    recv_f.start()
