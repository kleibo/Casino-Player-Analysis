from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pandas as pd
import os
class PlayerAnalysis:
    def __init__(self, playerDataFile):
        self.playerData = pd.read_csv(playerDataFile)
        
    def theoPerVisit(self):
        theoPerVisit = self.playerData.groupby(['PlayerId']).agg({'TotlVisit': 'sum', 'TotlTheo': 'sum'})
        theoPerVisit['average_theo_per_visit'] = theoPerVisit['TotlTheo'] / theoPerVisit['TotlVisit']
        return theoPerVisit

    def descriptiveStats(self):
        data = self.theoPerVisit()
        descriptiveStats = data.describe()
        return descriptiveStats

        





