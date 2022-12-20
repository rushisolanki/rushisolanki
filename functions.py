import requests
import datetime
from datetime import timedelta
import pandas as pd

def print_myname(name) :   
    return name



def Download_Delivery_Data(date_required):
    raw_url = "https://archives.nseindia.com/products/content/sec_bhavdata_full_"+date_required+".csv"
    print(raw_url)  
    try : 
        y = requests.get("https://archives.nseindia.com/products/content/sec_bhavdata_full_"+date_required+".csv", timeout=5)    
        url_content = y.content       
        csv_file = open(f"Data/{date_required}.csv", "wb")        
        csv_file.write(url_content)
        csv_file.close   
    except Exception as e:
        print(e)

def Download_Delivery_Data_For_N_DAYS(n):
    date = datetime.datetime.today()
    for i  in range (n): 
        date1 = date.strftime("%d%m%Y")
        Download_Delivery_Data(date1)
        date = date - timedelta(days=1)
    return i 



def List_To_String(s):
    a = s.split("-")
    a.reverse()
    str1 = ""
    for ele in a:
        str1 += ele
    return str1


def High_Delivery_Percent(selected_date):
    error_list = []
    FO_Stocks = pd.read_csv("fo_stocks.csv")
    List_of_stock_that_Max_deliveryforlast_20_days =[]
    date_ddmmyyyy = selected_date.strftime("%d%m%Y")   # ddmmyyyy format 
    a = selected_date
    for name in FO_Stocks.Symbol[:193]:
        start_date = a  
        date_ddmmyyyy = start_date.strftime("%d%m%Y")
        df_final = pd.read_csv(f"Data/{date_ddmmyyyy}.csv")   # read todays date
        df_final = df_final[df_final['SYMBOL'] == name]  # first raw stock specific 
                
        for i in range (30):            # for 30 days 
            try : 
                dd_raw_1 = pd.read_csv(f"Data/{date_ddmmyyyy}.csv")
                d_stock = dd_raw_1[dd_raw_1['SYMBOL'] == name]  # next n rows
                df_final = pd.concat([df_final,d_stock])
                
            except Exception as e:
                error_list.append(e)
            
            start_date = start_date - timedelta(days=1)
            date_ddmmyyyy = start_date.strftime("%d%m%Y")

        df = df_final[df_final[' DELIV_PER'] == df_final[" DELIV_PER"].max()]
        date_at_high_delivery = df.iat[0,2]    
        date_at_high_delivery = date_at_high_delivery.replace(" ","")
        date_for_comparision_instring = selected_date.strftime("%d-%b-%Y")
        
        if date_at_high_delivery == date_for_comparision_instring:
            List_of_stock_that_Max_deliveryforlast_20_days.append(name)
    return List_of_stock_that_Max_deliveryforlast_20_days






