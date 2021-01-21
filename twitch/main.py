import socket
import json
from emoji import demojize
import re
import sys
from datetime import datetime
import logging
from twitch.commands.commands import commands

class sockWrap:
    def __init__(self):
        self.socket = socket.socket()
        with open('private/connection.json') as f:
            data = json.load(f)
            self.server = data['server']
            self.port = data['port']
            self.token = data['token']
            self.nickname = data['nickname']
            self.channel = data['channel']
        self.connect_socket()

    def connect_socket(self):
        self.socket.connect((self.server, self.port))
        self.socket.send(f"PASS {self.token}\n".encode('utf-8'))
        self.socket.send(f"NICK {self.nickname}\n".encode('utf-8'))
        self.socket.send(f"JOIN {self.channel}\n".encode('utf-8'))

def main():
    sock = sockWrap()
    callCommand = commands(sock)
    while True:
        resp = sock.socket.recv(2048).decode('utf-8')

        if resp.startswith('PING'):
            sock.socket.send("PONG\n".encode('utf-8'))
    
        elif len(resp) > 0:
            resp = parse_resp(resp)
            for line in resp:
                print(str(line['dt']) + " - " + line['username'] + " - " + line['message'])
                if(line['message'][0] == "!"):
                    command = line['message'][1:]
                    callCommand.call(line['username'],command)
            

def parse_resp(resp):
    resp = demojize(resp)
    lines = str.splitlines(resp)
    data = []
    for line in lines:
        try:
            if(resp[0] != ":"):
                time_logged = line.split('—')[0].strip()
                time_logged = datetime.strptime(time_logged, '%Y-%m-%d_%H:%M:%S')

                username_message = line.split('—')[1:]
                username_message = '—'.join(username_message).strip()
            else:
                time_logged = datetime.now()
                username_message = line
                username_message = (username_message).strip()
            reg = re.search(
                ':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)', username_message
            )
            username, channel, message = reg.groups()
            d = {
                'dt': time_logged,
                'channel': channel,
                'username': username,
                'message': message
            }
            data.append(d)
        except Exception:
            print(sys.exc_info()[0])
    return data

