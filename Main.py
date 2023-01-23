import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PlayerAnalysis import PlayerAnalysis
from LinearRegression import PlayerLinearRegression
from KmeansClustering import PlayerKmeansClustering

class Main:
    def __init__(self):
        self.filepath = ""
        
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Player Analysis")
        
        # Create a button for each method
        self.selectFileButton = tk.Button(self.root, text="Select File", command=self.selectFile)
        self.selectFileButton.pack()
        
        self.runPlayerAnalysisButton = tk.Button(self.root, text="Run Player Analysis", command=self.runPlayerAnalysis)
        self.runPlayerAnalysisButton.pack()
        
        self.runLinearRegressionButton = tk.Button(self.root, text="Run Linear Regression", command=self.runLinearRegression)
        self.runLinearRegressionButton.pack()
        
        self.runKmeansClusteringButton = tk.Button(self.root, text="Run Kmeans Clustering", command=self.runKmeansClustering)
        self.runKmeansClusteringButton.pack()
        
        # Start the main loop
        self.root.mainloop()
    
    def selectFile(self):
        # Open a file dialog to select the player data file
        self.root = tk.Tk()
        self.root.withdraw()
        self.filepath = askopenfilename()
        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)


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
    
    

