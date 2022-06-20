#produces two main output files: overall_clean.csv has all the data from every trial, and summary_clean.csv
#has only one row per participant with relevant averages

import os
import pandas as pd
import numpy as np

#all raw files will have this template for their path
file_path = './data/{file_name}'

#get all the csv file names in the data directory
files = os.listdir('./data')
csvs = []
for f in files:
    elems = f.split('.')
    if elems[1] == 'csv':
        csvs.append(f)     
print('Files:', csvs)

#set up overall_clean csv
entire_clean_data = pd.DataFrame(columns=['participant', 'correct_resp', 'resp', 'stim_interval', 
                                          'rt', 'vivid_report', 'correct'])

for csv in csvs:
    
    #open and extract relevant columns from each participant's data
    curr_file = pd.read_csv(file_path.format(file_name = csv))
    new_df = curr_file[['participant', 'correct_resp', 'key_resp.keys', 
                        'stim_interval', 'key_resp.rt', 'vivid_report']].copy()
    
    #drop the intro and exit routines
    new_df = new_df.drop([0, 1, 2, 3, 4, 5, 106])
    new_df = new_df.reset_index(drop=True)
    
    #put vividness response on the same line as the content response for each trial
    for i in range(len(new_df.index)):
        if i%2 == 0:
            new_df.at[i, 'vivid_report'] = new_df.at[i + 1, 'vivid_report']
        else:
            new_df = new_df.drop([i])
    new_df = new_df.reset_index(drop=True)
    
    #get rid of any trials where the response was not recorded and correctly format content responses
    for i in range(len(new_df.index)):
        resp = new_df.at[i, 'key_resp.keys']
        viv = new_df.at[i, 'vivid_report']
        if resp == 'None' or viv == '[]':
            new_df = new_df.drop([i])
        else:
            new_df.at[i, 'key_resp.keys'] = float(resp)
    new_df = new_df.reset_index(drop=True)
    
    #tally correct responses and add to df
    corr = []
    for i in range(len(new_df.index)):
        resp = new_df.at[i, 'key_resp.keys']
        ans = new_df.at[i, 'correct_resp']
        if resp == ans:
            corr.append(1.0)
        else:
            corr.append(0.0)
    new_df.insert(loc=len(new_df.columns), column='correct', value=corr, allow_duplicates=True)
    
    #save each participant's cleaned dataset
    new_df = new_df.rename(columns={'key_resp.keys':'resp', 'key_resp.rt':'rt'})
    save_path = './clean_data/{save_name}.csv'
    new_df.to_csv(save_path.format(save_name=csv.split('.')[0] + '_clean'), index=False)
    
    #append to overall dataset
    entire_clean_data = pd.concat([new_df, entire_clean_data], ignore_index=True)
    entire_clean_data.to_csv(save_path.format(save_name='overall_clean'), index=False)
    
print('Done cleaning files!')

#all clean files will have this template for their path
file_path = './clean_data/{file_name}'

#get all the csv file names in the clean_data directory
files = os.listdir('./clean_data')
csvs = []
for f in files:
    elems = f.split('.')
    if elems[1] == 'csv':
        csvs.append(f)
csvs.remove('overall_clean.csv')
if 'summary_clean.csv' in csvs:
    csvs.remove('summary_clean.csv')

#set up the summary csv
summary_clean = pd.DataFrame(columns=['participant', 'tms', 'session', 'hit_rate', 'error_rate', 'avg_rt', 'avg_vividness'])


for i in range(len(csvs)):
    
    #read in each file
    file = csvs[i]
    df = pd.read_csv(file_path.format(file_name=file))
    
    #extract relevant info into lists
    participant = df.at[0, 'participant']
    rt = df[['rt']].values.tolist()
    vivid = df[['vivid_report']].values.tolist()
    corr = df[['correct']].values.tolist()
    for j in range(len(df.index)):
        rt[j] = float(rt[j][0])
        vivid[j] = float(vivid[j][0])
        corr[j] = float(corr[j][0])           
    
    #add to summary df
    summary_clean.at[i, 'participant'] = participant
    summary_clean.at[i, 'tms'] = 0
    summary_clean.at[i, 'session'] = 0
    summary_clean.at[i, 'hit_rate'] = sum(corr)/len(corr)
    summary_clean.at[i, 'error_rate'] = 1 - (sum(corr)/len(corr))
    summary_clean.at[i, 'avg_vividness'] = sum(vivid)/len(vivid)
    valid_rt = []
    for k in range(len(corr)):
        if corr[k] == 1.0:
            valid_rt.append(rt[k])
    summary_clean.at[i, 'avg_rt'] = sum(valid_rt)/len(valid_rt)
    
#save summary df
summary_clean.to_csv('./clean_data/summary_clean.csv', index=False) 
print(summary_clean)