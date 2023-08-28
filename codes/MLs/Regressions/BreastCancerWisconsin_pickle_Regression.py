# 예제 [[16.34, 87.21]]

수술시간 = float(input('수술시간 : '))
헤모글로빈수치 = float(input('헤모글로빈수치 : '))

import pickle
import os 

file_path = 'datasets/BreastCancerWisconsin_Regression.pkl'

## 파일 읽는법 
if os.path.exists(file_path): # 파일 존재 여부 return True/False 
    with open ('datasets/BreastCancerWisconsin_Regression.pkl', 'rb') as regression_file : 
        loaded_model = pickle.load(regression_file)
        input_labels = [[수술시간, 헤모글로빈수치]]  # 학습했던 설명변수 형식 맞게 적용 
        result_predict = loaded_model.predict(input_labels)
        print('Predict Age Result : {}'.format(result_predict))
        pass
    
else : 
    print('File Not exists!')
## Predict Age Result : [13.45096511]