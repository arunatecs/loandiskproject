import requests



import json

import pandas as pd


"""   To display the adjusted loan scedule values         """

def display_values(res):
        
        data = res.json()

        
        adjusted_loan_detail =[]
        response = data["response"]
        result=response['Results']
        #print(result)

        
        counter = 0
      
        for i in response['Results']:
               
                while(counter < len(i)):
                    adjusted_loan_detail.append([
                        i[counter]['LoanId'],
                        i[counter]['Date'],
                        i[counter]['Description'],
                        i[counter]['Principal'],
                        i[counter]['Interest'],
                        i[counter]['Fees'],
                        i[counter]['Penalty'],
                        i[counter]['Due'],
                        i[counter]['Paid'],
                        i[counter]['Pending Due'],
                        i[counter]['Total Due'],
                        i[counter]['Principal Due'],


                    ])
                  
                    
                
                    counter +=  1
               

        adjusted_loan_df = pd.DataFrame(data=adjusted_loan_detail, columns=['LoanId', 'Date','Description',
                                    'Principal','Interest','Fees','Penalty','Due','Paid','Pending Due','Total Due','Principal Due'])
        
        adjusted_loan_df.to_csv('adjusted_loan.csv')


def main():

    public_key = 12815

    branch = 15735
 

    loan_id = 1786909

    

    header = {
        'content-type': 'application/json',
        'Authorization': 'Fn5eHUrSX6vD6ckykekD52NyamrfpR4gHBYgDk8f',
    }

    
    try:

        API_BASE_URL = f'https://api-main.loandisk.com/{public_key}/{branch}/loan/adjusted_loan_schedule/{loan_id}/from/0/count/50'
            
        res = requests.get(API_BASE_URL,headers = header)
            
        display_values(res)
       

    except requests.exceptions.HTTPError as e:
        print('Unable to retrieve values.')
        print(e.response.text)
 

if __name__ == '__main__':
    main()
