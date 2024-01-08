# SYN-FLOOD-DOS-ATTACKER-I-SDN
Detta reposetory är en guide till installationen av mininet och dokumentation av olika attack typer.

## Installation av mininet i UBUNTU

först insatalera vi mininet genom sudo `apt-get install mininet`.

sedan ladda vi ner github `sudo apt-get install git`.

vi clona mininet github `git clone git://github.com/mininet/mininet`.

i mininet hitta `git tag`.

kopiera tag.

skapa en ny gren `git checkout -b "tag"`.

ladda ned python och andra verktyg för mininet `mininet/util/install.sh -a`.

lägg till din linux distributiuon, den finns på topen när du ladar ner `mininet/util/install.sh -a "din linux distributiuon"`.

## Starta mininet

för att starta en simpel mininet skriver du `sudo mn` det ger den en kontroller en switch och två host
