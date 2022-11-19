import pandas as pd

import numpy as np

import seaborn as sns

import matplotlib

from matplotlib import pyplot as plt

from matplotlib import rcParams



from pandas import Series, DataFrame

from cycler import cycler

import datetime as dt

import plotly.figure_factory as ff

import plotly.express as px

from datetime import date, timedelta



import nbconvert

import textwrap



from nbconvert import PDFExporter



plt.rcParams["figure.figsize"] = (5,5)



pd.set_option('display.max_rows', None)

pd.set_option('display.max_columns', None)



df_process = pd.read_csv("./reference.csv")



sns.set_theme(style="ticks")



# Get matplotlib figure and axes objects

fig, ax1 = plt.subplots(figsize=(15,7.5))



# parameters for first y-axis

ax1.plot(df_process['CV'], df_process['UV 1_280 (mAU)'], color='blue')

ax1.set_xlabel('CV')

ax1.set_ylabel('UV (mAU)')

ax1.set_ylim([-1,250])

ax1.set_xlim([55,88])

ax1.set_yticks(np.arange(0,250,50))

ax1.set_xticks((55,56, 59, 62, 65, 66.4,67.9,69.4,70.9,72.4,73.9,74.84,76.84,78.84,80.84, 85))

ax1.set_xticklabels(ax1.get_xticks(),rotation=90)

plt.grid()



axB = ax1.twiny()

axB.plot(df_process['CV'], df_process['UV 1_280 (mAU)'], color='blue')

axB.set_xlabel('<batch Name> Process Stage')

axB.set_ylabel('UV (mAU)')

axB.set_ylim([-1,250])

axB.set_xlim([55,88])

axB.set_yticks(np.arange(0,250,50))

axB.set_xticks((55,56, 59, 62, 65, 66.4,67.9,69.4,70.9,72.4,73.9,74.84,76.84,78.84,80.84, 85))

axB.set_xticklabels(('Load','Post-Load Wash','Grad I (0-26%)','Grad II (26% Hold)',\

                     'Grad III (26%-27.2%)','Eln-1A1(27.2% Hold)','1A3','1A5','1B2','1B4', '1C1',\

                     'Grad IV (100% B)','Regeneration','Clean-In-Process','Water Wash','Storage'),rotation=90)



# parameters for second y-axis

ax2 = ax1.twinx()

ax2.plot(df_process['CV'], df_process['Cond (mS/cm)'], color='orange')

ax2.set_ylabel('Conductivity (mS/cm)')

ax2.set_ylim([-1,250])

ax2.set_yticks(np.arange(0,260,10))



# parameters for third y-axis

ax3 = ax1.twinx()

ax3.plot(df_process['CV'], df_process['pH'], color='red')

ax3.spines['right'].set_position(('outward', 60))

ax3.set_ylabel('pH')

ax3.set_ylim([0,15])

ax3.set_yticks(np.arange(0,15,0.5))



# parameters for fourth y-axis

ax4 = ax1.twinx()

ax4.plot(df_process['CV'], df_process['Conc B (%)'], color='green', alpha=0.5)

ax4.spines['right'].set_position(('axes', -0.1))

ax4.set_ylabel('Conc B (%)', labelpad=-45)

ax4.set_ylim([-1,101])

ax4.set_yticks(np.arange(0,101,4))



# parameters for fourth y-axis

ax5 = ax1.twinx()

ax5.plot(df_process['CV'], df_process['PreC pressure (Mpa)'], color='black')

ax5.spines['right'].set_position(('axes', -0.18))

ax5.set_ylabel('PreC pressure (Mpa)', labelpad=-45)

ax5.set_ylim([0,1])

ax5.set_yticks(np.arange(0,1,0.05))



# parameters for fourth y-axis

ax6 = ax1.twinx()

ax6.plot(df_process['CV'], df_process['DeltaC pressure (Mpa)'], color='violet', alpha=0.5)

ax6.spines['right'].set_position(('outward', 120))

ax6.set_ylabel('DeltaC pressure (Mpa)', labelpad=10)

ax6.set_ylim([0,1])

ax6.set_yticks(np.arange(0,1,0.05))



# legends for all y-axes

ax1.legend(['UV (mAU)'],ncol=1 , bbox_to_anchor=(0.15, 1.40), facecolor="white" )

ax2.legend(['Conductivity (mS/cm)'],ncol=1, bbox_to_anchor=(0.35, 1.40), facecolor="white")

ax3.legend(['pH'],ncol=1 , bbox_to_anchor=(0.45, 1.40), facecolor="white")

ax4.legend(['Conc B (%)'],ncol=1 , bbox_to_anchor=(0.6, 1.40), facecolor="white")

ax5.legend(['PreC pressure (Mpa)'],ncol=1 , bbox_to_anchor=(0.8, 1.40), facecolor="white")

ax6.legend(['DeltaC pressure (Mpa)'],ncol=1 , bbox_to_anchor=(1, 1.40), facecolor="white")



# saving plot to a PNG file

plt.savefig(".\output.png", dpi=1600, bbox_inches='tight')
