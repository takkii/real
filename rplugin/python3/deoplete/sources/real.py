import gc
import os
import re
import yaml
import traceback
from operator import itemgetter
from deoplete.source.base import Base


# Use Config project
class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'Real'
        self.filetypes = ['ruby']
        mark_synbol = '[Real]'
        self.mark = str(mark_synbol)
        ruby_match = [r'\.[a-zA-Z0-9_?!]*|[a-zA-Z]\w*::\w*']
        slash_no_match = [r'[;/[^¥/]\*/]']
        self.input_pattern = '|'.join(ruby_match + slash_no_match)
        self.rank = 500

    def get_complete_position(self, context):
        ruby_complete = '[a-zA-Z0-9_?!]*$'
        m = re.search(ruby_complete, context['input'])
        return m.start() if m else -1

    def gather_candidates(self, context):
        try:
            # Set the dictionary.
            with open(os.path.expanduser("~/config/load.yml")) as yml:
                config = yaml.safe_load(yml)
                yml_load = os.path.expanduser(config['Folder_Load_Path'])

            # Get the dictionary.
            if os.path.isdir(yml_load):
                ruby_method = open(os.path.expanduser(
                    config['File_Load_Path']))

            # The dictionary not found.
            else:
                raise ValueError("Please, Check the path of real.")

        # TraceBack
        except Exception:
            with open("real_error.log", 'a') as log_py:
                traceback.print_exc(file=log_py)
                raise RuntimeError from None

        # Custom Exception
        except ValueError as ext:
            print(ext)
            raise RuntimeError from None

        # ruby dictionary list complete
        else:
            # read
            data = list(ruby_method.readlines())
            data_ruby = [s.rstrip() for s in data]
            ruby_method.close()

            # sort and itemgetter
            complete = data_ruby
            complete.sort(key=itemgetter(0))

            # result
            return complete

            # GC exec
            gc.collect()
