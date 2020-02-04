import socket

raddr 0 ('127.0.0.1', 50001)
laddr = ('127.0.0.1', 50005)
create_connection = socket.create_connection(raddr, laddr)
