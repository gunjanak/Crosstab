from math import e
import numpy as np
import streamlit as st
import pandas as pd
import numpy as np
global output_df 


def template1(output_df):
    pec_df = output_df.div(output_df.sum(axis=1), axis=0)
    pec_df = round(pec_df*100,2)
    final_df = pd.concat([output_df,pec_df],axis=1)
    no_cols = len(output_df.columns)
    empty_list = []
    for i in range(no_cols):
        empty_list.append(output_df.values[:,i])
        empty_list.append(pec_df.values[:,i])

    final_df = pd.DataFrame(empty_list).T
    final_df.index = output_df.index
    sum = output_df.sum(axis=1)

    cols = output_df.columns
    new_cols = []
    for col in cols:
        
        count_tuple = (col,'Count')
        new_cols.append(count_tuple)
        pec_tuple = (col,"Pec")
        new_cols.append(pec_tuple)

    final_df.columns=pd.MultiIndex.from_tuples(new_cols)
    final_df['Sum'] = sum
    final_df.loc['Total'] = final_df.sum()
    total_values = final_df.loc['Total'].values
    final_total_values = []
    for i in range(len(total_values)-1):
        if((i+1)%2 != 0):
            total_values[i+1] = round((total_values[i]/total_values[-1])*100,2)
            final_total_values.append(total_values[i+1])
        

 

    return final_df


def template2(output_df):
    pec_df = output_df.div(output_df.sum(axis=0), axis=1)
    pec_df = round(pec_df*100,2)
    final_df = pd.concat([output_df,pec_df],axis=1)
    no_cols = len(output_df.columns)
    empty_list = []
    for i in range(no_cols):
        empty_list.append(output_df.values[:,i])
        empty_list.append(pec_df.values[:,i])
    final_df = pd.DataFrame(empty_list).T
    final_df.index = output_df.index
    
    sum = output_df.sum(axis=1)
    cols = output_df.columns
    new_cols = []
    for col in cols:
        count_tuple = (col,'Count')
        new_cols.append(count_tuple)
        pec_tuple = (col,"Pec")
        new_cols.append(pec_tuple)

    
    final_df.columns=pd.MultiIndex.from_tuples(new_cols)
    final_df['Sum'] = sum
    final_df.loc['Total'] = final_df.sum()
    total_values = final_df.loc['Total'].values
    final_total_values = []
    for i in range(len(total_values)-1):
        if((i+1)%2 != 0):
            total_values[i+1] = round((total_values[i]/total_values[-1])*100,2)
            final_total_values.append(total_values[i+1])
        




    return final_df