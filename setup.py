#!/usr/bin/env python3
from setuptools import setup
from pathlib import Path
from os import path,sep
import shutil
#　home directory配下の.elodieに設定ファイルを設置
from_config = Path(f"{path.dirname(path.abspath(__file__))}{sep}config.ini-sample")
to_config = Path(f"{path.expanduser('~')}{sep}.elodie{sep}config.ini")
def copy(from_p,to_p):
    print(f"copy configfile")
    print(f"{from_p} > {to_p}\n")
    to_p.parent.mkdir(parents=True,exist_ok=True)
    if not to_p.is_file():
        shutil.copy(from_p,to_p)
copy(from_config,to_config)
setup()