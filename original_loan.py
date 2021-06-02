import requests

from requests.auth import HTTPBasicAuth

import json



"""   To display the orginal loan scedule values         """

def display_values(res):
        
        data = res.json()

        #print(res)

        json_str = json.dumps(data,indent =4)
        
        print(f'display the original loan scedule values:\n{json_str}')
       

  
def main():

    public_key = 12815

    branch = 15735
 

    loan_id_list = [1786909,1621672,1569248,1566174]

    #API_BASE_URL = f'https://api-main.loandisk.com/{public_key}/{branch}/loan/original_loan_schedule/{loan_id}/from/0/count/50'

    header = {
        'content-type': 'application/json',
        'Authorization': 'Fn5eHUrSX6vD6ckykekD52NyamrfpR4gHBYgDk8f',
    }

    
    try:

        for item in loan_id_list:

            API_BASE_URL = f'https://api-main.loandisk.com/{public_key}/{branch}/loan/original_loan_schedule/{item}/from/0/count/50'
            
            res = requests.get(API_BASE_URL,headers = header)
            
            display_values(res)
       

    except requests.exceptions.HTTPError as e:
        print('Unable to retrieve values.')
        print(e.response.text)
 

if __name__ == '__main__':
    main()
