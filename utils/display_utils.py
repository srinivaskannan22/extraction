
import streamlit as st
import pandas as pd

class Streamlit_Extraction:
        def __init__(self,data):
                self.data=data

        def show_bill_(self):
                invoice=pd.json_normalize(self.data)
                invoice=invoice.transpose()
                st.dataframe(invoice)

        def show_csv(self):  
                datafr=pd.DataFrame(self.data)
                st.dataframe(datafr)
                st.balloons()

        def show_xlsx(self):
                dfs = [pd.DataFrame(sheet_data[1:], columns=sheet_data[0]) for sheet_data in self.data]
                combined_df = pd.concat(dfs, ignore_index=True)
                st.dataframe(combined_df)  

        def show_generic(self):
                st.success(self.data)
                st.balloons()