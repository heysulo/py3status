from modules.BaseModule import BaseModule, ModuleState
import os
# from colorama import Fore, Back, Style


class SystemLoad(BaseModule):
    def __init__(self, warn_level, crit_level):
        self._warn = warn_level
        self._crit = crit_level
        BaseModule.__init__(self,'SystemLoad')

    def get_data(self):
        load = os.getloadavg()[0]
        if load > self._crit:
            BaseModule._set_state(self, ModuleState.CRITICAL)
        elif load > self._warn:
            BaseModule._set_state(self,ModuleState.WARNING)
        else:
            BaseModule._set_state(self, ModuleState.NORMAL)
        return '{0:.2f}'.format(load)

