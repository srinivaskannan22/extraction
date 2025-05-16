from services.extraction import Extraction
from fastapi import FastAPI,File,UploadFile,Form
from typing import Literal 
import time
from pydantic import BaseModel
from typing import Annotated
from fastapi import Body
from fastapi import HTTPException
app=FastAPI()


@app.post('/file_extraction')
async def fileextraction(is_bill: bool = Form(False),file: UploadFile = File(...)):
    content = await file.read()
    iextraction = Extraction(content)
    if not is_bill:
        extension_map = {
            '.png': iextraction.gemini_extraction,
            '.jpeg': iextraction.image_extraction,
            '.xlsx': iextraction._extract_excel,
            '.pdf': iextraction.process_pdf,
            '.docx': iextraction.docx_extraction,
            '.csv': iextraction.csv_extraction,
            
        }
        for ext, method in extension_map.items():
            if file.filename.endswith(ext):
                return method()
        raise HTTPException(status_code=400,detail='this file is not support')
    else:
        return iextraction.gemini_extraction()       
    
    