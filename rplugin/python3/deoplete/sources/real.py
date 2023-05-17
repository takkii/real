import gc
import os
import re
import traceback
import yaml
from deoplete.source.base import Base
from operator import itemgetter
from typing import Optional


# Use Config project
class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name: Optional[str] = 'real'
        self.filetypes = ['ruby']
        mark_synbol: Optional[str] = '[real-time]'
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
            # Use vim-plug, This Config load path is Neovim ENV.
            config_path: Optional[str] = '~/.neovim/plugged/config/'
            path_file: Optional[str] = '~/.neovim/plugged/config/load.yml'

            # Standard config/folder/file Loading PATH.
            config_load: Optional[str] = '~/config/'
            load_file: Optional[str] = '~/config/load.yml'
            folder_load: Optional[str] = 'Folder_Load'
            file_load: Optional[str] = 'File_Load'

            # Set the dictionary.
            if os.path.isdir(config_path):
                with open(os.path.expanduser(path_file)) as yml:
                    config = yaml.safe_load(yml)
                    yml_load = os.path.expanduser(config[folder_load])

            elif os.path.isdir(config_load):
                with open(os.path.expanduser(load_file)) as yml:
                    config = yaml.safe_load(yml)
                    yml_load = os.path.expanduser(config[folder_load])

            else:
                raise ValueError("None, Please Check the Config Folder.")

            # Get Receiver/Ruby Method Complete.
            if os.path.isdir(yml_load):
                with open(os.path.expanduser(config[file_load])) as r_method:
                    data = list(r_method.readlines())
                    data_ruby: Optional[list] = [s.rstrip() for s in data]
                    complete: Optional[list] = data_ruby
                    complete.sort(key=itemgetter(0))
                    return complete

            # Config Folder not found.
            else:
                raise ValueError("None, Please Check the Config Folder.")

        # TraceBack.
        except Exception:
            # Load/Create LogFile.
            except_folder: Optional[str] = 'Except_Folder_load'
            except_file: Optional[str] = 'Except_File_load'
            real: Optional[str] = os.path.expanduser(config[except_folder])
            debug_word: Optional[str] = os.path.expanduser(config[except_file])

            # Load the dictionary.
            if os.path.isdir(real):
                with open(debug_word, 'a') as log_py:
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
