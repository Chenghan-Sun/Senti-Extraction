import pandas as pd
from typing import Dict
import numpy as np


class MissingValue(object):
    def __init__(self, pd_df: pd.DataFrame) -> None:
        self.na_count_dict = {}
        self.na_index_dict = {}
        self.data = pd_df

    def __str__(self) -> Dict:
        return self.na_count_dict
    
    def __getitem__(self, item) -> int:
        return self.na_count_dict[item]

    def missing_value_summary(self, verbose=False):
        self.na_list = self.data.isna().sum(axis=0)
        self.na_count=0
        for obj in self.na_list.index:
            if self.na_list[obj] != 0:
                self.na_count_dict[obj] = self.na_list[obj]
                self.na_count+=1
                if verbose:
                    print("In column\033[91m {}\033[00m , "
                          "we have\033[91m {}\033[00m missing values.".format(obj, self.na_list[obj]))
        if not self.na_count_dict:
            if verbose:
                print("No missing value found!")
        return self.na_count_dict,self.na_count,self.na_list

    def missing_value_enumerator(self):
        self.name=['textID','text','selected_text','sentiment']
        self.na_index_dict = {}
        self.na_index_dict_e = []
        self.na_index_dict_line={}
        #self.na_index_dict_e=pd.DataFrame(columns=self.name)
        #self.na_index_dict_e.columns=self.na_index_dict.columns
        if not self.na_count_dict:
            raise Exception("Please use function missing_value_summary() first.")
        if self.na_count!=0:
            self.na_index_dict=self.data.isna()*1
            for item in self.name:
                if self.na_index_dict[item].sum()!=0:
                    self.na_index_dict_e.append(self.na_index_dict[self.na_index_dict[item]>0])
            self.na_index=[self.na_index_dict_e[0].index[0]]
            for ind in range(1,len(self.na_index_dict_e)):
                if self.na_index_dict_e[ind].index[0]!=self.na_index_dict_e[ind-1].index[0]:
                    self.na_index.append(self.na_index_dict_e[ind].index[0])
            for r in self.na_index:
                print(self.data.iloc[int(r)])
        return self.na_index,self.na_index_dict_line
