#! /usr/bin/env python

# This script helps to get some statistic from Mongo DB node.
# It was originally developed to be used by Zabbix. But it could be
# used with different monitoring tools or manually as well.

#  PREREQUISITE:
# Mongo Rest Api should be enabled. Use "rest = true" option. (see more at
# https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0CC0QFjAA&url=http%3A%2F%2Fwww.mongodb.org%2Fdisplay%2FDOCS%2FHttp%2BInterface%2F&ei=rCMaVJumDtfloASn8oD4AQ&usg=AFQjCNEqcTRKhmKEsei04Orz3dLuzveG9w&sig2=bWCYgmE7IfHOxrpkf72ShQ&bvm=bv.75097201,d.cGU)

# License: GNU General Public License 3.0
# Author: Vladimir Malyarevich


import urllib
import json
import optparse
import sys


def main():
    usage = "Usage: %prog -h <fqdn> -p <parameter>"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('-n', '--node', type='string', help="FQDN of mongoDB node")
    parser.add_option('-p', '--param', type='string', help="Parameter to obtain. "
                      "Use comma-separated list for nested parameters.")
    (options, args) = parser.parse_args()

    # Verify options
    if len(args) != 0:
        print "ERROR: options malformed"
        sys.exit(1)

    param = options.param.split(',')

    # Get Json from Mongo node
    url = urllib.urlopen("http://{0}:28017/serverStatus".format(options.node))
    try:
        stat = json.loads(url.read())
    except ValueError:
        print "ERROR: json couldn't be load. Verify if rest is enabled"
        sys.exit(1)

    current = stat # Temp variable to walk alon stat dictionary
    for p in param:
        current = current.get(p)
        if current is None:
            print "ERROR: no such parameter found"
            sys.exit(1)
    print current

if __name__ == '__main__':
    main()
