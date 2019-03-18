#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import sys


# In[3]:


if "__main__":
    data = pd.read_csv(sys.argv[1])
    by_rep = pd.Series("No-repair(Conditon 1 and 2)" if ((i==1) or (i==2)) else "Repair(Condition 3 and 4)" for i in data['Participant study:'])
    data['repair'] = by_rep
    sanity_dict = {1:3,2:1,3:3,4:1}
    sanity_dict_2 = {1:5,2:5,3:4,4:4}
    data_sanity_check = data[[sanity_dict[data['Participant study:'][i]] == data['Did this voice agent ever make a mistake?'][i] for i in range(0,(len(data)))]]
    data_sanity_check_2 = data_sanity_check[[sanity_dict_2[data_sanity_check['Participant study:'][i]] 
                                         == data_sanity_check['Did this agent ever try to repair a mistake it made?'][i] for i in data_sanity_check.index]]
    
    data_sanity_check_2.to_csv(sys.argv[1].split('.csv')[0]+"_modified.csv",index = False)

