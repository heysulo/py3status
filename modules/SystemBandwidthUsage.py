from socket import AddressFamily

from modules.BaseModule import BaseModule, ModuleState
import os
import psutil


# from colorama import Fore, Back, Style


class SystemBandwidthUsage(BaseModule):
    def __init__(self):
        BaseModule.__init__(self, 'SystemBandwidthUsage')

    def get_data(self):
        usage = psutil.net_io_counters()
        tx = usage.bytes_sent / (1024*1024*1024)
        rx = usage.bytes_recv / (1024*1024*1024)
        return 'D:{0:.2f} U:{1:.2f}'.format(rx, tx)
