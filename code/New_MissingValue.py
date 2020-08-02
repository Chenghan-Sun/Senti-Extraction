{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from typing import Dict\n",
    "import numpy as np\n",
    "\n",
    "\n",
    "class MissingValue(object):\n",
    "    def __init__(self, pd_df: pd.DataFrame) -> None:\n",
    "        self.na_count_dict = {}\n",
    "        self.na_index_dict = {}\n",
    "        self.data = pd_df\n",
    "\n",
    "    def __str__(self) -> Dict:\n",
    "        return self.na_count_dict\n",
    "    \n",
    "    def __getitem__(self, item) -> int:\n",
    "        return self.na_count_dict[item]\n",
    "\n",
    "    def missing_value_summary(self, verbose=False):\n",
    "        self.na_list = self.data.isna().sum(axis=0)\n",
    "        self.na_count=0\n",
    "        for obj in self.na_list.index:\n",
    "            if self.na_list[obj] != 0:\n",
    "                self.na_count_dict[obj] = self.na_list[obj]\n",
    "                self.na_count+=1\n",
    "                if verbose:\n",
    "                    print(\"In column\\033[91m {}\\033[00m , \"\n",
    "                          \"we have\\033[91m {}\\033[00m missing values.\".format(obj, self.na_list[obj]))\n",
    "        if not self.na_count_dict:\n",
    "            if verbose:\n",
    "                print(\"No missing value found!\")\n",
    "        return self.na_count_dict,self.na_count,self.na_list\n",
    "\n",
    "    def missing_value_enumerator(self):\n",
    "        self.name=['textID','text','selected_text','sentiment']\n",
    "        self.na_index_dict = {}\n",
    "        self.na_index_dict_e = []\n",
    "        self.na_index_dict_line={}\n",
    "        #self.na_index_dict_e=pd.DataFrame(columns=self.name)\n",
    "        #self.na_index_dict_e.columns=self.na_index_dict.columns\n",
    "        if not self.na_count_dict:\n",
    "            raise Exception(\"Please use function missing_value_summary() first.\")\n",
    "        if self.na_count!=0:\n",
    "            self.na_index_dict=self.data.isna()*1\n",
    "            for item in self.name:\n",
    "                if self.na_index_dict[item].sum()!=0:\n",
    "                    self.na_index_dict_e.append(self.na_index_dict[self.na_index_dict[item]>0])\n",
    "            self.na_index=[self.na_index_dict_e[0].index[0]]\n",
    "            for ind in range(1,len(self.na_index_dict_e)):\n",
    "                if self.na_index_dict_e[ind].index[0]!=self.na_index_dict_e[ind-1].index[0]:\n",
    "                    self.na_index.append(self.na_index_dict_e[ind].index[0])\n",
    "            for r in self.na_index:\n",
    "                print(self.data.iloc[int(r)])\n",
    "        return self.na_index,self.na_index_dict_line\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
