import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import PlayerAnalysis

class LinearRegression(PlayerAnalysis):
    def __init__(self, playerDataFile):
        super().__init__(playerDataFile)


    def linearRegressionByPlayer(self):
        self.playerData['GamingDt'] = pd.to_datetime(self.playerData['GamingDt'])
        self.playerData.sort_values(by='GamingDt', inplace=True)
        self.playerData['GamingDt_order'] = self.playerData.groupby('PlayerId')['GamingDt'].rank()

        # Create a dictionary to store the models
        models = {}
        
        # Group the data by player and fit a linear regression model
        for player, group in self.playerData.groupby('PlayerId'):
            x = group['GamingDt_order'].values.reshape(-1, 1)
            y = group['TotlTheo'].values
            model = LinearRegression().fit(x, y)
            models[player] = model
        return models


    def plotLinearRegression(self, models):
        # Create a drop-down list to select the player
        playerList = list(models.keys())
        root = tk.Tk()
        root.title("Linear Regression")
        playerDropDown = ttk.Combobox(root, values=playerList)
        playerDropDown.current(0)
        playerDropDown.pack()
        
        # Plot the linear regression for the selected player
        def onPlayerChange(*args):
            plt.figure()
            player = int(playerDropDown.get())
            model = models[player]
            data = self.playerData[self.playerData['PlayerId'] == player]
            x = data['GamingDt_order'].values.reshape(-1, 1)
            y = data['TotlTheo'].values
            plt.scatter(x,y)
            plt.plot(x, model.predict(x), color = 'red')
            plt.xlabel('Gaming Date')
            plt.ylabel('Total Theo')
            plt.title(f'Linear Regression for player {player}')
            plt.show()

        playerDropDown.bind("<<ComboboxSelected>>", onPlayerChange)
        root.protocol("WM_DELETE_WINDOW", root.destroy)
        root.mainloop()


analysis = PlayerAnalysis("/Users/kleib/Code/kleibo/Projects/Casino-Player-Analysis/Test_Data_10_Accts.csv")
models = analysis.linearRegressionByPlayer()
analysis.plotLinearRegression(models)