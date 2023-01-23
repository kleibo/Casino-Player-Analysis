import tkinter as tk
from tkinter.filedialog import askopenfilename
from PlayerAnalysis import PlayerAnalysis
from LinearRegression import PlayerLinearRegression
from KmeansClustering import PlayerKmeansClustering

class Main:
    def __init__(self):
        # Open a file dialog to select the player data file
        root = tk.Tk()
        root.withdraw()
        self.filepath = askopenfilename()
        root.protocol("WM_DELETE_WINDOW", root.destroy)

    def runPlayerAnalysis(self):
        file = PlayerAnalysis(self.filepath)
        file.descriptiveStats()

    def runLinearRegression(self):
        file = PlayerLinearRegression(self.filepath)
        models = file.linearRegressionByPlayer()
        file.plotLinearRegression(models)

    def runKmeansClustering(self):
        file = PlayerKmeansClustering(self.filepath)
        clusteredPlayers = file.clusterPlayers()
        file.plotClusterspx()

# Create a PlayerAnalysis object with filepath directory
if __name__ == '__main__':
    main = Main()
    main.runLinearRegression()
    


# Save Results
# clustering.saveResults("Model")