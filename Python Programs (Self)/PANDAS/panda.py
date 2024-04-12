import pandas as pd

dict_marks = {"Mathematics": [90, 67, 93, 84, 55], "Science": [78, 64, 89, 98, 43], "Informatics Practices": [80, 75, 100, 79, 56]}

df_result = pd.DataFrame(dict_marks, index = ["Arjun", "Saurabh", "Aryan", "Rohit", "Manya"])

print(df_result)
