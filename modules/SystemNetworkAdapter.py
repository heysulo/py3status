from socket import AddressFamily

from modules.BaseModule import BaseModule, ModuleState
import os
import psutil


# from colorama import Fore, Back, Style


class SystemNetworkAdapter(BaseModule):
    def __init__(self, adapter, eth=True):
        self.adapter = adapter
        self.adapter_type = 'ETH' if eth else 'WLAN'
        BaseModule.__init__(self, 'SystemNetworkAdapter')

    def get_data(self):
        network = psutil.net_if_addrs()[self.adapter]
        ipaddress = ''
        for registration in network:
            if registration.family == AddressFamily.AF_INET:
                ipaddress = registration.address
                break
        if ipaddress == '':
            BaseModule._set_state(self, ModuleState.CRITICAL)
        else:
            BaseModule._set_state(self, ModuleState.NORMAL)
        speed = psutil.net_if_stats()[self.adapter].speed
        if self.get_state() == ModuleState.NORMAL:
            return '{}: {} ({}MBps)'.format(self.adapter_type, ipaddress, speed)
        return '{}: Disconnected'.format(self.adapter_type)
