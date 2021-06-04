import requests
import pandas as pd

import json



"""   To display the single repayment   """

def display_values(res,repayment_id):
        
        data = res.json()

        response = data["response"]
        
        repayment_list =[]

       
        for i in response['Results']:
          
                        repayment_list.append([
                                i['repayment_id'],
                                i['loan_id'],
                                i['repayment_amount'],
                                i['loan_repayment_method_id'],
                                i['repayment_collected_date'],
                                i['collector_id'],
                                i['loan_do_not_adjust_remaining_pro_rata'],
                                i['repayment_adjust_remaining_schedule'],
                                i['repayment_manual_composition'],
                                i['principal_repayment_amount'],
                                i['interest_repayment_amount'],
                                i['fees_repayment_amount'],
                                i['penalty_repayment_amount'],
                                i['repayment_description'],
                            ])
                            
                      
                        repayment_df = pd.DataFrame(data=repayment_list, columns=['repayment_id' ,'loan_id' ,'repayment_amount' ,
                                                    'loan_repayment_method_id' ,'repayment_collected_date' ,'collector_id' ,
                                                    'loan_do_not_adjust_remaining_pro_rata' ,'repayment_adjust_remaining_schedule' ,
                                                    'repayment_manual_composition' , 'principal_repayment_amount' ,'interest_repayment_amount' ,
                                                    'fees_repayment_amount' , 'penalty_repayment_amount' ,'repayment_description' ,

                        ])

                        repayment_df.to_csv('data/single_repayment_'+str(repayment_id)+'.csv',index=None)
  
       

  
def main():

    public_key = 12815

    branch = 15735

    repayment_id = 6288587

    
    API_BASE_URL = f'https://api-main.loandisk.com/{public_key}/{branch}/repayment/{repayment_id}'

    header = {
        'content-type': 'application/json',
        'Authorization': 'Fn5eHUrSX6vD6ckykekD52NyamrfpR4gHBYgDk8f',
    }

    
    try:
        
        res = requests.get(API_BASE_URL,headers = header)
           
        display_values(res,repayment_id)
       

    except requests.exceptions.HTTPError as e:
        print('Unable to retrieve values.')
        print(e.response.text)
 

if __name__ == '__main__':
    main()
