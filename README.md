# DHCP-starvation

### Qu'est-ce que le DHCP?
>Le protocole DHCP permet la configuration dynamique de paramètres réseau en gérant une base de données de paramètres configurables pour chacun des ordinateurs sur le réseau. DHCP permet aussi l'allocation dynamique d'adresses IP. Cette allocation peut être permanente (automatique ou manuelle) ou dynamique (avec délai d'expiration). Une fois les paramètres négociés, un poste de travail peut charger une image système à partir d'un serveur à l'aide de Trivial File Transfer Protocol (TFTP).
Lorsqu'on doit gérer un grand ensemble d'ordinateurs ayant sensiblement la même configuration, on voudrait être capable de centraliser la gestion des paramètres de configuration de ces ordinateurs pour éviter de devoir modifier sur chacun d'eux ces informations manuellement. Si vous avez par exemple 100 postes de travail ayant tous la même configuration (adresse du routeur, serveur DNS, masque réseau, imprimantes, etc.), un changement d'un de ces paramètres demande un grand travail si on doit modifier la configuration de chaque machine. Le protocole DHCP permet de simplifier ce travail en centralisant la gestion de ces paramètres et en fournissant un protocole pour leur négociation.

Fait inusité, DHCP est un protocole de la couche application utilisant IP/UDP. Quelques trucs sont donc nécessaires pour initialiser le processus, puisque souvent l'adresse IP du client lui est inconnue au départ.

### Fonctionnement du protocole DHCP
>Les requêtes sont transmises du client au port 67 du serveur. Les réponses sont transmises du serveur au port 68 du client. Si le client ignore l'adresse du serveur, il envoie son message par un "broadcast" sur le réseau local. Comme seul les serveurs DHCP écoutent sur le port 67, les autres postes de travail détruisent ce message sur réception. Le client attend ensuite sur le port 68 pour les réponses du serveur. Certains systèmes ne permettent pas de faire un "unicast" à un client n'ayant pas d'adresse IP, même si on connaît l'adresse de l'interface matérielle. Dans ces cas, le serveur doit faire un "broadcast" de sa réponse. En transmettant sur le port 68, on évite que les serveurs DHCP qui écoutent seulement au port 67 doivent décoder des réponses à des requêtes.

![image](https://user-images.githubusercontent.com/83721477/147104995-ce9b5446-6763-4841-bd3c-73edbb4b6d51.png)

### Attaque DHCP Starvation
>DHCP Starvation (attaque par épuisement de ressources) cible généralement les serveurs DHCP du réseau, dans le but d'inonder le serveur DHCP autorisé de messages de demandes DHCP REQUEST en utilisant des adresses MAC source spoofées. Le serveur DHCP répondra à toutes les demandes, sans savoir qu'il s'agit d'une attaque, en lui attribuant les adresses IP disponibles, entraînant ainsi l'épuisement du stock DHCP. Les vrais clients ne pourront plus obtenir d'adresse IP : le trafic réseau sera paralysé.

###### © 2021 IONOS SARL & P. Kropf, G. Babin
