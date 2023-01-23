from tkinter import Tk
from tkinter.filedialog import askopenfilename
import PlayerAnalysis
import LinearRegression

# Open a file dialog to select the player data file
root = Tk()
root.withdraw()
filepath = askopenfilename()
print(filepath)
# Create a PlayerAnalysis object with filepath directory
# analysis = PlayerAnalysis.PlayerAnalysis(filepath)

test = LinearRegression(filepath)
models = test.linearRegressionbyPlayer()
test.plotLinearRegression(models)



# Save Results
# clustering.saveResults("Model")