from modules.BaseModule import BaseModule
from datetime import datetime as dts
# from colorama import Fore, Back, Style


class DateTimeModule(BaseModule):
    def __init__(self, tz_format):
        self.tz_format = tz_format
        BaseModule.__init__( self,'DateTimeModule')

    def get_data(self):
        return dts.now().strftime(self.tz_format)
