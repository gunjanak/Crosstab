
import numpy as np
import streamlit as st


import pandas as pd





def load_data():
    st.write("Upload a csv file")
    uploaded_file = st.file_uploader("Choose a file",'csv')
    st.write(uploaded_file)
    if(uploaded_file == None):
        status = False
    else:
        status = True

    to_return = [uploaded_file,status]
    return to_return

def read_data(uploaded_file):
    df = pd.read_csv(uploaded_file)

    return df


def main():
    st.title('Crosstab Analysis')
    status = False
    st.write(status)
    uploaded_file,status = load_data()
    st.write(status)
    if(status == True):
        df = read_data(uploaded_file)

        st.write('List of columns')
        st.write(df.columns)
        col_list = list(df.columns.values)
        
        length = len(col_list)
        st.write(length)


        #columns with categorical data
        col_list = df.select_dtypes(include=['object']).columns
        index_list = col_list
        indexx = st.multiselect('Which column you want as index:',index_list)
        st.write('You Selected: ',indexx)


        
        st.write('Select column for column')
        columns = st.multiselect('Select for column:',col_list)
        st.write('You Selected: ',columns)
        
        if(len(indexx)>0 and len(columns)>0) :

            #No of index selected
            no_of_index = len(indexx)

            #no of columns selected
            no_of_columns = len(columns)

            #creating array of index selected to be fed in crosstab function
            index_list = []
            for i in range(no_of_index):
                print(indexx[i])
                element = df[indexx[i]]
                index_list.append(element)


            #creating array of index selected to be fed in crosstab function
            column_list = []
            for i in range(no_of_columns):
                print(columns[i])
                element = df[columns[i]]
                column_list.append(element)



            output_df = pd.crosstab(index_list,column_list)
            #print(output_df)

            st.write(output_df)
            
            st.write('For Major index only')
            i=1
            st.write(output_df.index.get_level_values(0).unique())
            particular_index = st.multiselect('Select value of index of your choice:',output_df.index.get_level_values(0).unique())
            st.write(type(particular_index))
            st.write(output_df.loc[particular_index])
            #https://towardsdatascience.com/working-with-multi-index-pandas-dataframes-f64d2e2c3e02

            st.write('For nested index')
            particular_index = st.multiselect('Select value of index of your choice:',output_df.index)
            st.write(type(particular_index))
            st.write(output_df.loc[particular_index])

            







      


    


if __name__ == '__main__':
    main()