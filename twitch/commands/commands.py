from database.controllers.main_controller import main_controller as cont
class commands:
    
    def __init__(self, sock):
        self.sock = sock
        self.controller = cont()
        self.commandDict = {
            'GSM': self.sendChat,
            'GSJoin': self.join
        }

    def call(self, username, command):
        command = command.split(" ")
        commType = command[0]
        args = command[1:]
        call = self.commandDict.get(commType, None)
        if(call):
            print(call(username, args))
        

    def sendChat(self, user, args):
        chat = ' '.join(str(n) for n in args)
        try:
            self.sock.socket.send("PRIVMSG {} :{}\r\n".format(self.sock.channel, chat).encode("utf-8"))
            return True
        except:
            return False

    def join(self, user, args):
        try:
            self.controller.create.create_user(None, user)
            self.sock.socket.send("PRIVMSG {} :{}\r\n".format(self.sock.channel, user+" Has Joined Good Samaritans").encode("utf-8"))
            return True
        except:
            return False