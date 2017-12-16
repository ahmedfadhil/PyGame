import cx_Freeze
from cx_Freeze import setup, Executable
import os

executables = [cx_Freeze.Executable("pg.py")]

cx_Freeze.setup(
    name="Obstacles",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["racecar.png"],
                           "excludes": ['tcl', 'ttk', 'tkinter', 'Tkinter']}},
    executables=executables
)
