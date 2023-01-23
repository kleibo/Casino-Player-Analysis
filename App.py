from tkinter import Tk
from tkinter.filedialog import askopenfilename
import PlayerAnalysis
import LinearRegression
# Open a file dialog to select the player data file
root = Tk()
root.withdraw()
filepath = askopenfilename()
root.protocol("WM_DELETE_WINDOW", root.destroy)
print(filepath)


# Create a PlayerAnalysis object with filepath directory
<<<<<<< HEAD
analysis = PlayerAnalysis.PlayerAnalysis(filepath)

=======
analysis = LinearRegression.PlayerLinearRegression(filepath)
>>>>>>> dev2
models = analysis.linearRegressionByPlayer()
analysis.plotLinearRegression(models)

# Save Results
# clustering.saveResults("Model")