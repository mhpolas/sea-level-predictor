import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x1=df['Year']
    x2=df['CSIRO Adjusted Sea Level']
    # Create scatter plot
    plt.scatter(x1,x2 )

    # Create first line of best fit
    line1 = linregress(x1, x2)
    xPred = np.arange(x1.min(),2050,1)
    yPred = xPred*line1.slope + line1.intercept

    plt.plot(xPred,yPred,'r')

    # Create second line of best fit
  
    df_2nd = df[df['Year'] >= 2000]
    df_2nd_x1 = df_2nd['Year']
    df_2nd_x2 = df_2nd['CSIRO Adjusted Sea Level']
  
    line2 = linregress(df_2nd_x1, df_2nd_x2)
    xPred2 = np.arange(2000,2050,1)
    yPred2 = xPred2*line2.slope + line2.intercept

    plt.plot(xPred2,yPred2)

    # Add labels and title
  
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()