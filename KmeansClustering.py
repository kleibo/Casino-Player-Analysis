import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
import matplotlib.pyplot as plt
import os
from PlayerAnalysis import PlayerAnalysis

class PlayerKmeansClustering(PlayerAnalysis):
    def __init__(self, playerDataFile):
        super().__init__(playerDataFile)
        self.file_directory = os.path.dirname(playerDataFile)
        self.model = None

    def clusterPlayers(self):
        # Create a new DataFrame with player's total theo and total visits
        playerSummary = self.playerData.groupby('PlayerId').agg({'TotlTheo': 'sum', 'TotlVisit': 'sum'})
        playerSummary.reset_index(inplace=True)

        # Scale the data
        playerSummary[['TotlTheo', 'TotlVisit']] = preprocessing.StandardScaler().fit_transform(playerSummary[['TotlTheo', 'TotlVisit']])

        # Run Kmeans with 4 clusters
        kmeans = KMeans(n_clusters=4)
        kmeans.fit(playerSummary[['TotlTheo', 'TotlVisit']])
        playerSummary['Cluster'] = kmeans.labels_


        return playerSummary

analysis = PlayerKmeansClustering("C:/Users/kleib/Code/kleibo/Projects/Casino-Player-Analysis/Test_Data_10_Accts.csv")
clustered_players = analysis.clusterPlayers()
