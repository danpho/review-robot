import os
import sys
import pandas as pd
import json
import gzip

# set pandas for complete view of data
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", -1)

work_dir = os.getcwd().rstrip()
data_dir = work_dir + "\\data\\"
file = data_dir + "meta_Appliances.json.gz"
os.chdir(data_dir)


# read data from json file
data = []
with gzip.open(file) as f:
    for l in f:
        data.append(json.loads(l.strip()))

print(data[0])


# convert list into pandas dataframe
df = pd.DataFrame.from_dict(data)

# category, # tech1, # description, # fit, # title, # also_buy
# tech2, # brand, # feature, # rank, # also_view, # details,
# main_cat, # similar_item, # date, # price, # asin, # imageURL, # imageURLHighRes
i = 0
for col in df.columns:
    i += 1
    print(i, col)


# check brand amount
brand = df["brand"].unique()
amt_brand = len(brand)  # 2762

# check imageURLHighRes
amt_image = len(df["imageURLHighRes"])  # 30445

# data preview and clean
# after checking values for each column,
# drop column "fit", "tech2" which only show SN
# drop column "imageURL" which only show vague image
# df = df.drop(["fit", "tech2", "imageURL"], 1)
df = df.drop(["fit", "tech2"], 1)

# "rank" need to be split
# it consists of up to 41 list elements if use dfrk = pd.DataFrame(df["rank"].tolist()) would result in below errors
# reason unknown
"""
      0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39    40
10158  4  ,  9  0  2  ,  3  2  8     i  n     C  l  o  t  h  i  n  g  ,     S  h  o  e  s     &     J  e  w  e  l  r  y     (  None
14271  4  ,  6  0  8  ,  0  3  7     i  n     C  l  o  t  h  i  n  g  ,     S  h  o  e  s     &     J  e  w  e  l  r  y     (  None
14996  2  ,  8  2  9  ,  7  4  3     i  n     C  l  o  t  h  i  n  g  ,     S  h  o  e  s     &     J  e  w  e  l  r  y     (  None
15421  3  ,  5  2  5  ,  4  5  7     i  n     C  l  o  t  h  i  n  g  ,     S  h  o  e  s     &     J  e  w  e  l  r  y     (  None
26038  1  ,  1  8  6  ,  5  2  7     i  n     C  l  o  t  h  i  n  g  ,     S  h  o  e  s     &     J  e  w  e  l  r  y     (  None
26230  6  ,  9  3  4  ,  5  7  4     i  n     C  l  o  t  h  i  n  g  ,     S  h  o  e  s     &     J  e  w  e  l  r  y     (  None
"""

