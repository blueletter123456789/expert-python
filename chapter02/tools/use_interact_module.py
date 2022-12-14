# IPythonを使用する場合
import IPython
IPython.embed()

# bpythonを使用する場合
import bpython
bpython.embed()

# pypythonを使用する場合
from ptpython.repl import embed
embed(globals(), locals())
