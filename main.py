
#    Copyright 2014 Philippe THIRION
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


import sipfullproxy
from sipfullproxy import UDPHandler


if __name__ == "__main__":
    sipfullproxy.logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy.log', level=sipfullproxy.logging.INFO,
                        datefmt='%H:%M:%S')
    sipfullproxy.logging.info(sipfullproxy.time.strftime("%a, %d %b %Y %H:%M:%S ", sipfullproxy.time.localtime()))
    sipfullproxy.hostname = sipfullproxy.socket.gethostname()
    sipfullproxy.ipaddress = sipfullproxy.socket.gethostbyname(sipfullproxy.hostname)

    if sipfullproxy.ipaddress == "127.0.0.1":
        sipfullproxy.ipaddress = sipfullproxy.sys.argv[1]

    sipfullproxy.logging.info(sipfullproxy.hostname)
    sipfullproxy.ipaddress = sipfullproxy.socket.gethostbyname(sipfullproxy.hostname)
    sipfullproxy.socket.gethostbyname(sipfullproxy.hostname)

    sipfullproxy.logging.info(sipfullproxy.ipaddress)
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (sipfullproxy.ipaddress, sipfullproxy.PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (sipfullproxy.ipaddress, sipfullproxy.PORT)
    sipfullproxy.server = sipfullproxy.socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), UDPHandler)

    print("SIP Proxy : <%s:%s>" % (sipfullproxy.ipaddress, sipfullproxy.PORT))

    sipfullproxy.server.serve_forever()
