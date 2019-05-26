# -*- coding: utf-8 -*-
# author:xls
"""
    socketserver模块实现多线程网络服务器
"""

import socketserver

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        conn = self.request
        conn.sendall('欢迎访问socketserver服务器！'.encode())
        while True:
            data = conn.recv(1024).decode()
            if data == "exit":
                print("断开与%s的连接！" % (self.client_address,))
                break
            print("来自%s的客户端向你发来信息：%s" % (self.client_address, data))
            conn.sendall(('已收到你的消息<%s>' % data).encode())

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',9999),MyServer)
    print("启动socketserver服务器！")
    server.serve_forever()