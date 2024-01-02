# Importera nödvändiga moduler från Mininet
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.node import CPULimitedHost

# Skapa ett Mininet-objekt med CPULimitedHost som standardhost
net = Mininet(host=CPULimitedHost)

# Skapa host, switch och controller
h1 = net.addHost('h1',cpu=1.0)
h2 = net.addHost('h2',cpu=1.0)
h3 = net.addHost('h3',cpu=1.0)
s1 = net.addSwitch('s1')
c0 = net.addController('c0', ip='127.0.0.1', port=6653) #Skapa en controller 'c0' med IP '127.0.0.1' och port '6653'

# Lägg till länkar mellan host och switch med konfigurerade länkalternativ
net.addLink(h1, s1)
net.addLink(h2, s1)
net.addLink(h3, s1)


# Apply cpulimit to limit all processes on each host
for host in net.hosts:
     host.cmd('cpulimit --limit=10 --background')
# Starta nätverket
net.start()

# Starta CLI (Command Line Interface) för att interagera med nätverket
CLI(net)

# Stoppa nätverket efter att CLI-sessionen är avslutad
net.stop()

