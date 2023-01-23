import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
import matplotlib.pyplot as plt
import plotly.express as px
from PlayerAnalysis import PlayerAnalysis

class PlayerKmeansClustering(PlayerAnalysis):
    def __init__(self, playerDataFile):
        super().__init__(playerDataFile)


    def clusterPlayers(self):
        # Create a new DataFrame with player's total theo and total visits
        playerSummary = self.playerData.groupby('PlayerId').agg({'TotlTheo': 'sum', 'TotlVisit': 'sum'})
        playerSummary.reset_index(inplace=True)

        # Scale the data
        playerSummary[['TotlTheo', 'TotlVisit']] = preprocessing.StandardScaler().fit_transform(playerSummary[['TotlTheo', 'TotlVisit']])

        # Run Kmeans with 4 clusters
        kmeans = KMeans(n_clusters=4)
        kmeans.fit(playerSummary[['TotlTheo', 'TotlVisit']])
        playerSummary['Cluster'] = kmeans.predict(playerSummary[['TotlTheo', 'TotlVisit']])


        return playerSummary

    def plotClusterMatPlot(self):
        # Create the scatterplot
        clusteredPlayers = self.clusterPlayers()

        plt.scatter(clusteredPlayers['TotlVisit'], clusteredPlayers['TotlTheo'], c=clusteredPlayers['Cluster'])

        # Add labels for the x and y axis
        plt.xlabel('Total Visit')
        plt.ylabel('Total Theo')

        # Add a title for the plot
        plt.title('Player Kmeans Clustering')

        # Show plot
        plt.show()

    def plotClusterspx(self):
        clusteredPlayers = self.clusterPlayers()
        fig = px.scatter(clusteredPlayers, x='TotlVisit', y='TotlTheo', color='Cluster', hover_name="PlayerId")
        fig.show()

analysis = PlayerKmeansClustering("C:/Users/kleib/Code/kleibo/Projects/Casino Data/Test_Data_UnClean - Shortened.csv")
# analysis.plotCluster()
analysis.plotClusterspx()
