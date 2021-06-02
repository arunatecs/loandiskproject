import requests

from requests.auth import HTTPBasicAuth

import json



"""   To display the borrower values         """

def display_values(res):
        
        data = res.json()

        json_str = json.dumps(data,indent =4)
        
        print(f'display the borrower values:\n{json_str}')
       

  
def main():

    public_key = 12815

    branch = 15735

    borrower_id = 1573265
    
    
    API_BASE_URL = f'https://api-main.loandisk.com/{public_key}/{branch}/loan/borrower/{borrower_id}/from/0/count/50'

    header = {
        'content-type': 'application/json',
        'Authorization': 'Fn5eHUrSX6vD6ckykekD52NyamrfpR4gHBYgDk8f',
    }

    
    try:
        
        res = requests.get(API_BASE_URL,headers = header)
           
        display_values(res)
       

    except requests.exceptions.HTTPError as e:
        print('Unable to retrieve values.')
        print(e.response.text)
 

if __name__ == '__main__':
    main()
