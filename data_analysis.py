#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import os
import matplotlib.pyplot as plt
from collections import OrderedDict
import numpy as np
import seaborn as sns
import scipy.stats as stat


# In[ ]:


#clean and organize data

#all files will have this template for their path
file_path = './data/{file_name}'

#get all the csv file names in the data directory
files = os.listdir('./data')
csvs = []
for f in files:
    elems = f.split('.')
    if elems[1] == 'csv':
        csvs.append(f)
    
#create empty df to fill with cleaned data    
clean_df = pd.DataFrame(columns=['actual_answer', 'response', 'stimulus_duration', 'reaction_time', 'correct', 'vivid'])
  
#fill the new df with cleaned data from each individual csv    
for f in csvs:
    
    #get appropriate columns and remove nans
    datas = []
    df = pd.read_csv(file_path.format(file_name=f))
    datas.append(df['correct_resp'].tolist()[6:107])
    datas.append(df['key_resp.keys'].tolist()[6:107])
    datas.append(df['stim_interval'].tolist()[6:107])
    datas.append(df['key_resp.rt'].tolist()[6:107])
    datas.append(df['vivid_report'].tolist()[6:107])
    new_datas = []
    for d in datas:
        new_d = [i for i in d if not (pd.isnull(i))==True]
        new_datas.append(new_d)
    
    #create new df with cleaned columns
    new_df = pd.DataFrame(columns=['actual_answer', 'response', 'stimulus_duration', 'reaction_time', 'correct', 'vivid'])
    new_df['actual_answer'] = new_datas[0]
    new_df['response'] = new_datas[1]
    new_df['stimulus_duration'] = new_datas[2]
    new_df['reaction_time'] = new_datas[3]
    new_df['vivid'] = new_datas[4]
    
    #add cleaned dfs to overall df
    clean_df = pd.concat([clean_df, new_df], ignore_index=True)

#adds values to 'correct' col based on if the response matches the correct answer
for i in range(len(clean_df.index)):
    ans = clean_df.iloc[i]['actual_answer']
    resp = clean_df.iloc[i]['response']
    if resp == 'None':
        resp = 0
    if int(ans) == int(resp):
        clean_df.at[i, 'correct'] = 1
    else:
        clean_df.at[i, 'correct'] = 0
    
#print and save cleaned df
#print(clean_df)
clean_df.to_csv('./clean_data.csv')
print('Done with data cleaning!')


# In[ ]:


#stimulus type vs hit rate

print('Number of trials:', len(clean_df.index))

total = len(clean_df.index)
corr_sum = clean_df.loc[:,'correct'].sum()
hr = corr_sum/total
print('Overall hit rate:', hr)
print('One sample t-test for overall hit rate >0.5:', stat.ttest_1samp(list(clean_df['correct']), 0.5, alternative='greater'))


#tally number of each type of trial and number of correct answers
stim_corr = {}
for i in range(len(clean_df.index)):
    stim = clean_df.iloc[i]['actual_answer']
    corr = clean_df.iloc[i]['correct']
    if stim not in stim_corr:
        stim_corr[stim] = (corr, 1)
    else:
        stim_corr[stim] = (stim_corr[stim][0] + corr, stim_corr[stim][1] + 1)
        
#calculate hit rates for each type of stimuli        
stim_corr_prop = {}
for i in stim_corr:
    stim_corr_prop[i] = (stim_corr[i][0])/(stim_corr[i][1])

s = stim_corr_prop.keys()
c = stim_corr_prop.values()

#plot bar graphs
fig2, ax2 = plt.subplots(figsize=(10,10))
ax2.bar(s, c)
ax2.set_yticks(np.arange(0, 1.1, 0.1))
ax2.set_xticks((1, 2), ['Letters', 'Numbers'])
ax2.set_xlabel('Stimulus Type')
ax2.set_ylabel('Proportion Correct')
ax2.set_title('Stimulus Type vs Hit Rate')
plt.show()

#ind. samples t-test between stimuli types
letters = []
numbers = []

for i in range(len(clean_df.index)):
    ans = clean_df.iloc[i]['actual_answer']
    corr = clean_df.iloc[i]['correct']
    if ans == 1.0:
        letters.append(corr)
    elif ans == 2.0:
        numbers.append(corr)

print('Ind. samples t-test, letter-number:', stat.ttest_ind(letters, numbers))
print('One sample t-test for letter hit rate >0.5:', stat.ttest_1samp(letters, 0.5, alternative='greater'))
print('One sample t-test for number hit rate >0.5:', stat.ttest_1samp(numbers, 0.5, alternative='greater'))


# In[ ]:


#duration vs hit rate

print('Number of trials:', len(clean_df.index))

#tally number of each duration and number of correct answers
duration_correct = {}
for i in range(len(clean_df.index)):
    duration = clean_df.iloc[i]['stimulus_duration']
    if duration not in duration_correct:
        duration_correct[duration] = (clean_df.iloc[i]['correct'], 1)
    else:
        duration_correct[duration] = (duration_correct[duration][0] + clean_df.iloc[i]['correct'], duration_correct[duration][1] + 1)

#calculate hit rates for each duration 
duration_correct_prop = {}
for i in duration_correct:
    duration_correct_prop[i] = (duration_correct[i][0])/(duration_correct[i][1])
        
duration_correct_prop = OrderedDict(sorted(duration_correct_prop.items()))
d = list(duration_correct_prop.keys())
c = list(duration_correct_prop.values())

#plot regression between duration and hit rate
fig1, ax1 = plt.subplots(figsize=(15,10))
sns.regplot(x=d, y=c, ax=ax1)
sns.regplot(x=d, y=c, ax=ax1, logx=True, ci=False)
ax1.vlines(0.125, 0, 1, colors='m', linestyle='dotted')
ax1.set_xticks(np.arange(0.025, 0.525, 0.025))
plt.setp(ax1.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")
ax1.set_yticks(np.arange(0, 1.1, 0.1))
ax1.set_xlabel('Stimulus Duration (s)')
ax1.set_ylabel('Proportion Correct')
ax1.set_title('Duration vs Hit Rate')
plt.show()

#show summary statistics
print('duration vs hit-rate, pearson-r:', stat.pearsonr(d, c)[0])
print(stat.linregress(d, c))


# In[ ]:


#duration vs vividness

print('Number of trials:', len(clean_df.index))

#tally number of each duration and number of correct answers
duration_vivid = {}
for i in range(len(clean_df.index)):
    duration = clean_df.iloc[i]['stimulus_duration']
    vivid = clean_df.iloc[i]['vivid']
    if vivid == "[]":
        vivid = 1
    vivid = int(vivid)
    if duration not in duration_vivid:
        duration_vivid[duration] = (vivid, 1)
    else:
        duration_vivid[duration] = (int(duration_vivid[duration][0]) + int(vivid), duration_vivid[duration][1] + 1)

#calculate hit rates for each duration 
duration_vivid_prop = {}
for i in duration_vivid:
    duration_vivid_prop[i] = (duration_vivid[i][0])/(duration_vivid[i][1])
        
duration_vivid_prop = OrderedDict(sorted(duration_vivid_prop.items()))
d = list(duration_vivid_prop.keys())
v = list(duration_vivid_prop.values())

#plot regression between duration and hit rate
fig3, ax3 = plt.subplots(figsize=(15,10))
sns.regplot(x=d, y=v, ax=ax3)
sns.regplot(x=d, y=v, ax=ax3, logx=True, ci=False)
ax3.vlines(0.125, 0, 5, colors='m', linestyle='dotted')
ax3.set_xticks(np.arange(0.025, 0.525, 0.025))
plt.setp(ax3.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")
ax3.set_yticks(np.arange(0, 6.0, 1.0))
ax3.set_xlabel('Stimulus Duration (s)')
ax3.set_ylabel('Avg. Vividness Rating')
ax3.set_title('Duration vs Vividness')
plt.show()

#show summary statistics
print('duration vs avg. vividness, pearson-r:', stat.pearsonr(d, v)[0])
print(stat.linregress(d, v))


# In[ ]:


#vividness vs hit rate

df = clean_df
print('Number of trials:', len(df.index))

vivid_corr = {}
for i in range(len(df.index)):
    vivid = df.iloc[i]['vivid']
    corr = df.iloc[i]['correct']
    if vivid == "[]":
        vivid = 1
    vivid = int(vivid)
    if vivid not in vivid_corr:
        vivid_corr[vivid] = (corr, 1)
    else:
        vivid_corr[vivid] = (vivid_corr[vivid][0] + corr, vivid_corr[vivid][1] + 1)
        
vivid_corr_prop = {}
for i in vivid_corr:
    vivid_corr_prop[i] = (vivid_corr[i][0])/(vivid_corr[i][1])
vivid_corr = OrderedDict(sorted(vivid_corr_prop.items()))
v = list(vivid_corr.keys())
c = list(vivid_corr.values())

fig4, ax4 = plt.subplots(figsize=(10, 10))
sns.regplot(x=v, y=c, ax=ax4)
ax4.set_xticks(np.arange(1, len(v) + 1, 1), v)
ax4.set_yticks(np.arange(0, 1.1, 0.1))
ax4.set_xlabel('Vividness Ratings')
ax4.set_ylabel('Proportion Correct')
ax4.set_title('Vividness vs Hit Rate')
plt.show()

#show summary statistics
print('vividness vs hit rate, pearson-r:', stat.pearsonr(v, c)[0])
print(stat.linregress(v, c))


# In[ ]:


#stimulus type vs vividness 

df = clean_df
print('Number of trials:', len(df.index))

stim_vivid = {}
for i in range(len(df.index)):
    stim = df.iloc[i]['actual_answer']
    vivid = df.iloc[i]['vivid']
    if vivid == "[]":
        vivid = 1
    vivid = int(vivid)
    if stim not in stim_vivid:
        stim_vivid[stim] = (vivid, 1)
    else:
        stim_vivid[stim] = (stim_vivid[stim][0] + vivid, stim_vivid[stim][1] + 1)
        
stim_vivid_prop = {}
for i in stim_vivid:
    stim_vivid_prop[i] = (stim_vivid[i][0])/(stim_vivid[i][1])
s = stim_vivid_prop.keys()
v = stim_vivid_prop.values()

#plot bar graphs
fig5, ax5 = plt.subplots(figsize=(10,10))
ax5.bar(s, v)
ax5.set_yticks(np.arange(0, 5.5, 0.5))
ax5.set_xticks((1, 2), ['Letters', 'Numbers'])
ax5.set_xlabel('Stimulus Type')
ax5.set_ylabel('Avg. vividness rating')
ax5.set_title('Stimulus Type vs Vividness')
plt.show()

#ind. samples t-test between stimuli types
letters = []
numbers = []

for i in range(len(df.index)):
    ans = df.iloc[i]['actual_answer']
    vivid = df.iloc[i]['vivid']
    if vivid == "[]":
        vivid = 1
    vivid = int(vivid)
    if ans == 1.0:
        letters.append(vivid)
    elif ans == 2.0:
        numbers.append(vivid)

print('Ind. samples t-test, letter-number:', stat.ttest_ind(letters, numbers))


# In[ ]:




