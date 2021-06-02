import requests

import json
import pandas as pd


"""   To display list of repayment values         """

def display_values(res):
        
        data = res.json()
        
        response = data["response"]
        
        repayment_list =[]

       
        counter =0

        for i in response['Results']:
               
                while(counter < len(i)):
                    
                    
                        repayment_list.append([
                                i[counter]['repayment_id'],
                                i[counter]['loan_id'],
                                i[counter]['repayment_amount'],
                                i[counter]['loan_repayment_method_id'],
                                i[counter]['repayment_collected_date'],
                                i[counter]['collector_id'],
                                i[counter]['loan_do_not_adjust_remaining_pro_rata'],
                                i[counter]['repayment_adjust_remaining_schedule'],
                                i[counter]['repayment_manual_composition'],
                                i[counter]['principal_repayment_amount'],
                                i[counter]['interest_repayment_amount'],
                                i[counter]['fees_repayment_amount'],
                                i[counter]['penalty_repayment_amount'],
                                i[counter]['repayment_description'],
                            ])
                            
                        counter += 1
                        repayment_df = pd.DataFrame(data=repayment_list, columns=['repayment_id' ,'loan_id' ,'repayment_amount' ,
                                                    'loan_repayment_method_id' ,'repayment_collected_date' ,'collector_id' ,
                                                    'loan_do_not_adjust_remaining_pro_rata' ,'repayment_adjust_remaining_schedule' ,
                                                    'repayment_manual_composition' , 'principal_repayment_amount' ,'interest_repayment_amount' ,
                                                    'fees_repayment_amount' , 'penalty_repayment_amount' ,'repayment_description' ,

                        ])

                        repayment_df.to_csv('repaymentlist.csv',index=None)
  
def main():

    public_key = 12815

    branch = 15735 

    
    
    
    API_BASE_URL = f'https://api-main.loandisk.com/{public_key}/{branch}/repayment/from/1/count/25'

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
