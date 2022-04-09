from datetime import datetime as dts


class ModuleState:
    NORMAL = 0
    DEGRADED = 1
    WARNING = 2
    CRITICAL = 3


class BaseModule:
    def __init__(self, name: str):
        self._module_name = name
        self._state = ModuleState.NORMAL

    def get_data(self) -> str:
        return 'NOT_IMPLEMENTED'

    def get_state(self) -> int:
        return self._state

    def _set_state(self, state: int):
        self._state = state
