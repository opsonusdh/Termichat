import subprocess



              
#function define
def clear():
    subprocess.run('clear',shell=True)
    
col = {
    'black': '\033[30m',
    'purple':'\033[95m',
    'cyan':'\033[96m',
    'blue':'\033[94m',
    'green':'\033[92m',
    'yellow':'\033[93m',
    'red':'\033[91m',
    'bold':'\033[1m',
    'underline':'\033[4m',
    'end':'\033[0m',
    'newline':'\n',
    'tab':'\t',
    'gray': '\033[90m',
    'red-d': '\033[31m',
    'green-d': '\033[32m',
    'yellow-d': '\033[33m',
    'blue-d': '\033[34m',
    'purple-d': '\033[35m',
    'cyan-d': '\033[36m',
    'white-d': '\033[37m',
    'gray-bg': '\033[100m',
    'red-bg': '\033[101m',
    'green-bg': '\033[102m',
    'yellow-bg': '\033[103m',
    'blue-bg': '\033[104m',
    'purple-bg': '\033[105m',
    'cyan-bg': '\033[106m',
    'white-bg': '\033[107m',
    'black-bg': '\033[40m',
    'red-bg-d': '\033[41m',
    'green-bg-d': '\033[42m',
    'yellow-bg-d': '\033[43m',
    'blue-bg-d': '\033[44m',
    'purple-bg-d': '\033[45m',
    'cyan-bg-d': '\033[46m',
    'white-bg-d': '\033[47m'
}

def color(text,*args):
    txt = ''
    args = list(args)
    if 'end' in args:
        end = True
        args.remove('end')
    else:
        end = False
    for i in args:
        txt += col[i]
    if end:
        return txt+text+col['end']
    else:
        return txt+text



#checking modules
while True:
        try:
            global requests, HTTPBasicAuth, tinydb, random, re, time
            import requests
            from requests.auth import HTTPBasicAuth
            import tinydb
            import re, random, time, emoji
            break
        except:
            print(color('[!] Installing modules. Please don\'t close the window. This only take a while...','yellow','bold','end'))
            for i in ['requests','tinydb','re','random','time','emoji']:
                subprocess.run(f'pip install {i}',shell=True)
                



def logo(animation=False):
    text = "  _______                  _      _           _   \n |__   __|                (_)    | |         | |  \n    | | ___ _ __ _ __ ___  _  ___| |__   __ _| |_ \n    | |/ _ \ '__| '_ ` _ \| |/ __| '_ \ / _` | __|\n    | |  __/ |  | | | | | | | (__| | | | (_| | |_ \n    |_|\___|_|  |_| |_| |_|_|\___|_| |_|\__,_|\__|\n                                                  By S.D.H."
    if not animation:
        print(color(text,'blue','bold','end'))
    else:
        for i in text.split('\n'):
                    print(color(i,'blue','bold','end'))
                    time.sleep(0.1)
    print('\n\n')
    



def int_on():
    if subprocess.getoutput("ping -c 1 8.8.8.8") == "connect: Network is unreachable":
        return False
    else:
        return True


#some code
clear()
logo(True)
if not int_on():
    print(color("[!] Internet is not connected. Please try again.",'bold','red','end'))
    quit()







file = open("gists/gists.json","r")
cont = eval(file.read())
USERNAME = cont["username"]
TOKEN = cont["token"]
IDINFO = cont["idinfo"]
ROOMSERVER = cont["roomserver"]
file.close()



if IDINFO == ROOMSERVER:
    print(color("[+] Creating github based servers...","yellow","end"))
    create_url = 'https://api.github.com/gists'
        
    create_data = {
        "public": False,
        "files": {
            "idinfo.txt": {
                "content": "[]"
            }
        }
    }
    try:
        response = requests.post(create_url, json=create_data, auth=HTTPBasicAuth(self.username, self.token))
        IDINFO = str(response.json()['id'])
    except:
        print(color("[!] Internet is not connected. Please try again.",'bold','red','end'))
        quit()
    
    create_data = {
        "public": False,
        "files": {
            "roomserver.txt": {
                "content": "[]"
            }
        }
    }
    try:
        response = requests.post(create_url, json=create_data, auth=HTTPBasicAuth(self.username, self.token))
        ROOMSERVER = str(response.json()['id'])
    except:
        print(color("[!] Internet is not connected. Please try again.",'bold','red','end'))
        quit()

    file = open("gists/gists.json","w")
    file.write("{'username': "+ f"'{USERNAME}','token':"+ f"'{TOKEN}', 'idinfo':"+ f"'{IDINFO}', 'roomserver':"+ f"'{ROOMSERVER}'"+"}")
    file.close()




class ServerError(Exception):
     def __init__(self,mess):
        self.message = mess
        super().__init__(self.message)



    
def bin_to_text(bin_data):
    byte_chunks = [bin_data[i:i+8] for i in range(0, len(bin_data), 8)]
    byte_values = [int(byte, 2) for byte in byte_chunks]
    bytes_data = bytes(byte_values)
    text = bytes_data.decode('utf-8')
    return text
    
def simple_hash(password: str) -> int:
    salted_password = password + bin_to_text('0100100100100000011011010111010101110011011101000010000001100010011001010010000001101101011100100010000001100110011001010110010101101100')
    hash_value = 0
    for char in salted_password:
        hash_value = (hash_value * 31 + ord(char)) % (2**32)
    return hash_value
    
def verify_simple_hash(stored_hash: int, provided_password: str) -> bool:
    hash_value = simple_hash(provided_password)
    return hash_value == stored_hash



        
def text_modify(text):
    text = text.replace(r'\${', '__ESCAPED_DOLLAR__{')
    pattern = re.compile(r'\${([^}]*)}')
    
    def replacement(match):
        instructions = match.group(1)
        replacement_str = ''
        if instructions.startswith('emoji:'):
            emoji_name = instructions[len('emoji:'):].split(',')[0].strip()
            emojii = emoji.emojize(f":{emoji_name}:")
            if emojii != f":{emoji_name}:":
                if ',' in instructions[len('emoji:'):]:
                    if instructions[len('emoji:'):].split(',')[1] == '':
                        temp = ''
                    else:
                        temp = ' '
                else:
                    temp = ''
                replacement_str += emojii+temp
            instructions = instructions[len('emoji:' + emoji_name):]
        
        instructions_list = [instr.strip() for instr in instructions.split(',')]
        for instr in instructions_list:
            if instr in col:
                replacement_str += col[instr]
            else:
                fg_match = re.match(r'^(\d{1,3})$', instr)
                bg_match = re.match(r'^(\d{1,3})-bg$', instr)
                if fg_match:
                    color_code = fg_match.group(1)
                    replacement_str += f'\033[38;5;{color_code}m'
                elif bg_match:
                    color_code = bg_match.group(1)
                    replacement_str += f'\033[48;5;{color_code}m'
        return replacement_str

    modified_text = re.sub(pattern, replacement, text)
    modified_text = modified_text.replace('__ESCAPED_DOLLAR__{', r'${')
    return modified_text + col['end']
    
class Server:
    def __init__(self,USERNAME, TOKEN, IDINFO, ROOMSERVER):
        self.username = USERNAME
        self.token = TOKEN
    
    def edit_gist(self,gist_id,filename,new_content):
        edit_url = f'https://api.github.com/gists/{gist_id}'

        update_data = {
            "files": {
                filename: {
                    "content": new_content
                }
            }
        }
        try:
            response = requests.patch(edit_url, json=update_data, auth=HTTPBasicAuth(self.username, self.token))
        except:
            print(color("[!] Internet is not connected. Please try again.",'bold','red','end'))
            quit()

    def read_gist(self,gist_id):
        read_url = f'https://api.github.com/gists/{gist_id}'
        try:
            response = requests.get(read_url)
        except:
            print(color("[!] Internet is not connected. Please try again.",'bold','red','end'))
            quit()
        if response.status_code == 200:
            gist = response.json()
            for filename, file_info in gist['files'].items():
                return filename,file_info["content"]


    
    
    






    #creating id
    def create_id(self,username,nickname,passwd):
        content = self.read_gist(IDINFO)[1]
        content = eval(content)
        for m in content:
            if m["username"] == username:
                raise ServerError("Username already Exists")
        content.append(eval('{"username":"'+username+'","nickname":"'+nickname+'","password":'+str(simple_hash(passwd))+'}'))
        self.edit_gist(IDINFO,"idinfo.txt",str(content))
        
    
    #deleting id
    def delete_id(self,username,passwd):
        content = eval(self.read_gist(IDINFO)[1])
        for m in range(len(content)):
            c = content[m]
            if c["username"] == username and c["password"] == simple_hash(passwd):
                content.pop(m)
                self.edit_gist(IDINFO,'idinfo.txt',str(content))
                return
        raise ServerError("Invalid username or password")
    
    #editing id
    def edit_id(self,mode,username,passwd,new_one):
        content = eval(self.read_gist(IDINFO)[1])
        for m in range(len(content)):
            c = content[m]
            if c["username"] == username and c["password"] == simple_hash(passwd):
                #mode 0 = nickname, 1 = password
                if mode == 0:
                    c["nickname"] = new_one
                else:
                    c["password"] = simple_hash(new_one)
                
                content[m] = c
                self.edit_gist(IDINFO,'idinfo.txt',str(content))
                return
        raise ServerError("Invalid username or password")


    def sign_id(self, username, passwd):
        file, content = self.read_gist(IDINFO)
        content = eval(content)
        for m in range(len(content)):
            c = content[m]
            if c["username"] == username and c["password"] == simple_hash(passwd):
                return c
        raise ServerError("Invalid username or password")
    
    
    
    
    def get_room(self,room_id,passwd):
        content = eval(self.read_gist(ROOMSERVER)[1])
        for m in range(len(content)):
            c = content[m]
            if c['room_id'] == room_id:
                gist_id = c['gist_id']
                
                room_content = eval(self.read_gist(gist_id)[1])
                if room_content["password"] == simple_hash(passwd):
                    return c
                else:
                    raise ServerError("Invalid Room Password")
        
        raise ServerError("Room does not Exists")
        
    
    #create room
    def create_room(self,room_name,passwd,id):
        content = eval(self.read_gist(ROOMSERVER)[1])
        while True:
            room_id = ''
            for i in range(6):
                room_id += str(random.choice([0,1,2,3,4,5,6,7,8,9]))
            room_id = int(room_id)
            for m in content:
                if m['room_id'] == room_id:
                    continue
            break
        
        create_url = 'https://api.github.com/gists'
        
        create_data = {
            "public": False,
            "files": {
                f"{room_name}.json": {
                    "content": str({"room_id":room_id,"password":simple_hash(passwd),"members":[id],"admins":[id],"chats":[]})
                }
            }
        }
        try:
            response = requests.post(create_url, json=create_data, auth=HTTPBasicAuth(self.username, self.token))
        except:
            print(color("[!] Internet is not connected. Please try again.",'bold','red','end'))
            quit()
            
        gist_id = str(response.json()['id'])
        content.append({"room_id":room_id,"gist_id":gist_id})
        self.edit_gist(ROOMSERVER, "roomserver.txt", str(content))
        return room_id, gist_id
    
    def delete_room(self, room_id,passwd):
        content = eval(self.read_gist(ROOMSERVER)[1])
        for m in range(len(content)):
            c = content[m]
            if c['room_id'] == room_id:
                gist_id = c['gist_id']
                
                room_content = eval(self.read_gist(gist_id)[1])
                if room_content["password"] == simple_hash(passwd):
            
                    delete_url = f'https://api.github.com/gists/{gist_id}'
                    try:
                        response = requests.delete(delete_url, auth=HTTPBasicAuth(self.username, self.token))
                    except:
                        print(color("[!] Internet is not connected. Please try again.",'bold','red','end'))
                        quit()
            
                    content.pop(m)
                    self.edit_gist(ROOMSERVER, "roomserver.txt", str(content))
                    return
                else:
                    raise ServerError("Invalid Room Password")
        
        raise ServerError("Room does not Exists")
                
    
    def chat(self,username,room_gist_id,passwd,text,time):
        file, content = self.read_gist(room_gist_id)
        content = eval(content)
        if content['password'] == simple_hash(passwd):
            chats = content["chats"]
            
            cont = {"username":username,"text":text,"time":time}
            chats.append(cont)
            content["chats"] = chats
            
            self.edit_gist(room_gist_id, file, str(content))
        else:
            raise ServerError('Invalid room password.')
            
    
    




server = Server(USERNAME, TOKEN, IDINFO, ROOMSERVER)
id = nickname = password = room_name = room_id = room_gist_id = room_pass = ''
check_old = check_room_old = True


def intro():
    global id, nickname, password,check_old
    
    while (id=='' or nickname=='' or password==''):
        clear()
        logo(True)
        db = tinydb.TinyDB("userid.json")
        lst = db.all()
        if lst != [] and check_old:
            try:
                user_data = server.sign_id(lst[0]['username'],lst[0]['password'])
                id, nickname, password = user_data['username'], user_data['nickname'], lst[0]['password']
                continue
            except ServerError as e:
                input(color('[!] '+str(e)+'. Press Enter: ','bold','red', 'end'))
        
        print(color("Options:\n  [1] Log in\n  [2] Sign up\n  [3] exit","yellow","bold","end"))
        inp = input(color("\nEnter your choice: ","cyan","bold"))
    
        if inp == "1":
            clear()
            logo()
            print(color("Log in",'yellow','bold','end'),color("\n  [?] Press \"-b\" for back\n",'purple','bold','end'))
            id = input(color('Enter your username: ','cyan','bold'))
            if id == '-b':
                continue
            password = input(color('Enter your password: ','cyan','bold'))
            if password == '-b':
                continue
            try:
                user_data = server.sign_id(id,password)
                print(color("[✓] Login successful! \n","green","bold","end"))
                print(color('[?] Save login info?\nOptions:\n  [1] Yes\n  [2] No',"yellow",'bold'))
                inp = input(color('Enter your choice: ','cyan','bold'))
                if inp == '1':
                    db = tinydb.TinyDB("userid.json")
                    db.truncate()
                    user_data1 = user_data
                    user_data1["password"] = password
                    db.insert(user_data1)
                break
            except ServerError as e:
                id = ''
                input(color('[!] '+str(e)+'. Press Enter: ','bold','red', 'end'))
                continue
    
        elif inp == '2':
            while True:
                clear()
                logo()
                print(color("Sign up",'yellow','bold','end'),color("\n  [?] Press \"-b\" for back\n",'purple','bold','end'))
                id = input(color('Enter your username: ','cyan','bold'))
                if id == '-b':
                    id = ''
                    break
                content = server.read_gist(IDINFO)[1]
                content = eval(content)
                user_found = False
                for m in content:
                    if m["username"] == id:
                        id = ''
                        user_found = True
                        break
                if user_found:
                    input(color("[!] Username already Exists. Press enter: ", 'red', 'bold'))
                    continue
            
                nickname = input(color('Enter your nickname: ','cyan','bold'))
                if nickname == '-b':
                    nickname = ''
                    break
                password = input(color('Enter your password: ','cyan','bold'))
                if password == '-b':
                    password = ''
                    break
        
                server.create_id(id, nickname,password)
                user_data = {"username":id,"nickname":nickname,"password":password}
                
                print(color("[✓] Log in successful.\n",'green','end'))
                print(color('[?] Save login info?\nOptions:\n  [1] Yes\n  [2] No\n','yellow','bold'))
                inp = input(color('Enter your choice: ','cyan','bold'))
                if inp == '1':
                    db = tinydb.TinyDB("userid.json")
                    db.truncate()
                    db.insert(user_data)
                break
        elif inp == '3':
            print(color('\n|#|','green'),color('GoodBye!','underline','end'))
            quit()
    return




def user_interface():
    global room_name,room_id,room_gist_id,room_pass,nickname, id, password, check_old, check_room_old
    
    while room_name=='' or room_id=='' or room_gist_id=='' or room_pass=='':
        db = tinydb.TinyDB("rooms.json")
        room_list = db.all()
        
        clear()
        logo()
        print(color(f'|#| Logged is as {id}...\n    Wellcome, {nickname}.','green','end'))
        print(color('\nOptions:\n  [1] Create room\n  [2] Join Room\n  [3] Settings\n  [4] Show previosly joined rooms\n  [5] Log out\n','yellow','bold','end'))
        inp = input(color('Enter your choice: ','cyan','bold'))
        if inp == '5':
            check_old = False
            id = nickname = password = room_name = room_id = room_gist_id = room_pass = ''
            intro()
        elif inp == '1':
            clear()
            logo()
            print(color("Create room",'yellow','bold','end'),color("\n  [?] Press \"-b\" for back\n",'purple','bold','end'))
            room_name = input(color('Enter your room name: ','cyan','bold'))
            if room_name == '-b':
                room_name = ''
                break
            passwd = input(color('Enter your room password: ','cyan','bold'))
            if passwd == '-b':
                break
            room_pass = passwd
            room_id, room_gist_id = server.create_room(room_name, passwd,id)
            print(color("\n[✓] Room created successfully.",'green', 'bold','end'))
            print(color("Your room id is",'purple', 'bold','end'),color(str(room_id),'purple', 'bold','underline','end'))
            print(color('[?] Save room info?\nOptions:\n  [1] Yes\n  [2] No','yellow','bold'))
            inp = input(color('Enter your choice: ','cyan','bold'))
            if inp == '1':
                 db = tinydb.TinyDB("rooms.json")
                 lis = db.all()
                 if len(lis) >= 50:
                     first_doc_id = min(doc.doc_id for doc in db)
                     db.remove(doc_ids=[first_doc_id])
                 db.insert({'room_name':''.join(room_name.split('.')[:-1]),'room_id':room_id, 'room_gist_id':room_gist_id, 'password':room_pass})
                 
                 
        elif inp == '2':
            clear()
            logo()
            if room_list != [] and check_room_old:
                first_doc = max(room_list, key=lambda doc: doc.doc_id)
                print(color(f'\n[?] Join "{first_doc["room_name"]}" Room?\n\nOptions:\n  [1] Yes\n  [2] No\n','yellow','bold'))
                imp = input(color('Enter your choice: ','cyan','bold'))
                if imp == '1':
                    room_cont = eval(server.read_gist(ROOMSERVER)[1])
                    for i in room_cont:
                        if i['room_id'] == int(first_doc["room_id"]):
                            room_gist_id = i['gist_id']
                            break
                    if room_gist_id == '':
                        input(color('[!] Invalid Room Id. Maybe the room has deleted. press enter: ','bold','red','end'))
                        check_room_old = False
                    else:
                        room_name, room_cont = server.read_gist(room_gist_id)
                        room_cont = eval(room_cont)
                        if simple_hash(first_doc["password"]) == room_cont['password']:   
                            room_id = first_doc["room_id"]
                            room_pass = first_doc["password"]
                            input(color('\n[✓] Room joined successfully. press enter: ','green','bold','end'))
                            return
                        else:
                            input(color('[!] Invalid Room Password. Maybe the pasword has changed. press enter: ','bold','red','end'))
                            check_room_old = False
                else:
                    check_room_old = False
            while True:
                clear()
                logo()
                print(color("Join room",'yellow','bold','end'),color("\n  [?] Press \"-b\" for back\n",'purple','bold','end'))
                room_id = input(color('Enter Room Id: ','cyan','bold'))
                if room_id == '-b':
                    user_interface()
                content = eval(server.read_gist(ROOMSERVER)[1])
                for i in content:
                    if str(i['room_id']) == room_id:
                        room_gist_id_temp = i['gist_id']
                        room_name, room_cont = server.read_gist(room_gist_id_temp)
                        room_cont = eval(room_cont)
                        room_pass = input(color('Enter Room Password: ','cyan','bold'))
                        if room_pass == '-b':
                            user_interface()
                        elif room_cont['password'] == simple_hash(room_pass):
                            room_gist_id = i['gist_id']
                            if id not in room_cont['members']:
                                room_cont['members'].append(id)
                                server.edit_gist(room_gist_id, room_name, str(room_cont))
                            print(color('\n[✓] Room login successful.\n','green','bold','end'))
                            print(color('[?] Save room info?\nOptions:\n  [1] Yes\n  [2] No','yellow','bold'))
                            inp = input(color('Enter your choice: ','cyan','bold'))
                            if inp == '1':
                                db = tinydb.TinyDB("rooms.json")
                                lis = db.all()
                                if len(lis) >= 50:
                                    first_doc_id = min(doc.doc_id for doc in db)
                                    db.remove(doc_ids=[first_doc_id])
                                    
                                db.insert({'room_name':''.join(room_name.split('.')[:-1]),'room_id':room_id, 'room_gist_id':room_gist_id, 'password':room_pass})
                            input(color('\n[✓] Room joined successfully. press enter: ','green','bold','end'))
                            return
                        else:
                            input(color("[!] Invalid Room Password. press enter: ",'bold','red','end'))
                            room_id = room_password = ''
                input(color("[!] Invalid Room Id. press enter: ",'bold','red','end'))
                room_id = room_password = ''
                 
        elif inp == '3':
            while True:
                clear()
                logo()
                db = tinydb.TinyDB("userid.json")
                if db.all() != []:
                    user_data = db.all()[0]
                print(color("Settings",'yellow','bold','end'))
                print(color('Options:\n  [1] Change Nickname\n  [2] Change Password\n  [3] Back\n','yellow','bold','end'))
                inp = input(color('Enter your choice: ','cyan','bold'))
                if inp == '1':
                    clear()
                    logo()
                    print(color('Change Nickname\n','yellow','bold','end'))
                    print(color("  [?] Press \"-b\" for back\n",'purple','bold','end'))
                    passwd = input(color('Enter your password: ','cyan','bold'))
                    if passwd == '-b':
                        continue
                    elif passwd != password:
                        input(color("[!] Invalid Password. press enter: ",'bold','red','end'))
                        continue
                    new_one = input(color('Enter your new nickname: ','cyan','bold'))
                    if new_one == '-b':
                        continue
                    try:
                        server.edit_id(0,id,passwd,new_one)
                        nickname = new_one
                        if db.all() != []:
                            user_data['nickname'] = new_one
                            db.truncate()
                            db.insert(user_data)
                        input(color('\n[✓] Nickname changed successfully. press enter: ','green','bold','end'))
                        break
                    except ServerError as e:
                        input(color("[!] "+e+'. press enter: ','bold','red','end'))
                elif inp == '2':
                    clear()
                    logo()
                    print(color('Change Password\n','yellow','bold','end'))
                    print(color("  [?] Press \"-b\" for back\n",'purple','bold','end'))
                    passwd = input(color('Enter your old password: ','cyan','bold'))
                    if passwd == '-b':
                        continue
                    elif passwd != password:
                        input(color("[!] Invalid Password. press enter: ",'bold','red','end'))
                        continue
                    new_one = input(color('Enter your new password: ','cyan','bold'))
                    if new_one == '-b':
                        continue
                    try:
                        server.edit_id(1,id,passwd,new_one)
                        password = new_one
                        if db.all() != []:
                            user_data['password'] = new_one
                            db.truncate()
                            db.insert(user_data)
                        input(color('\n[✓] Password changed successfully. press enter: ','green','bold','end'))
                        break
                    except ServerError as e:
                        input(color("[!] "+e+'. press enter: ','bold','red','end'))
                elif inp == '3':
                    break

        elif inp == '4':
            clear()
            logo()
            print(color('Previous Rooms\n','yellow','bold','end'))
            print(color("  [?] Press \"-b\" for back\n",'purple','bold','end'))
            print()
            db = tinydb.TinyDB("rooms.json")
            room_list = db.all()
            if room_list != []:
                for i in room_list:
                    print(f"{col['yellow']}[{i.doc_id}] {col['end']}Room name: {i['room_name']}\n   {' '*len(str(i.doc_id))}{col['purple']}Room id: {col['underline']}{i['room_id']}{col['end']}\n\n")
                m = input(color('Enter your choice: ','cyan','bold'))
                if m == '-b':
                    continue
                try:
                    m = int(m)
                except:
                    input(color('[!] Invalid Input. press enter: ','bold','red','end'))
                    continue
                if m >= 1 and m <= len(room_list):
                    room_info = db.get(doc_id=m)
                    room_name = room_info['room_name']
                    room_id = room_info['room_id']
                    room_gist_id = room_info['room_gist_id']
                    room_pass = room_info['password']
                    continue
            else:
                input(color('[!] Nothing in History. press enter: ','bold','red','end'))
                continue




def rooming():
    global room_name,room_id,room_gist_id,room_pass,nickname, id, password, check_old, check_room_old
    while True:
        clear()
        logo()
        print(color('Chat room\n','yellow','bold','end'))
        print(color('|#| Room Name:','green','bold','end'),color(f'{"".join(room_name.split(".")[:-1])}\n\n','green','bold','underline','end'))
        print(color('Options:\n  [1] Chat\n  [2] Change Room Password\n  [3] Members\n  [4] Back\n','yellow','bold','end'))
    
        inp = input(color('Enter your choice: ','cyan', 'bold'))
        if inp == '4':
            room_name = room_id = room_gist_id = room_pass = ''
            user_interface()
        elif inp == '3':
            clear()
            logo()
            b = eval(server.read_gist(room_gist_id)[1])
            memb = b['members']
            admin = b['admins']
            print(color('Members\n\n','yellow','bold','end'))
            for i in range(len(memb)):
                temp = '(admin)' if memb[i] in admin else ''
                print(color(f"  [{i+1}] {memb[i]} {temp}", 'green','bold','end'))
                print()
            input(color("[?] Press Enter to back: ",'bold','purple','end'))
        elif inp == '2':
            clear()
            logo()
            print(color('Change Room Password\n','yellow','bold','end'))
            print(color("  [?] Press \"-b\" for back\n\n",'purple','bold','end'))
            b = eval(server.read_gist(room_gist_id)[1])
            if id not in b['admins']:
                input(color("[!] You are not an admin of this room. press enter: ",'bold','red','end'))
                continue
            passwd1 = input(color('Enter your ID\'s password: ','cyan', 'bold'))
            if passwd1 == '-b':
                continue
            if passwd1 != password:
                input(color("[!] Invalid Password. press enter: ",'bold','red','end'))
                continue
            passwd2 = input(color('Enter your old room password: ','cyan', 'bold'))
            if passwd2 == '-b':
                continue
            if passwd2 != room_pass:
                input(color("[!] Invalid Room Password. press enter: ",'bold','red','end'))
                continue
            passwd3 = input(color('Enter your new room password: ','cyan', 'bold'))
            if passwd3 == '-b':
                continue
            b['password'] = simple_hash(passwd3)
            server.edit_gist(room_gist_id, room_name, str(b))
            db = tinydb.TinyDB("rooms.json")
            room = tinydb.Query()
            db.update({'password' : passwd3}, room.room_id == room_id)
        elif inp == '1':
            id_info = eval(server.read_gist(IDINFO)[1])
            members = {}
            see_full = False
            see_user = False
            see_time = False
            while True:
                clear()
                logo()
                print(color('Chat\n','yellow','bold','end'))
                print(color("  [?] Press \"-b\" for back",'purple','bold','end'))
                print(color("  [?] Press \"-r\" for refresh",'purple','bold','end'))
                if not see_full:
                    print(color("  [?] Press \"-f\" to see full chat",'purple','bold','end'))
                if see_full:
                    print(color("  [?] Press \"-f\" to hide full chat",'purple','bold','end'))
                if not see_user:
                    print(color("  [?] Press \"-u\" to see username of the sender",'purple','bold','end'))
                if see_user:
                    print(color("  [?] Press \"-u\" to hide username of the sender",'purple','bold','end'))
                if not see_time:
                    print(color("  [?] Press \"-t\" to see time of sending message\n",'purple','bold','end'))
                if see_time:
                    print(color("  [?] Press \"-t\" to hide time stamp\n",'purple','bold','end'))
                    
                b = eval(server.read_gist(room_gist_id)[1])
                memb = b['members']
                if len(members) != len(memb):
                    for i in id_info:
                        if i['username'] in memb:
                            members.update({i['username']:i['nickname']})

                chats = b['chats']
                if not see_full:
                    chats = chats[len(chats)-50:]
                
                for i in chats:
                    if i['username'] != id:
                        text = color('','bold','yellow')
                    else:
                        text = color('','bold','green')
                    if see_user:
                        text += i['username']
                        text += '('
                        text += members[i['username']]
                        text += ')'
                    else:
                        text += members[i['username']]
                    if see_time:
                        text += "["
                        text += str(i['time'])
                        text += "]"
                    text += color(': ','end')
                    text += text_modify(i['text'])
                    print(text)
                    print()
                print()
                inp = input(color('Type Something: ','cyan','bold'))
                if inp == '-b':
                    rooming()
                    break
                elif inp == '-r':
                    continue
                elif inp == '-f':
                    see_full = not see_full
                elif inp == '-u':
                    see_user = not see_user
                elif inp == '-t':
                    see_time = not see_time
                else:
                    try:
                        server.chat(id,room_gist_id,room_pass,inp,str(time.strftime("%d/%m/%Y-%A-%T")))
                    except ServerError as e:
                        input(color(f'[!] {e} press enter: ','bold','red','end'))
                        
                
                
        
            
      
intro()
user_interface()
rooming()
