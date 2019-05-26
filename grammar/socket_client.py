# -*- coding: utf-8 -*-
# author:xls
"""
    socket通信,client端
"""
import socket

IP_PORT = ('127.0.0.1',9999)

sk = socket.socket()

sk.connect(IP_PORT)

while True:
    inp = input('请输入你要发送的信息： ').strip()
    if not inp:
        continue
    sk.sendall(inp.encode())

    if inp == "exit":
        print("通信结束！")
        break
    server_reply = sk.recv(1024).decode()
    print(server_reply)
sk.close()