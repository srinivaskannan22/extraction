import streamlit as st
import httpx
import asyncio
import pandas as pd
import json
from utils.display_utils  import Streamlit_Extraction

st.title('Extraction')
invoice1=st.radio(label='Type of search',options=['invoice','normal'])
file=st.file_uploader(label='File-upload',type=['jpg','xlsx','docx','csv','pdf',"png"])
button=st.button(label='onsubmit')

with open('data.json','rb')as json_file:
    in_dic=json.load(json_file) 

async def send_request(data,files):
    async with httpx.AsyncClient() as client:
        response = await client.post('http://127.0.0.1:8000/file_extraction',data=data,files=files)
        return response
    
def handle_response(data, file_type, is_bill):
    """Handles how the data should be displayed based on file type and invoice flag."""
    dis=Streamlit_Extraction(data)
    if is_bill == 'true':
        dis.show_bill_()
    else:
        handlers = {
            'text/csv': dis.show_csv,
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': dis.show_xlsx
        }
        handler = handlers.get(file_type, dis.show_generic)
        handler()

if button:
    if file is not None:
        with st.spinner("Fetching the data..."):
            try:
                # Prepare file and payload
                files = {'file': (file.name, file, file.type)}
                data = {'is_bill': in_dic.get(invoice1)}

                # Send request and process response
                response = asyncio.run(send_request(data, files))

                if response.status_code == 200:
                    response_data = response.json().get('data', [])
                    file_type = file.type
                    is_bill = in_dic.get(invoice1)

                    handle_response(data=response_data, file_type=file_type, is_bill=is_bill)
                else:
                    st.error("❌ Failed to retrieve data from the server.")
            except Exception as err:
                st.error(f"⚠️ An unexpected error occurred: {err}")
