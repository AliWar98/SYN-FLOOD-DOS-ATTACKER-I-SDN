# Importera nödvändiga moduler från Mininet
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.topo import Topo
from mininet.cli import CLI

# Skapa ett Mininet-objekt
net = Mininet()

# Skapa host, switch och controller
h1 = net.addHost('h1')
h2 = net.addHost('h2')
h3 = net.addHost('h3')
s1 = net.addSwitch('s1')
c0 = net.addController('c0', ip='127.0.0.1', port=6653) #Skapa en controller 'c0' med IP '127.0.0.1' och port '6653'

# Konfigurera länkalternativ (bandbredd)
link_opts = {'bw': 5} # Skapa en dictionary link_opts med länkalternativ, här är bandbredden satt till 5

# Lägg till länkar mellan host och switch med konfigurerade länkalternativ
net.addLink(h1, s1, cls=TCLink, **link_opts)
net.addLink(h2, s1, cls=TCLink, **link_opts)
net.addLink(h3, s1, cls=TCLink, **link_opts)

# Starta nätverket
net.start()

# Starta CLI (Command Line Interface) för att interagera med nätverket
CLI(net)

# Stoppa nätverket efter att CLI-sessionen är avslutad
net.stop()

