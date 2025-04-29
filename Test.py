from pylab import *
import numpy as np

år = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]
lønn_Per = [272.55]
lønn_Amalie = [272.55]
vekst_Per = 1.015
vekst_Amalie = 1.023
total_lønn_Per = []
total_lønn_Amalie = []

for i in range(0, len(år)+1):
    lønn_Per.append(lønn_Per[i]*vekst_Per)
    lønn_Amalie.append(lønn_Amalie[i]*vekst_Amalie)

for i in range(0, len(år) + 1):
    for b in range(0, 1701):
        total_lønn_Per.append(lønn_Per[i])

for i in range(0, len(år) + 1):
    for b in range(0, 1701):
        total_lønn_Amalie.append(lønn_Amalie[i])

print(round(sum(total_lønn_Per), 1))
print(round(sum(total_lønn_Amalie), 1))