import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')
df['math_pass_status'] = df['math score'].apply(lambda x: 'pass' if x > 33 else 'fail')
print(df.head())
df.to_csv('StudentsPerformance_with_new_column.csv', index=False)