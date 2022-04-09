import os
import time

from modules.DateTimeModule import DateTimeModule
from modules.SystemBandwidthUsage import SystemBandwidthUsage
from modules.SystemLoad import SystemLoad
from modules.SystemMemory import SystemMemory
from modules.SystemCPU import SystemCPU
from modules.SystemNetworkAdapter import SystemNetworkAdapter

lst_modules = []
lst_modules.append(SystemBandwidthUsage())
lst_modules.append(SystemNetworkAdapter('wlp38s0', False))
lst_modules.append(SystemNetworkAdapter('enp34s0'))
lst_modules.append(SystemCPU(70, 90))
lst_modules.append(SystemMemory(60, 90))
lst_modules.append(SystemLoad(1.0, 3.0))
lst_modules.append(DateTimeModule('%A %Y/%m/%d %H:%M:%S'))

while True:
    output = ''
    count = 0
    for module in lst_modules:
        if count > 0:
            output += ' / '
        output += module.get_data()
        count += 1
    print(output)
    time.sleep(1)