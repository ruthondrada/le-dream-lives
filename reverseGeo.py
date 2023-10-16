import requests
import pandas as pd

#variables
excel_file_path = 'RecycleGoWhere Backend.xlsx'
sheet_name = 'Facilities List (Final)'
columns_to_read  = 'b,h'
filter_value = 'Blue Bin'
#columns_to_read = 'B'

headers = {"Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI5OGZjZjZmMzI4OTZjYzM3NWNmOGE3YmIwZmY5MDZjMiIsImlzcyI6Imh0dHA6Ly9pbnRlcm5hbC1hbGItb20tcHJkZXppdC1pdC0xMjIzNjk4OTkyLmFwLXNvdXRoZWFzdC0xLmVsYi5hbWF6b25hd3MuY29tL2FwaS92Mi91c2VyL3Bhc3N3b3JkIiwiaWF0IjoxNjk3Mjk5MDk0LCJleHAiOjE2OTc1NTgyOTQsIm5iZiI6MTY5NzI5OTA5NCwianRpIjoiRWRkRjZWVURMTWZMemp3WSIsInVzZXJfaWQiOjEyMjQsImZvcmV2ZXIiOmZhbHNlfQ.9qj5y26R19ZLLFhF4JHSb8GV33_c0Xwi3JV1g-2VJmI"}


try:
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name, usecols=columns_to_read)
    filtered_df = df[df['channel_name'] == filter_value]
    #print(filtered_df.dtypes)
    print(filtered_df)
    with open('output.txt', 'w') as file:
        for index, row in filtered_df.iterrows():
            channel_name = row['channel_name']
            postalcode = int(row['postcode'])
            str_postcode = str(postalcode)
            #file.write(channel_name + ":" + str_postcode )
            url = "https://www.onemap.gov.sg/api/common/elastic/search?searchVal="+ str_postcode + "&returnGeom=Y&getAddrDetails=Y"
            response = requests.request("GET", url, headers=headers)
            file.write(response.text+'\n')


        # print("Column1 Value:", channel_name)
        # print("Column2 Value:", str_postcode)

except pd.errors.ParserError as e:
    print("Error", e)
#print(filtered_df)



# for x in str_postcode:
      
#     # print(response.text)
#     with open('output.txt', 'w') as file:
#         file.write(response.text+'\n')
#TODO
#read from file. - done 
#filter by bluepin in channel_name - done
#read postal code - done

#write in Address as BLK Building - pending