import gc
import numpy as np
import os
import platform
import re
import sys
import traceback
import warnings

from deoplete.source.base import Base
from operator import itemgetter
from typing import Optional

warnings.filterwarnings('ignore')


# Use Config project
class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name: Optional[str] = 'real'
        self.filetypes = ['ruby']
        mark_synbol: Optional[str] = '[python: ' + str(
            platform.python_version()) + ']'
        self.mark = str(mark_synbol)
        ruby_match = [r'\.[a-zA-Z0-9_?!]*|[a-zA-Z]\w*::\w*']
        slash_no_match = [r'[;/[^¥/]\*/]']
        self.input_pattern = '|'.join(ruby_match + slash_no_match)
        self.rank = 500

    def get_complete_position(self, context):
        ruby_complete: Optional[str] = '[a-zA-Z0-9_?!]*$'
        m = re.search(ruby_complete, context['input'])
        return m.start() if m else -1

    def gather_candidates(self, context):
        try:
            # It doesn't support python4 yet.
            py_mj = sys.version_info[0]
            py_mi = sys.version_info[1]

            # 3.5 and higher, 4.x or less,python version is required.
            if (py_mj == 3 and py_mi > 4) or (py_mj < 4):
                # Settings, $HOME/dict path is true/false folder search.
                loc_t: Optional[str] = 'real/'

                paths = [
                    os.path.expanduser(os.path.join(p, loc_t)) for p in [
                        '~/GitHub/dict/load/ruby/',
                        '~/.vim/plugged/dict/load/ruby/',
                        '~/.neovim/plugged/dict/load/ruby/'
                    ]
                ]

                path = next(p for p in paths if os.path.exists(p))
                el_dict: Optional[str] = 'method.txt'
                el_mod_fn = os.path.join(path, el_dict)

                # Get Receiver/diamond behavior.
                with open(el_mod_fn) as rb_mt:
                    dev_py: Optional[list] = list(rb_mt.readlines())
                    sort_ruby = np.array(dev_py).tolist()
                    dev_comp: Optional[list] = [s.rstrip() for s in sort_ruby]
                    sorted(dev_comp, key=itemgetter(0))
                    return dev_comp

            # Python_VERSION: 3.5 or higher and 4.x or less.
            else:
                raise ValueError("VERSION: 3.5 and higher, 4.x or less")

        # TraceBack.
        except Exception:
            # real file path.
            filepath = os.path.expanduser(
                "~/.vim/plugged/real/rplugin/python3/deoplete/sources/real.py")

            basename_without_ext = os.path.splitext(
                os.path.basename(filepath))[0]
            filename = (str(basename_without_ext) + "_log")

            # Load/Create LogFile.
            real: Optional[str] = str(filename)
            db_w: Optional[str] = os.path.expanduser('~/' + filename +
                                                     '/debug.log')

            # Load the dictionary.
            if os.path.isdir(real):
                with open(db_w, 'a') as log_py:
                    traceback.print_exc(file=log_py)

                    # throw except.
                    raise RuntimeError from None

            # real Foler not found.
            else:
                raise ValueError("None, Please Check the real Folder.")

        # Custom Exception.
        except ValueError as ext:
            print(ext)
            raise RuntimeError from None

        # Once Exec.
        finally:
            # GC collection.
            gc.collect()
