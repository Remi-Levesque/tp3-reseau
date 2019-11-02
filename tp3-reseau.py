from cryptoModule import entierAleatoire, trouverNombrePremier, exponentiationModulaire
import socket, optparse, sys
from socketUtil import recv_msg, send_msg


#choisissez l’adresse avec l’option -a et le port avec -p
parser = optparse.OptionParser()
parser.add_option("-s", "--server", action="store_true", dest="serveur", default=False)
parser.add_option("-a", "--address", action="store", dest="address", default="localhost")
parser.add_option("-p", "--port", action="store", dest="port", type=int, default=1337)

opts = parser.parse_args(sys.argv[1:])[0]

if opts.serveur: #mode serveur
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(("localhost", opts.port))
    serversocket.listen(5)
    print("Listening on port " + str(serversocket.getsockname()[1]))

    i = 0
    while True:
        i +=1
        (s, address) = serversocket.accept()
        print(address)
        print(s)
        print (str(i) + "e connexion au serveur")
        send_msg(s, "Bonjour, mon nom est Serveur. Et vous?\n")
        nom = recv_msg(s)
        print("Le nom du client est " + nom)
        send_msg(s, "Enchante, " + nom)
        s.close()

else: #mode Client
    destination = (opts.address, opts.port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(destination)
    print(recv_msg(s))
    send_msg(s, input())
    print(recv_msg(s))
    s.close()
