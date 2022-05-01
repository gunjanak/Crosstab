from math import e
import numpy as np
import streamlit as st
import pandas as pd
import numpy as np
global output_df 
import templates



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
    global output_df
   
    st.title('Crosstab Analysis')
    status = False
    st.write(status)
    uploaded_file,status = load_data()
    st.write(status)
    if(status == True):
        df = read_data(uploaded_file)
        st.write(df.head())
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
                #print(columns[i])
                element = df[columns[i]]
                column_list.append(element)


            #Crosstab
            output_df = pd.crosstab(index_list,column_list)

            st.dataframe(output_df)
            menu = ['None','Template1','Template2']
            op = st.selectbox('Option',menu)
            if(op == 'Template1'):
                final_df = templates.template1(output_df)
                st.dataframe(final_df)
            elif (op == 'Template2'):
                final_df = templates.template2(output_df)
                st.dataframe(final_df)



if __name__ == '__main__':
    main() 