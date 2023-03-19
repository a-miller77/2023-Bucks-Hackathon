#Created By Aiden Miller

import pandas as pd
import numpy as np

name = np.array(['Free_Throw%', 'Field_Goal%', '2pt%', '3pt%', 'Iso', 'Pick', 'Post', 'Offball', 'AT_Ratio', 'TT_ratio'])#, 'TP_Ratio', 'SQavg'])
top = np.array(['ft_player', 'fg', 'empty', 'fg3', 'iso_pts', 'pick_pts', 'post_pts', 'offBall_pts', 'tov', 'tov'])#, 'tov', 'qsq'])
bottom = np.array(['fta', 'fga', 'empty', 'fga3', 'iso_actions', 'pick_actions', 'post_actions', 'offBall_actions', 'assistOppCreated', 'touches'])#, 'poss', 'poss'])

def create_stats_column(df, i, top=top, bottom=bottom, multi_var=False):
    top = top[i]
    bottom = bottom[i]
    row = np.zeros(0, dtype=float)
    for j in range(np.shape(df)[0]):
        if(multi_var):
            #print('2pt%' if name[i] != '2pt%' else 'multi')
            num = df[f'avg_fg'].iloc[j] - df[f'avg_fg3'].iloc[j]
            denom = df[f'avg_fga'].iloc[j] - df[f'avg_fga3'].iloc[j]
            result = num/denom
        else:
            result = df[f'avg_{top}'].iloc[j]/df[f'avg_{bottom}'].iloc[j]
        row = np.append(row, [result])
    return row

def update_df(df, top=top, bottom=bottom):
    for i in range(len(name)-1):
        name_temp = name[i]
        #print(name_temp, name[i])
        data = pd.DataFrame({f'{name_temp}': create_stats_column(df, i, top, bottom, multi_var=(True if name[i] == '2pt%' else False))})
        df = pd.concat([df, data], axis=1)
    print(np.shape(df))
    return df