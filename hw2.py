import numpy as np
import pandas as pd

# P1 T0
data_frame = pd.read_html("https://uk.wikipedia.org/wiki/%D0%9D%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8",
                          attrs={"class": "wikitable collapsible collapsed",
                                 "style": "text-align: right"},
                          match="Регіон"
                          )
table = data_frame[0]
table


# P1 T1
table.head()  # default 5


# P1 T2
table.shape


# P1 T3
table_upd_1_replace = table.replace(to_replace="—", value=np.nan)
table_upd_1_replace


# P1 T4
table_upd_1_replace.dtypes


# P1 T5
table_upd_1_replace["2014"] = pd.to_numeric(table_upd_1_replace["2014"])
table_upd_1_replace["2019"] = pd.to_numeric(table_upd_1_replace["2019"])
table_upd_1_replace.dtypes


# P1 T6
table_upd_1_replace.isnull().sum()/table_upd_1_replace.shape[0]
# table_upd_1_replace.sum()


# P1 T7
table_upd_2_del_row_total = table_upd_1_replace.drop([27])
table_upd_2_del_row_total


# P1 T8
values = {"1950": table_upd_2_del_row_total["1950"].mean().round(1),
          "1960": table_upd_2_del_row_total["1960"].mean().round(1),
          "1970": table_upd_2_del_row_total["1970"].mean().round(1),
          "1990": table_upd_2_del_row_total["1990"].mean().round(1),
          "2000": table_upd_2_del_row_total["2000"].mean().round(1),
          "2012": table_upd_2_del_row_total["2012"].mean().round(1),
          "2014": table_upd_2_del_row_total["2014"].mean().round(1),
          "2019": table_upd_2_del_row_total["2019"].mean().round(1),
          }
table_upd_3_fillna_nan_to_average = table_upd_2_del_row_total.fillna(
    value=values)
table_upd_3_fillna_nan_to_average


# P1 T9
avr_val2019 = table_upd_3_fillna_nan_to_average["2019"].mean().round(1)
# avr_val2019 # = 80.2
table_upd_3_fillna_nan_to_average[table_upd_3_fillna_nan_to_average["2019"] > avr_val2019][[
    "Регіон", "2019"]]


# P1 T10
table_upd_4_sort_by_max_value = table_upd_3_fillna_nan_to_average.sort_values(
    ["2014"], ascending=False)[["Регіон", "2014"]].head(1)
table_upd_4_sort_by_max_value


# P1 T11
graph = table_upd_3_fillna_nan_to_average.plot.bar(x="Регіон",
                                                   y="2019",
                                                   title="Діаграма коефіцієнтів народжуваності в регіонах України у 2019 році",
                                                   ylabel="Коефіцієнт",
                                                   figsize=(16, 10),
                                                   grid=True
                                                   )
graph
