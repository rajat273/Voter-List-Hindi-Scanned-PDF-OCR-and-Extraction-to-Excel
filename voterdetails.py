from PIL import Image
from pytesseract import image_to_string
import PyPDF2
import fitz
import pytesseract
import numpy as np
import pandas as pd
import PIL
from pdf2image import convert_from_path
import numpy as np
import cv2
from PIL import Image
import cv2
import pandas as pd
import re
import os  
import glob
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Specify the path where your PDF files are located
pdf_path = r"C:\Users\RaJat sharma\Downloads\cg10\*.pdf"
excel_folder = r"C:\Users\RaJat sharma\Downloads\shalendraji"
# Use glob to get a list of file paths matching the pattern
pdf_files = glob.glob(pdf_path)

# Print the list of PDF files
print("PDF files found:")
for pdf_file in pdf_files:
    print(pdf_file)
    

    # Extract numbers from the file name using regular expressions
    numbers = re.findall(r'\d+',pdf_file)

    # Assuming the numbers are the third and fifth groups of digits in the file name
    vidhansabha = numbers[3]
    bhag_no = numbers[5]

    
    pdf_document = fitz.open(pdf_file)
    pages = convert_from_path(pdf_file, poppler_path=r"C:\Users\RaJat sharma\Downloads\Release-24.02.0-0\poppler-24.02.0\Library\bin")
    
    x=847
    y=1885
    s1=190
    s2=577
    e1=755
    e2=256
    
    s3=865
    x1=500
    ex1=603
    
    a=1530
    b=380
    l=1240
    w=165
    er1=1400
    er2=938
    
    
    aa=1190
    bb=430
    ll=330
    ww=120
    err1=2310
    err2=983
    
    
    relation=[]
    
    anubha_num = []
    anubhag_name=[]
    names = []
    ages = []
    genders = []
    father_names = []
    address_numbers = []
    sex=[]
    age=[]
    number=[]
    kk=2
    makan=[]
    serial=[]
    sr=0
    for kk in range(2,pdf_document.page_count-1):
        im = pages[kk]
        im = np.array(im)
        im = cv2.resize(im, None, fx=5, fy=5, interpolation=cv2.INTER_CUBIC)
        _, im = cv2.threshold(im, 180, 255, cv2.THRESH_BINARY)
        
        im=Image.fromarray(im)
        head=im.crop((190,215,3000,350))
        
        headerp = pytesseract.image_to_string(head, lang='hin')
        headerp=headerp.split(":")[-1].strip() if ":" in headerp else (headerp.split(";")[-1].strip() if ";" in headerp else headerp)
        anubha_nu=headerp.split("-")[0].strip() if "-" in headerp else (headerp.split(" ")[-0].strip() if " " in headerp else headerp)
        
        anubhag_nam=headerp.split("-")[1].strip() if "-" in headerp else (headerp.split(" ")[1].strip() if " " in headerp else headerp)
        
        if "घटक" not in headerp:
            
            
            
            
            
            for j in range(10):
                for i in range(3):
                    cin = im.crop((s1,s2, s1+y, s2+x))
                    entry = pytesseract.image_to_string(cin, lang='hin')
                    
                    lines = entry.split("\n")
                    if len(lines) > 1:  # Check if there are at least 2 lines of text
                            g_name_line = lines[1].strip()
                            f_name = g_name_line.split(":")[-1].strip() if ":" in g_name_line else (g_name_line.split(";")[-1].strip() if ";" in g_name_line else g_name_line)
                            rel = g_name_line.split(" ")[0].strip() if " " in g_name_line[:9] else g_name_line
                            relation.append(rel)
                            
                            father_names.append(f_name)
                            name_line = lines[0].strip()
                            name = name_line.split(":")[-1].strip() if ":" in name_line else (name_line.split(";")[-1].strip() if ";" in name_line else name_line)
    
                            names.append(name)
                            cn1= im.crop((s1,s3,s1+y, s3+x1))
                            
                            text2 = pytesseract.image_to_string(cn1, lang='eng+hin')
                            
                            li = text2.split("\n")
                            sr+=1
                            serial.append(sr)
                            
                            
                            anubha_num.append(anubha_nu)
                            anubhag_name.append(anubhag_nam)
                            
                            if len(li)>1:
                                first = li[0].strip()
                                makn = first.split(":")[-1].strip() if ":" in first else (first.split(";")[-1].strip() if ";" in first else first)
    
                                makan.append(makn)
                                second = li[1].strip()
                                ages = second.split(":")[1].strip() if ":" in second[:7] else (second.split(";")[1].strip() if ";" in second else second)
                                sexs = second.split(":")[-1].strip() if ":" in second[-7:] else (second.split(";")[-1].strip() if ";" in second else second)
    
                                sex.append(sexs)
                                age.append(ages)
                                cn= im.crop((a,b, a+l, b+w))
                                
                                text2 = pytesseract.image_to_string(cn, lang='eng')
                                text2=text2.strip()
                                number.append(text2)
                                
                                
                                
                                
                                
                                
                            else:
                                names.pop()
                                father_names.pop()
                                serial.pop()
                                anubha_num.pop()
                                anubhag_name.pop()
                                relation.pop()
                            
                            s1=s1+y+e1
                            a=a+l+er1
                            aa=aa+ll+err1
                            
                   #cin.show()
                    #cn.show()
                s2=s2+x+e2
                b=b+w+er2
                s3=s3+x1+ex1
                bb=bb+ww+err2
                s1=190
                a=1530
                aa=1190
                
                
            s1=190
            a=1530
            x=847
            y=1885
            s1=190
            s2=577
            e1=755
            e2=256
            a=1530
            b=380
            l=1240
            w=165
            er1=1400
            er2=938
            s3=865
            x1=500
            ex1=603
            bb=430
        else:
     
             
            for j in range(10):
                for i in range(3):
                    cin = im.crop((s1,s2, s1+y, s2+x))
                    entry = pytesseract.image_to_string(cin, lang='hin')
                    
                    lines = entry.split("\n")
                    if len(lines) > 1:  # Check if there are at least 2 lines of text
                            g_name_line = lines[1].strip()
                            f_name = g_name_line.split(":")[-1].strip() if ":" in g_name_line else (g_name_line.split(";")[-1].strip() if ";" in g_name_line else g_name_line)
                            rel = g_name_line.split(" ")[0].strip() if " " in g_name_line[:9] else g_name_line
                            relation.append(rel)
                            
                            father_names.append(f_name)
                            name_line = lines[0].strip()
                            name = name_line.split(":")[-1].strip() if ":" in name_line else (name_line.split(";")[-1].strip() if ";" in name_line else name_line)
    
                            names.append(name)
                            cn1= im.crop((s1,s3,s1+y, s3+x1))
                            
                            text2 = pytesseract.image_to_string(cn1, lang='eng+hin')
                            
                            li = text2.split("\n")
                            sr+=1
                            serial.append(sr)
                            
                            sb=im.crop((aa,bb,aa+ll,bb+ww))
                            
                            sbt= pytesseract.image_to_string(sb,config='--psm 6 outputbase digits')
                            anubha_num.append(sbt)
                            anubhag_name.append(None)
                            
                            if len(li)>1:
                                first = li[0].strip()
                                makn = first.split(":")[-1].strip() if ":" in first else (first.split(";")[-1].strip() if ";" in first else first)
    
                                makan.append(makn)
                                second = li[1].strip()
                                ages = second.split(":")[1].strip() if ":" in second[:7] else (second.split(";")[1].strip() if ";" in second else second)
                                sexs = second.split(":")[-1].strip() if ":" in second[-7:] else (second.split(";")[-1].strip() if ";" in second else second)
    
                                sex.append(sexs)
                                age.append(ages)
                                
    
                                
                                
                                
                                
                                
                                cn= im.crop((a,b, a+l, b+w))
                                
                                text2 = pytesseract.image_to_string(cn, lang='eng')
                                text2=text2.strip()
                                number.append(text2)
                                
                                sb=im.crop((aa,bb,aa+ll,bb+ww))
                                
                                
                                
                                
                            else:
                                names.pop()
                                father_names.pop()
                                serial.pop()
                                anubha_num.pop()
                                anubhag_name.pop()
                                relation.pop()
                            
                            s1=s1+y+e1
                            a=a+l+er1
                            aa=aa+ll+err1
                            
                   #cin.show()
                    #cn.show()
                s2=s2+x+e2
                b=b+w+er2
                s3=s3+x1+ex1
                bb=bb+ww+err2
                s1=190
                a=1530
                aa=1190
                
                
            s1=190
            a=1530
            x=847
            y=1885
            s1=190
            s2=577
            e1=755
            e2=256
            a=1530
            b=380
            l=1240
            w=165
            er1=1400
            er2=938
            s3=865
            x1=500
            ex1=603
            bb=430
            
     
  
    
    
    # Assuming you have three lists: names, father_names, and numbers
    data = {'sr':serial,'Name': names,'Relation':relation, 'Father Name': father_names, 'Number': number,'aged': age,'sex':sex,'makan': makan,'Anubhag_number':anubha_num,"Anubhag_name":anubhag_name}
    
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data)
    df['age'] = df['aged'].apply(lambda x: x.split(' ')[0] if ' ' in x else x)
    df.drop(columns=['aged'], inplace=True)
    df['vidhansabha'] = vidhansabha
    df['bhag_no'] = bhag_no
    
    df['Anubhag_number'].replace(['।', ' ','','|'], 1, inplace=True)
    pdf_base_name = os.path.basename(pdf_file)
    excel_file_name = os.path.splitext(pdf_base_name)[0] + ".xlsx"
    output_file = os.path.join(excel_folder, excel_file_name)
    
    df.to_excel(output_file, index=False)

    
    
    
    
    print(f"Data extracted from '{pdf_file}' and saved to '{excel_file_name}'")
    
    


excel_files = [file for file in os.listdir(excel_folder) if file.endswith('.xlsx')]


dfs = []


for file in excel_files:
    file_path = os.path.join(excel_folder, file)
    df = pd.read_excel(file_path, header=0)  
    dfs.append(df)

# Combine all DataFrames in the list into one DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Save the combined DataFrame to a new Excel file
output_file = vidhansabha+'combined_152voter_data_with_header.xlsx'
combined_df.to_excel(output_file, index=False)

print(f"Combined data with headers saved to '{output_file}'.")






    

