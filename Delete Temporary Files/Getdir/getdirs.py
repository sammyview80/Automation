import os 
import pathlib


class Dir():

    """
    Get the user directory and the temp directory.

    Dir().use_dir for user directory.
    Dir().get_temp_dir for %temp% dir.
    """
    def __init__(self):
        self.rootDir = os.path.abspath(os.sep)

    @property
    def user_dir(self):
        return str(pathlib.Path.home())

    @property
    def get_temp_dir(self):
        self.getTempDir = os.path.join(self.user_dir, 'AppData\Local\Temp')
        return self.getTempDir
    
    @property
    def get_prefetch_dir(self):
        self.getPrefetchDir = os.path.join(self.user_dir, 'Windows\Prefetch')
        return self.getPrefetchDir