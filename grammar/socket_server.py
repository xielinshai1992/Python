# -*- coding: utf-8 -*-
# author:xls
"""
    多线程socket服务器,支持多client连接
"""

import socket
import threading

# def link_handler(link, client):
#     print("服务器开始接受来自[%s:%s]的请求...."% (client[0],client[1]))
#     while True:
#         client_data = link.recv(1024).decode()
#         if client_data == "exit":
#             print("结束与[%s:%s]的通信...."%(client[0],client[1]))
#             break
#         print("来自[%s:%s]的客户端向你发来信息：%s"%(client[0], client[1], client_data))
#         link.sendall('服务器已收到你的信息'.encode())

IP_PORT = ('127.0.0.1',9999)
sk = socket.socket()
sk.bind(IP_PORT)
sk.listen(5)
print('启动socket服务，等待客户端连接...')

# while True:
#     conn,address = sk.accept()
#     t = threading.Thread(target=link_handler,args=(conn, address))
#     t.start()

#单线程socket
conn, address = sk.accept()
while True:    # 一个死循环，直到客户端发送‘exit’的信号，才关闭连接
    client_data = conn.recv(1024).decode()
    if client_data == "exit":
        print("通信结束!")
        break
    print("来自%s的客户端向服务器发来信息：%s"% (address,client_data))

    conn.sendall('服务器已经收到你的信息了！'.encode())

conn.close()