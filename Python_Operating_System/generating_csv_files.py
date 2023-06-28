#!/usr/bin/env python3

import csv

hosts = [["Workstation.local","192.168.25.46"],["Webserver.cloud", "10.2.5.6"]]
with open ('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
