import os
import hashlib
import socket
import pika
import getpass

user_list = []
user_list.append(('admin','6371295ff936e8fae98f8ee80475bee3dc0e461754cdf5b6cce836648a83cf25'))
friend_list = []

def message_socket(name,port):
        ip = socket.gethostname()
        print('1')
        ip = socket.gethostbyname(ip)
        print('2')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('3')
        s.bind((ip,port))
        print('4')
        s.listen()
        print('5')
        connection, addr = s.accept()
        print('6')
        print(userlist[port - 8000])
        while True:
                msg = connection.recv(4096).decode()
                if msg == '/end':
                        break
                send_msg = input('msg:')
                connection.send(send_msg.encode())
        connection.close()
        s.close()

def message(name,port):
        pika_host = pika.ConnectionParameters('localhost')
        pika_conect = pika.BlockingConnection(pika_host)
        channel = pika_conect.channel()
        print('ok')

def message_home():
        global friend_list
        friend_list_str = '\n'.join(friend_list)
        send_user = input(friend_list_str,'\n\n/add')
        if send_user == '/add':
                port = input('what is port')

def Home(username,port):
        while True:
                global user_list
                do = input('Here is Home\n\n1:change profile\n2:send_message\n3:news\n4:exit\n\n')
                if do == '1':
                        nameorpass = input('What will you change?\n\n1:username\n2:password\n\n')
                        if nameorpass == '1':
                                new_username = input('new name:')
                                oldname,oldpass = user_list[port - 8000]
                                user_list[port - 8000] = (new_username,oldpass)
                        if nameorpass == '2':
                                new_password = getpass.getpass('new password:')
                                retype = getpass.getpass('retype:')
                                if new_password == retype:
                                        oldname,oldpass = user_list[port - 8000]
                                        new_password = hashlib.sha256(new_password.encode()).hexdigest()
                                        user_list[port - 8000] = (oldname,new_password)
                                        print('success')
                                elif not new_password == retype:
                                        print('wrong')

                if do == '2':
                        message_home()
#                if do == '3':
                if do == '4':
                        start()
def login(name,port):
        #os.system('cls')
        print('Hello! ' + name)
        print("\nYou'r port is",port)
        Home(name,port)

def sign_in():
        global user_list
        #os.system('cls')
        username = str(input('username:'))
        password = str(input('password:'))
        pass_hash = hashlib.sha256(password.encode()).hexdigest()
        if (username,pass_hash) in  user_list:
                port = user_list.index((username,pass_hash)) + 8000
                login(username,port)
        else:
                os.system('cls')
                print('Wrong username or password')

def sign_up():
        global user_list
        os.system('cls')
        username = str(input('new_name:'))
        password = str(getpass.getpass('new_pass:'))
        retype = str(getpass.getpass('retype:'))
        if password == retype:
                pass_hash = hashlib.sha256(password.encode()).hexdigest()
                user_list.append((username,pass_hash))
                print('OK')
        else:
                print('wrong')

def start():
        while True:
                #os.system('cls')
                do = input('What do you want?\n\n1:Sign in\n2:Sign up\n3:exit\n\n')
                if do == '1':
                        sign_in()
                if do == '2':
                        sign_up()
                if do == '3':
                        exit()
start()