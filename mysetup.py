# mysetup.py
from distutils.core import setup
import glob
import py2exe

setup(windows=["game_of_life.py"],
      data_files=[("templates",
                   ["template", "origin_template"])],
)