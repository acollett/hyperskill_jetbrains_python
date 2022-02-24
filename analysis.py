import pandas as pd

pd.set_option('display.max_columns', 8)

general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')

prenatal.columns = general.columns
sports.columns = general.columns

prenatal['gender'] = prenatal['gender'].fillna('f')

table = pd.concat([general, prenatal, sports], ignore_index=True)

table.drop(columns='Unnamed: 0', inplace=True)
table['gender'] = table['gender'].replace(['female', 'male', 'man', 'woman'], ['f', 'm', 'm', 'f'])
table.dropna(subset=['hospital'], inplace=True)
table.fillna(0, inplace=True)
#print(table.shape)
#print(table.sample(n=20, random_state=30))

# question 1
no_of_patients = table['hospital'].value_counts()
if no_of_patients[0] > no_of_patients[1] > no_of_patients[2]:
    answer1 = "general"
elif no_of_patients[1] > no_of_patients[2]:
    answer1 = "prenatal"
else:
    answer1 = "sports"
print(f"The answer to the 1st question is {answer1}")

# question 2
stomach_patients = table[(table['hospital']=='general') & (table['diagnosis']=='stomach')]
answer2 = (max(stomach_patients['diagnosis'].value_counts()) / no_of_patients[0])
print(f"The answer to the 2nd question is {round(answer2, 3)}")

# question 3
dislocated_patients = table[(table['hospital']=='sports') & (table['diagnosis']=='dislocation')]
answer3 = (max(dislocated_patients['diagnosis'].value_counts()) / no_of_patients[2])
print(f"The answer to the 3rd question is {round(answer3, 3)}")

# question 4
median_ages_general = table['age'][(table['hospital']=='general')].median()
median_ages_sports = table['age'][(table['hospital']=='sports')].median()
answer4 = median_ages_general - median_ages_sports
print(f"The answer to the 4th question is {int(answer4)}")

# question 5
no_of_blood_tests_gen = table['hospital'][(table['hospital']=='general') & (table['blood_test']=='t')].value_counts()
no_of_blood_tests_pre = table['hospital'][(table['hospital']=='prenatal') & (table['blood_test']=='t')].value_counts()
no_of_blood_tests_spo = table['hospital'][(table['hospital']=='sports') & (table['blood_test']=='t')].value_counts()
if max(no_of_blood_tests_gen) > max(no_of_blood_tests_pre) > max(no_of_blood_tests_spo):
    answer5 = "general"
elif max(no_of_blood_tests_pre) > max(no_of_blood_tests_gen):
    answer5 = "prenatal"
else:
    answer5 = "sports"
print(f"The answer to the 5th question is {answer5}, {max(no_of_blood_tests_pre)} blood tests")
