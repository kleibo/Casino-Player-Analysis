import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from ipywidgets import widgets
import os


class PlayerAnalysis:
    def __init__(self, playerDataFile):
        self.playerData = pd.read_csv(playerDataFile)
        self.fileDirectory = os.path.dirname(playerDataFile)
        
        
    def theoPerVisit(self):
        theoPerVisit = self.playerData.groupby(['PlayerID']).agg({'TotlVisit': 'sum', 'TotlTheo': 'sum'})
        theoPerVisit['average_theo_per_visit'] = theoPerVisit['TotlTheo'] / theoPerVisit['TotlVisit']
        return theoPerVisit

    def descriptiveStats(self):
        data = self.theoPerVisit()
        descriptiveStats = data.describe()
        return descriptiveStats

    def linearRegressionByPlayer(self):
        self.playerData['GamingDt'] = pd.to_datetime(self.data['GamingDt'])
        self.playerData.sort_values(by='GamingDt', inplace=True)
        self.playerData['GamingDt_order'] = self.playerData.groupby('PlayerID')['GamingDt'].rank()

        # Create a dictionary to store the models
        models = {}
        
        # Group the data by player and fit a linear regression model
        for player, group in self.playerData.groupby('PlayerID'):
            x = group['GamingDt_order'].values.reshape(-1, 1)
            y = group['TotalTheo'].values
            model = LinearRegression().fit(x, y)
            models[player] = model
        return model


    def plotLinearRegression(self, models):
        # Create a drop-down list to select the player
        playerList = list(models.key())
        playerDropDown = widgets.Dropdown(options=playerList, value=playerList[0])
        display(playerDropDown)

        # Plot the linear regression for the selected player
        def onPlayerChange(change):
            plt.figure()
            player = change['new']
            model = models[player]
            data = self.playerData[self.playerData['PlayerID'] == player]
            x = data['GamingDt_order'].values.reshape(-1, 1)
            y = data['TotlTheo'].values
            plt.scatter(x,y)
            plt.plot(x, model.predict(x), color = 'red')
            plt.xlabel('Gaming Date Order')
            plt.ylabel('Total Theo')
            plt.title(f'Linear Regression for player {player}')
            plt.show()
        playerDropDown.observe(onPlayerChange, names='value')





