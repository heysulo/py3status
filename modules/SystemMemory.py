from modules.BaseModule import BaseModule, ModuleState
import os
import psutil
# from colorama import Fore, Back, Style


class SystemMemory(BaseModule):
    def __init__(self, warn_level, crit_level):
        self._warn = warn_level
        self._crit = crit_level
        BaseModule.__init__(self,'SystemMemory')

    def get_data(self):
        memory = psutil.virtual_memory()
        total = memory.total / (1027*1024*1024)
        used = (memory.total - memory.available)/(1027*1024*1024)
        usage = (memory.total - memory.available) / memory.total * 100
        if usage > self._crit:
            BaseModule._set_state(self, ModuleState.CRITICAL)
        elif usage > self._warn:
            BaseModule._set_state(self,ModuleState.WARNING)
        else:
            BaseModule._set_state(self, ModuleState.NORMAL)
        return '{0:.2f}/{1:.2f} GB - {2:.2f}%'.format(used, total, usage)

