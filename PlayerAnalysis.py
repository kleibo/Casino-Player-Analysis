import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import os


class PlayerAnalysis:
    def __init__(self, playerDataFile):
        self.playerData = pd.read_csv(playerDataFile)
        self.fileDirectory = os.path.dirname(playerDataFile)
        
        
    def theoPerVisit(self):
        theoPerVisit = self.playerData.groupby(['PlayerId']).agg({'TotlVisit': 'sum', 'TotlTheo': 'sum'})
        theoPerVisit['average_theo_per_visit'] = theoPerVisit['TotlTheo'] / theoPerVisit['TotlVisit']
        return theoPerVisit

    def descriptiveStats(self):
        data = self.theoPerVisit()
        descriptiveStats = data.describe()
        return descriptiveStats

        





