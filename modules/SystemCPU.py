from modules.BaseModule import BaseModule, ModuleState
import os
import psutil
# from colorama import Fore, Back, Style


class SystemCPU(BaseModule):
    def __init__(self, warn_level, crit_level):
        self._warn = warn_level
        self._crit = crit_level
        BaseModule.__init__(self,'SystemCPU')

    def get_data(self):
        usage = psutil.cpu_percent(interval=None)
        if usage > self._crit:
            BaseModule._set_state(self, ModuleState.CRITICAL)
        elif usage > self._warn:
            BaseModule._set_state(self,ModuleState.WARNING)
        else:
            BaseModule._set_state(self, ModuleState.NORMAL)
        return '{0:.2f}%'.format(usage)

