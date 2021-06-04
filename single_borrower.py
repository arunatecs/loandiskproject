import requests


import json
import pandas as pd


"""   To display the borrower values         """

def display_values(res,borrower_id):
        
        data = res.json()

        response = data["response"]
        
        borrower_list =[]

       
        

        for i in response['Results']:
               
                
                
               
                    
                    result = dict((k, i[k]) for k in ['custom_field_5819', 'custom_field_5820', 'custom_field_5821'
                                                                 ,'custom_field_5822', 'custom_field_5823', 'custom_field_5824',
                                                                 'custom_field_6985', 'custom_field_7080', 'custom_field_7102'
                                                                 ,'custom_field_7103', 'custom_field_7104', 'custom_field_7106']
                                        if k in i)

                    key_5819 = 'custom_field_5819'   
                    key_5820 = 'custom_field_5820'
                    key_5821 = 'custom_field_5821' 
                    key_5822 = 'custom_field_5822'
                    key_5823 = 'custom_field_5823'
                    key_5824 = 'custom_field_5824'  
                    key_6985 = 'custom_field_6985'   
                    key_7080 = 'custom_field_7080'
                    key_7102 = 'custom_field_7102' 
                    key_7103 = 'custom_field_7103'
                    key_7104 = 'custom_field_7104'
                    key_7106 = 'custom_field_7106'   

                    if key_5819 in result.keys():
                        
                        field_5819 = i['custom_field_5819']
                   
                    else:
                        
                        field_5819 = ''
                   
                      

                    if key_5820 in result.keys():
                        
                        field_5820 = i['custom_field_5820']
                   
                    else:
                        
                        field_5820 = ''
                    
                      

                    if key_5821 in result.keys():
                      
                       field_5821 = i['custom_field_5821']
                    
                    else:
                        
                        field_5821 = ''
                    
                    

                    if key_5822 in result.keys():
                       
                        field_5822 = i['custom_field_5822']
                    
                    else:
                        
                        field_5822 = ''
                    
                    

                    if key_5823 in result.keys():
                        
                        field_5823 = i['custom_field_5823']
                    
                    else:
                        
                        field_5823 = ''
                     

                    if key_5824 in result.keys():
                        
                        field_5824 = i['custom_field_5824']
                    
                    else:
                        
                        field_5824 = ''
                    
                    if key_6985 in result.keys():
                        
                        field_6985 = i['custom_field_6985']
                   
                    else:
                        
                        field_6985 = ''
                   
                      

                    if key_7080 in result.keys():
                        
                        field_7080 = i['custom_field_7080']
                   
                    else:
                        
                        field_7080 = ''
                    
                      

                    if key_7102 in result.keys():
                      
                       field_7102 = i['custom_field_7102']
                    
                    else:
                        
                        field_7102 = ''
                    
                    

                    if key_7103 in result.keys():
                       
                        field_7103 = i['custom_field_7103']
                    
                    else:
                        
                        field_7103 = ''
                    
                    

                    if key_7104 in result.keys():
                        
                        field_7104 = i['custom_field_7104']
                    
                    else:
                        
                        field_7104 = ''
                     

                    if key_7106 in result.keys():
                        
                        field_7106 = i['custom_field_7106']
                    
                    else:
                        
                        field_7106 = ''
                   
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
                                        i ['borrower_photo'],
                                        field_5819,
                                        field_5820,
                                        field_5821,
                                        field_5822,
                                        field_5823,
                                        field_5824,
                                        field_6985,
                                        field_7080,
                                        field_7102,
                                        field_7103,
                                        field_7104,
                                        field_7106,

                                    ])
                   
                    
                    borrower_df = pd.DataFrame(data=borrower_list, columns=['borrower_id','borrower_country',
                            'borrower_fullname','borrower_firstname','borrower_lastname','borrower_business_name',
                            'borrower_unique_number','borrower_gender','borrower_title','borrower_mobile','borrower_email',
                            'borrower_dob','borrower_address','borrower_city','borrower_province','borrower_zipcode',
                            'borrower_landline','borrower_working_status', 'borrower_credit_score', 'borrower_description',
                            'borrower_access_ids','borrower_photo','custom_field_5819','custom_field_5820','custom_field_5821'
                            ,'custom_field_5822','custom_field_5823','custom_field_5824','custom_field_6985','custom_field_7080',
                            'custom_field_7102','custom_field_7103','custom_field_7104','custom_field_7106'])
                    borrower_df.to_csv('data/single_borrower_'+str(borrower_id)+'.csv',index=None)
        

  
def main():

    public_key = 12815

    branch = 15735

    borrower_id = 1573244

    

    
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
