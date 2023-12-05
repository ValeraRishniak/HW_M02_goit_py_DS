%matplotlib inline

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# P2 T1
table = pd.read_csv("2017_jun_final.csv")
# table


# P2 T2
table.head() #default 5 rows


# P2 T3
table.shape


# P2 T4
table.dtypes


# P2 T5
table.isnull().sum()/table.shape[0]


# P2 T6
table_upd_1_del_column = table.drop(labels=["Специализация", "Университет", "Предметная.область", "Валюта", "cls"], axis=1)


# P2 T7
table_upd_1_del_column.isnull().sum()/table_upd_1_del_column.shape[0]


# P2 T8
table_upd_2_del_rows = table_upd_1_del_column.dropna()


# P2 T9
table_upd_2_del_rows.shape


# P2 T10
python_data = table_upd_2_del_rows[table_upd_2_del_rows['Язык.программирования'] == 'Python']


# P2 T11
python_data.shape


# P2 T12
python_data_upd_1_groupby = python_data.groupby(by='Должность')
python_data_upd_1_groupby


# P2 T13
python_data_upd_2_agg = python_data_upd_1_groupby.agg({'Зарплата.в.месяц': ['min', 'max']})
python_data_upd_2_agg


# P2 T14
def fill_avg_salary(data):
  return data.mean()

new_column_avg = python_data_upd_2_agg.apply(fill_avg_salary, axis=1, result_type='expand')
new_column_avg.name = "avg_salary"
python_data_upd_3_new_column_avg = pd.concat([python_data_upd_2_agg, new_column_avg], axis=1)
python_data_upd_3_new_column_avg


# P2 T15
python_data_upd_3_new_column_avg['avg_salary'].describe()


# P2 T16
python_data_upd_3_new_column_avg.to_csv("2017_jun_final_clean_and_updated.csv")
