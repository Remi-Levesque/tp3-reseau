import socket, optparse, sys
#choisissez l’adresse avec l’option -a et le port avec -p
parser = optparse.OptionParser()
parser.add_option("-a", "--address", action="store", dest="address", default="localhost")
parser.add_option("-p", "--port", action="store", dest="port", type=int, default=1337)
opts = parser.parse_args(sys.argv[1:])[0]
     #le socket aura besoin d’un tuple contenant l’adresse et le port
destination = (opts.address, opts.port)
     #creation du socket et connexion a l’hote distant
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) s.connect(destination)
msgSize = 64
#on attend un message du serveur
message = s.recv(msgSize).decode()
print(message)
     #on entre notre reponse et l’envoie
reponse = input()
s.send(reponse.encode())
     #on attend une nouvelle reponse du serveur
message = s.recv(msgSize).decode() print(message)
s.close()
