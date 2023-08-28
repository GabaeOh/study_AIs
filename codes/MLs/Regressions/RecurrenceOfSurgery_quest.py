## 예제 [[47.0,16.42]]
texture_mean = float(input('texture_mean : '))
perimeter_mean = float(input('perimeter_mean : '))

import pickle

## 파일 읽는법 
with open ('datasets/datasets/RecurrenceOfSurgery.pkl', 'rb') as regression_file : 
    loaded_model = pickle.load(regression_file)
    input_labels = [[texture_mean, perimeter_mean]]  # 학습했던 설명변수 형식 맞게 적용 
    result_predict = loaded_model.predict(input_labels)
    print('Predict radius_mean Result : {}'.format(result_predict))
    pass