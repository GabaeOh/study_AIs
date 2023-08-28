## 예제 [0.2241	9.833	185.2]
# 설명변수 : 'radius_se', 'area_se', 'area_worst'

radius_se = float(input('radius_se : '))
area_se = float(input('area_se : '))
area_worst = float(input('area_worst : '))

import pickle
import os 

file_path = 'datasets/BreastCancerWisconsinDataSet.pkl'

## 파일 읽는법 
if os.path.exists(file_path): # 파일 존재 여부 return True/False 
    with open ('datasets/BreastCancerWisconsinDataSet.pkl', 'rb') as regression_file : 
        loaded_model = pickle.load(regression_file)
        input_labels = [[radius_se, area_se, area_worst]] 
        result_predict = loaded_model.predict(input_labels)
        print('Predict diagnosis Result : {}'.format(result_predict))
        pass

else : 
    print('File Not exists!')
## Predict diagnosis Result : [0]