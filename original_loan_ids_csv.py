import requests

import json

import pandas as pd


"""   To display the orginal loan scedule values         """

def display_values(res,item):
        
        data = res.json()
        
      
        loan_detail =[]
        
        response = data["response"]
        result=response['Results']
        
        counter = 0

        
      
        for i in response['Results']:
              
                while(counter < len(i)):
                       
                        if item == i[counter]['LoanId']or str(item) == i[counter]['LoanId'] or i[counter]['LoanId'] == None:
                           
                            loan_detail.append([
                                i[counter]['LoanId'],
                                i[counter]['Date'],
                                i[counter]['Description'],
                                i[counter]['Principal'],
                                i[counter]['Interest'],
                                i[counter]['Fees'],
                                i[counter]['Penalty'],
                                i[counter]['Due'],
                                i[counter]['Total Due'],
                                i[counter]['Principal Balance'],


                            ])
                            
                        
                            counter +=  1
                            

                            loan_df = pd.DataFrame(data=loan_detail, columns=['LoanId', 'Date','Description',
                                        'Principal','Interest','Fees','Penalty','Due','Total Due','Principal Balance'])
           
                            loan_df.to_csv('orginal_loan_'+str(item)+'.csv',index=None)

def main():

    public_key = 12815

    branch = 15735
 

    loan_id_list =  [1786909,1621672,1569248,1566174,1897705]

    

    header = {
        'content-type': 'application/json',
        'Authorization': 'Fn5eHUrSX6vD6ckykekD52NyamrfpR4gHBYgDk8f',
    }

    
    try:

        for item in loan_id_list:

            API_BASE_URL = f'https://api-main.loandisk.com/{public_key}/{branch}/loan/original_loan_schedule/{item}/from/0/count/50'
                
            res = requests.get(API_BASE_URL,headers = header)
                
            display_values(res,item)
       

    except requests.exceptions.HTTPError as e:
        print('Unable to retrieve values.')
        print(e.response.text)
 

if __name__ == '__main__':
    main()
