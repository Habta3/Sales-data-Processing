#!/usr/bin/env python
# coding: utf-8

# In[7]:


'''
This will Load the Data from specified location as DataFrame
The data will be returned as pd.DataFrame
'''
#load the necessary packages
import json
import sys
from git import Object
import pandas as pd
from logger import Logger

class Data_Loader:
    
   
    def read_csv(self, csv_file) -> pd.DataFrame:
        """Csv file reader to open and read csv files into a panda dataframe.
        Args:
        -----
        csv_file: str - path of a json file

        Returns
        -------
        dataframe containing data extracted from the csv file"""
        return pd.read_csv(csv_file)
'''
load1=Data_Loader()
pd=load1.read_csv("E:\\10xAccademy_Practice\\Week 3\\Week 3 Challenge\\Data\\rossmann-store-sales\\store.csv")
pd.head()
'''


# In[ ]:




