import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os


class PlayerAnalysis:
    def __init__(self, playerDataFile):
        self.playerData = pd.read_csv(playerDataFile)
        self.fileDirectory = os.path.dirname(playerDataFile)
        self.theoPerVisit = self.playerData.groupby(['PlayerID']).agg({'TotlVisit': 'sum', 'TotlTheo': 'sum'})
        self.theoPerVisit['average_theo_per_visit'] = self.theoPerVisit['TotlTheo'] / self.theoPerVisit['TotlVisit']
        
    def descriptiveStats(self):
        data = self.theoPerVisit['average_theo_per_visit']
        descriptiveStats = data.describe()
        return descriptiveStats

    def linear_regression(self, x, y):
        data = self.playerData
        model = LinearRegression()
        model.fit(data["GamingDt"], data["TotlTheo"])
        return model


class PlayerClustering:
    def __init__(self, playerDataFile):
        self.playerData = pd.read_csv(playerDataFile)
        self.fileDirectory = os.path.dirname(playerDataFile)
        self.model = None 

    def createClusters(self):
        # Use visit theo column in file
        totalTheoPerVisit = self.playerData.groupby("PlayerId")["TotlTheo"].mean()

        kmeans = KMeans(n_clusters=3)
        self.playerData['cluster'] = kmeans.fit_predict(totalTheoPerVisit[['TotlTheo']])

        clusters = totalTheoPerVisit['cluster']

