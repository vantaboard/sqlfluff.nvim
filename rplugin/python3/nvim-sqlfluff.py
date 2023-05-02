import pynvim
from sqlfluff import fix

@pynvim.plugin
class Formatter(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.function('SQLFluffFormat', sync=True)
    def sqlfluff_format():
        sql = "\n".join(self.nvim.current.buffer)
        self.nvim.current.buffer[:] = fix(sql, 'postgres', None, None, None, True).split('\n')
