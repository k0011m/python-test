import os
import hashlib
import socket
import pika
import getpass
import json

user_list = []
user_list.append(('admin','6371295ff936e8fae98f8ee80475bee3dc0e461754cdf5b6cce836648a83cf25'))
display_name = ''

#socket通信(使わないかも)

#rabbitmqの立ち上げ(未完)
def message(name,port):
        pika_host = pika.ConnectionParameters('localhost')
        pika_conect = pika.BlockingConnection(pika_host)
        channel = pika_conect.channel()
        print('ok')

def add_friend(friend_name,port):
        print('wait')
        #with open(friend_txt_file,'r') as friend_list_file_line:

#messageのhome画面
def message_home(username):
        while True:
                friend_info_list = [] #num,username,port情報
                friend_num_list = [] #num情報
                friend_name_list = [] #username情報
                friend_port_list = [] #port情報
                friend_view_list = [] #num,username情報
                friend_list_view_str = ''
                friend_list_file_len = 0

                #pathget
                user_profile = os.environ['USERPROFILE']
                directory_name = f"message_test_python_{username}"
                new_directory = os.path.join(user_profile,directory_name)
                friend_txt_file = os.path.join(new_directory,'friend_list.json')


                try:#フレンドリスト(自己ファイル管理)を読み込む
                        open(friend_txt_file)



                #ない場合は作成
                except FileNotFoundError:
                        os.mkdir(new_directory)
                        open(friend_txt_file,'w')
                        print('Created because there is no friends list')

                else:
                        with open(friend_txt_file,'r') as friend_list_file_load:
                                friend_list_file_line = json.load(friend_list_file_load)
                                friend_list_file_line_len = len(friend_list_file_line)
                                num = 0
                                #それぞれのlistにjsonから突っ込む
                                for num in friend_list_file_line:
                                        #num_str = "'" + str(num + 1) + "'"
                                        fna = friend_list_file_line[str(num)]['friend_name']
                                        pt = friend_list_file_line[str(num)]['port']
                                        #フレンドリスト化して、numで接続できるようにする
                                        friend_info_list.append((num,fna,pt))#all
                                        friend_name_list.append(fna)#username
                                        friend_num_list.append(num)#num
                                        friend_port_list.append(pt)#port
                                #listをstr化する
                                for list_append_fre in friend_num_list:
                                        friend_num_str = friend_num_list[int(list_append_fre) - 1]
                                        friend_name_str = friend_name_list[int(list_append_fre) - 1]
                                        friend_view_list.append(f"{friend_num_str}  {friend_name_str}\n")
                                friend_list_view_str = ''.join(friend_view_list)
                                friend_list_file_len = len(friend_list_file_line) + 1
                                friend_list_file_load.close()

                send_user = input(friend_list_view_str + '\n\n/add\n\n')
                if send_user == '/add':
                        add_port = input('what is port:')
                        add_friend_name = input("what is friend's name:")
                        friend_list_past = open(friend_txt_file,'r')
                        with open(friend_txt_file,'r') as friend_list_past:
                                friend_list_past_load = json.load(friend_list_past)
                        #ここからjsonにデータを追加するにはどうすればよいか
                        add_data = {friend_list_file_len:{"friend_name":add_friend_name,"port":add_port}}
                        friend_list_past_load.update(add_data)


                        with open(friend_txt_file,'w') as friend_list_file_past_load:
                                json.dump(friend_list_past_load,friend_txt_file)
                                
#ホーム画面
def Home(username,port):
        while True:
                global user_list
                global display_name
                do = input('Here is Home\n\n1:change profile\n2:send_message\n3:news\n4:exit\n\n')
                if do == '1':
                        change = input('What will you change?\n\n1:display name\n2:user name\n3:password\n\n')
                        if change == '1':
                                new_display_name = input('new display name:')
                                display_name = new_display_name
                        if change == '2':
                                new_username = input('new name:')
                                oldname,oldpass = user_list[port - 8000]
                                user_list[port - 8000] = (new_username,oldpass)
                        if change == '3':
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
                        message_home(username)
#                if do == '3':
                if do == '4':
                        start()
 
def login(name,port):
        os.system('cls')
        print('Hello! ' + name)
        print("\nYou'r port is",port)
        Home(name,port)

def sign_in():
        global user_list
        os.system('cls')
        username = str(input('username:'))
        password = str(getpass.getpass('password:'))
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
                os.system('cls')
                do = input('What do you want?\n\n1:Sign in\n2:Sign up\n3:exit\n\n')
                if do == '1':
                        sign_in()
                if do == '2':
                        sign_up()
                if do == '3':
                        exit()
start()