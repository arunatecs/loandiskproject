import requests


import json
import pandas as pd


"""   To display the borrower values         """

def display_values(res,borrower_id):
        
        data = res.json()

        response = data["response"]
        
        borrower_list =[]

       
        

        for i in response['Results']:
               
                
                    
                    if (i.get("custom_field_5819") !=None or i.get("custom_field_5820") !=None or 
                        i.get("custom_field_5821") !=None or i.get("custom_field_5822") !=None or 
                        i.get("custom_field_5823") !=None or i.get("custom_field_5824") !=None ):
                   
                       
                        borrower_list.append([
                                i['borrower_id'],
                                i['borrower_country'],
                                i['borrower_fullname'],
                                i['borrower_firstname'],
                                i['borrower_lastname'],
                                i['borrower_business_name'],
                                i['borrower_unique_number'],
                                i['borrower_gender'],
                                i['borrower_title'],
                                i['borrower_mobile'],
                                i['borrower_email'],
                                i['borrower_dob'],
                                i['borrower_address'],
                                i['borrower_city'],
                                i['borrower_province'],
                                i['borrower_zipcode'],
                                i['borrower_landline'],
                                i['borrower_working_status'],
                                i['borrower_credit_score'],
                                i['borrower_description'],
                                i['borrower_access_ids'],
                                i['borrower_photo'],
                                i["custom_field_5819"],
                                i["custom_field_5820"],
                                i['custom_field_5821'],
                                i['custom_field_5822'],
                                i['custom_field_5823'],
                                i['custom_field_5824'],
                                

                            ])
                            
                    else:

                            borrower_list.append([
                                i['borrower_id'],
                                i['borrower_country'],
                                i['borrower_fullname'],
                                i['borrower_firstname'],
                                i['borrower_lastname'],
                                i['borrower_business_name'],
                                i['borrower_unique_number'],
                                i['borrower_gender'],
                                i['borrower_title'],
                                i['borrower_mobile'],
                                i['borrower_email'],
                                i['borrower_dob'],
                                i['borrower_address'],
                                i['borrower_city'],
                                i['borrower_province'],
                                i['borrower_zipcode'],
                                i['borrower_landline'],
                                i['borrower_working_status'],
                                i['borrower_credit_score'],
                                i['borrower_description'],
                                i['borrower_access_ids'],
                                i['borrower_photo'],
                                '',
                                '',
                                '',
                                '',
                                '',
                                '',
                                
                            ])
                        
                   
                    
                    borrower_df = pd.DataFrame(data=borrower_list, columns=['borrower_id','borrower_country',
                    'borrower_fullname','borrower_firstname','borrower_lastname','borrower_business_name',
                    'borrower_unique_number','borrower_gender','borrower_title','borrower_mobile','borrower_email',
                    'borrower_dob','borrower_address','borrower_city','borrower_province','borrower_zipcode',
                    'borrower_landline','borrower_working_status', 'borrower_credit_score', 'borrower_description',
                    'borrower_access_ids','borrower_photo','custom_field_5819','custom_field_5820','custom_field_5821'
                    ,'custom_field_5822','custom_field_5823','custom_field_5824'])

                    borrower_df.to_csv('single_borrower_'+str(borrower_id)+'.csv',index=None)
        

  
def main():

    public_key = 12815

    branch = 15735

    borrower_id = 1216911

    

    
    API_BASE_URL = f'https://api-main.loandisk.com/{public_key}/{branch}/borrower/{borrower_id}'

    header = {
        'content-type': 'application/json',
        'Authorization': 'Fn5eHUrSX6vD6ckykekD52NyamrfpR4gHBYgDk8f',
    }

    
    try:
        
        res = requests.get(API_BASE_URL,headers = header)
           
        display_values(res,borrower_id)
       

    except requests.exceptions.HTTPError as e:
        print('Unable to retrieve values.')
        print(e.response.text)
 

if __name__ == '__main__':
    main()
