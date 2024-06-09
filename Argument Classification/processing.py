import pandas as pd

def label(row):
    if row['answer'] == 'Premise' or row['answer'] == 'premise' or row['answer'] == 'Prem':
        return 0
    if row['answer'] == 'Claim' or row['answer'] == 'claim':
        return 1
    
def evaluate(data):
    cnt = 0
    for i in range(0, len(data)):
        if data.at[i, 'y_true'] == data.at[i, 'true_predict']:   
            cnt += 1
    return f'{cnt} / {len(data)}', cnt/len(data)

data = pd.read_csv('C:/Users/User/Desktop/S/Senior2/NLP/Final Project Task 2/Task 2.1/test_predictions_21.csv')
print(data)
data['true_predict'] = data.apply(label, axis=1)
print(data)
ans, per = evaluate(data)
print(f'Passed cases: {ans}')
print(f'Accuracy: {per}')
data.to_csv('C:/Users/User/Desktop/S/Senior2/NLP/Final Project Task 2/Task 2.1/test_predictions_21_final.csv')