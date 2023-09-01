## STUDY_AI
![](./images/머신러닝%20학습과정.png)

## 데이터분석을 위한 기초문법
| 제목 | 작성소스 | 설명 | 비고 |
|---|---|---|---|
| concat | [numpys_concat](./codes/numpys.py) | numpy을 이용한 concat  | np.concatenate((, ), axis=)|
| concat | [pandas_concat](./codes/pandass.ipynb) | pandas를 이용한 concat  | pd.concat([ , ], axis=)|
| encoder, concat, Imbalanced Data Sampling | [pandas_encoder](./codes/sklearns.ipynb) | Encoding with One Hot Encoding & concat & Under/Over Sampling | oneHotEncoder.transform(df_[[' ']]).toarray()|

## 데이터분석
| 제목 | 작성소스 | 설명 | 비고 |
|---|---|---|---|
| 지도학습-이진분류 데이터 분석 | [TitanicFromDisaster](./codes/MLs/Classifications/TitanicFromDisaster.ipynb) | 지도학습-이진분류  |LogisticRegression |
| 지도학습-이진분류 DecisionTreeClassifier 분석 | [TitanicFromDisaster_Tree](./codes/MLs/Classifications/TitanicFromDisaster_Tree.ipynb) | DecisionTreeClassifier  | plot_tree |
| 지도학습-이진분류 evaluation | [TitanicFromDisaster_evaluation](./codes/MLs/Classifications/TitanicFromDisaster_evaluation.ipynb) |  evaluation(평가) |mean_squared_error(MSE), classification_report,오차 행렬 (confusion_matrix) |
| 지도학습-다항분류 Pre-Process | [Pre-Process](./codes/MLs/Classifications/NSC_BND_M20_DecisionTreeClassifier_preprocess.ipynb) |  전처리 과정 | apply() 활용|
| 비지도학습 | [iris_KMeans](./codes/MLs/Clusterings/iris_KMeans.ipynb) | 비지도학습의 데이터 분석|KMeans, sum of square |
| 회귀분석 | [Regression](./codes/MLs/Regressions/BreastCancerWisconsin_Regression.ipynb) | 회귀분석 |LinearRegression, 서비스 배포 |
| 회귀분석 평가 | [Regression_evaluations](./codes/MLs/Regressions/BreastCancerWisconsin_Regression_evaluations.ipynb) | 회귀분석의 평가 |r2_score, MSE(mean_squared_error) |
| 회귀분석 평가 | [scaling_encoding](./codes/MLs/Classifications/TitanicFromDisaster_scaling_encoding.ipynb) | Scaling & Encoding |Encoding with One Hot Encoding, Scaling - MinMaxScaler |
| GridSearchCV | [GridSearchCV](./codes/MLs/Classifications/NSC_BND_M20_GridSearchCV.ipynb) | GridSearchCV |평가 score, best_score,classification_report |
## QUEST
| 제목 | 작성소스 | 과제 설명 | 비고 |
|---|---|---|---|
|지도학습|[QUEST](./codes/regression/NSC2_M20_quest.ipynb)| mongoDB를 통해 파일 select, 전처리, 학습, 평가, 예측 과정 진행|---|
|linear regression|[QUES.ipynb](./codes/MLs/Regressions/RecurrenceOfSurgery_quest.ipynb), [QUEST.py](./codes/MLs/Regressions/RecurrenceOfSurgery_quest.py)|연속형 데이터 사용, linear regression 학습, 평가, 서비스(pickle)|---|
|Logistic regression|[QUEST.ipynb](./codes/MLs/Classifications/BreastCancerWisconsinDataSet_quest.ipynb), [QUEST.py](./codes/MLs/Classifications/BreastCancerWisconsinDataSet_quest.py)|연속형 데이터 사용, diagnosis 전처리,Logistic regression 학습, 평가, 서비스(pickle)|---|
|DecisionTreeClassifier|[목표변수의 전체데이터](./codes/MLs/Classifications/NSC_BND_M20_DecisionTreeClassifier_quest.ipynb), [목표변수의 범주 8개만](./codes/MLs/Classifications/NSC_BND_M20_DecisionTreeClassifier_quest_top8.ipynb)|DecisionTreeClassifier 전처리, 학습, 평가|---|
|split/classification_report|[evaluation](./codes/MLs/Classifications/BreastCancerWisconsinDataSet_evaluation_quest.ipynb)|train_test_split() 적용, classification_report() 적용|---|
|split/classification_report|[evaluation](./codes/MLs/Classifications/NSC_BND_M20_evaluation_quest.ipynb)|train_test_split() 적용, classification_report() 적용, 평가 의견 첨부|---|
|GridSearchCV|[best_model](./codes/MLs/Classifications/RecurrenceOfSurgery_FeatureEngin_quest.ipynb)|목표변수(재발여부), 설명변수(3개), 최고 모델 찾기|---|
