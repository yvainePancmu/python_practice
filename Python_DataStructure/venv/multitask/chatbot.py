import threading
import socket

def recv_message(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print('接收到的消息:{}'.format(recv_data[0].decode('utf-8')))


def send_message(udp_socket,dest_addr):
    while True:
        send_data = input('请输入要发送的消息：')
        udp_socket.sendto(send_data.encode('utf-8'),dest_addr)

def main():
    """完成udp聊天器的整体控制"""
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    localaddr = ('',8081)
    udp_socket.bind(localaddr)

    dest_ip = input('请输入对方的ip:')
    dest_port = int(input('请输入对方的port:'))
    dest_addr = (dest_ip,dest_port)

    t_recv = threading.Thread(target=recv_message,args=(udp_socket,))
    t_send = threading.Thread(target=send_message,args=(udp_socket,dest_addr))

    t_recv.start()
    t_send.start()

if __name__ == '__main__':
    main()
