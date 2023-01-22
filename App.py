from tkinter import Tk
from tkinter.filedialog import askopenfilename
import PlayerClustering

# Open a file dialog to select the player data file
root = Tk()
root.withdraw()
filepath = askopenfilename()

# Create a PlayerClustering object and cluster the players
clustering = PlayerClustering.PlayerClustering(filepath)
clustering.createClusters()

# Plot the clusters
clustering.plotClusters()

# Save Results
# clustering.saveResults("Model")