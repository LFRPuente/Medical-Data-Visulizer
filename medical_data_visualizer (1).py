import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight'] = (df['weight']/((df['height']/100)**2) > 25) * 1

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df[['cholesterol','gluc']] = (df[['cholesterol','gluc']] > 1) * 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df,id_vars='id', value_vars=['active','alco','cholesterol', 'gluc', 'overweight', 'smoke'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.

    df_cat = pd.melt(df,id_vars=['id','cardio'], value_vars=['active','alco','cholesterol', 'gluc', 'overweight', 'smoke'])

    
    # Draw the catplot with 'sns.catplot()'
    
    fig, (ax1,ax2) = plt.subplots(1,2, figsize = (15,5), sharey = 'row', gridspec_kw = {'wspace':0, 'hspace':0})

    sns.countplot(data=df_cat[df_cat['cardio'] == 1], x='variable', hue='value', ax = ax1)
    sns.countplot(data=df_cat[df_cat['cardio'] == 0], x='variable', hue='value', ax = ax2)
    ax1.set(ylabel='total')
    ax2.set(ylabel='total')  
    

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(df_heat.corr(), dtype=np.bool))



    # Set up the matplotlib figure
    fig, ax = plt.subplots(1,1)

    # Draw the heatmap with 'sns.heatmap()'

    sns.heatmap(corr,mask=mask, cmap="rocket", ax=ax, annot=True, fmt=".1f")

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
