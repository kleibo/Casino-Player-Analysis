from tkinter import Tk
from tkinter.filedialog import askopenfilename
import PlayerAnalysis

# Open a file dialog to select the player data file
root = Tk()
root.withdraw()
filepath = askopenfilename()

# Create a PlayerAnalysis object with filepath directory
analysis = PlayerAnalysis.PlayerAnalysis(filepath)

analysis.linearRegressionByPlayer()


# Save Results
# clustering.saveResults("Model")