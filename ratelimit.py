from mininet.net import Mininet
from mininet.link import TCLink
from mininet.topo import Topo
from mininet.cli import CLI

net= Mininet()

h1 = net.addHost('h1')
h2 = net.addHost('h2')
h3 = net.addHost('h3')
s1 = net.addSwitch('s1')
c0 = net.addController('c0', ip='127.0.0.1',port=6653)

link_opts= {'bw':5}
net.addLink(h1, s1, cls=TCLink,**link_opts)
net.addLink(h2, s1, cls=TCLink,**link_opts)
net.addLink(h3, s1, cls=TCLink,**link_opts)

net.start()
CLI(net)
net.stop()
