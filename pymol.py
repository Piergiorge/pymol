from pmg_tk.startup.pymol_launcher import run_pymol
from pmg_tk.startup import PyMOLStartup

def my_pymol_script():
    pymol = PyMOLStartup()
    pymol.cmd.load('example.pdb')
    pymol.cmd.color('white', 'example')
    pymol.cmd.show('surface', 'example')
    pymol.cmd.center('example')
    pymol.cmd.orient('example')
    pymol.cmd.zoom('example', 10)

run_pymol(my_pymol_script)
