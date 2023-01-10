import pymol2

# Create a PyMOL2 object
pymol = pymol2.PyMOL()

# Load the protein structure file
pymol.cmd.load("protein.pdb")

# Set the visualization style
pymol.cmd.show("cartoon")

# Set the background color
pymol.cmd.bg_color("white")

# Render the image
pymol.cmd.png("protein.png", width=600, height=600)

# Close the PyMOL2 object
pymol.close()
