import pandas as pd

data = pd.read_csv('adult.data.csv')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

data.head()

data['sex'].value_counts()

data[data['sex'] == 'Female']['age'].mean()

data['native-country'].unique()

data['native-country'].value_counts() / len(data) * 100

data.groupby('native-country').size() / len(data) * 100

sum(data.groupby('native-country').size() / len(data) * 100)

data[data['salary'] == '>50K']['age'].mean()

data[data['salary'] == '>50K']['age'].min()

data[data['salary'] == '>50K']['age'].max()

data[data['salary'] == '<=50K']['age'].mean()

data[(data['education'] == 'Bachelors') | (data['education'] == 'Prof-school') | \
     (data['education'] == 'Assoc-acdm') | (data['education'] == 'Assoc-voc') | \
     (data['education'] == 'Masters') | (data['education'] == 'Doctorate') & \
     (data['salary'] == '>50k')].value_counts()

data[(data['education'] == 'Bachelors') | (data['education'] == 'Prof-school') | \
     (data['education'] == 'Assoc-acdm') | (data['education'] == 'Assoc-voc') | \
     (data['education'] == 'Masters') | (data['education'] == 'Doctorate')].value_counts()

data[data['race'] == 'Amer-Indian-Eskimo']['age'].max()

data[(data['marital-status'] == 'Married-civ-spouse') | (data['marital-status'] == 'Married-spouse-absent') | \
     (data['marital-status'] == 'Married-AF-spouse') & (data['salary'] == '>50k')].value_counts()
data['marital-status'].value_counts()

data[(data['marital-status'] == 'Never-married') | (data['marital-status'] == 'Divorced') | \
     (data['marital-status'] == 'Separated') | (data['marital-status'] == 'Widowed') &  \
      (data['salary'] == '>50k')].value_counts()

data[data['hours-per-week'] == 99].value_counts()

data.groupby('hours-per-week').size() / len(data['hours-per-week']) * 100

data[(data['salary'] == '>50K') & (data['native-country'] ==  'Japan')]['hours-per-week'].mean()

data[(data['salary'] == '<=50K') & (data['native-country'] ==  'Japan')]['hours-per-week'].mean()