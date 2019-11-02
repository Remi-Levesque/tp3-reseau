import socket, optparse, sys
#choisissez le port avec l’option -p
parser = optparse.OptionParser()
parser.add_option("-p", "--port", action="store", dest="port", type=int, default=1337)
port = parser.parse_args(sys.argv[1:])[0].port
#AF_INET: indique d’utiliser des adresses IPv4
#SOCK_STREAM: indique d’utiliser le protocole TCP
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     #permet de faire plusieurs communications de suite sur le meme port
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
     #indique au socket d’ecouter sur le port selectionne
serversocket.bind(("localhost", port))
     #demarre le socket
serversocket.listen(5)
print("Listening on port " + str(serversocket.getsockname()[1]))

i=0
while True:
    #un client se connecte au serveur
    #s est un nouveau socket pour interagir avec le client

    (s, address) = serversocket.accept()
            #affichage du nombre de connection au serveur
    i += 1
    print (str(i) + "e connexion au serveur")
            #le serveur envoie un message au client
    message = "Bonjour, mon nom est Serveur. Et vous?\n"
    s.send(message.encode())
            #le serveur attend un message d’au plus 32 octets de la part du client puis le stocke dans
              #une variable
    nom = s.recv(32).decode()
    print(nom)
    message = "Enchante, " + nom
    s.send(message.encode())
    s.close()
