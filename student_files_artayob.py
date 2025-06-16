import pandas as pd
import os

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"File not found at: {self.filepath}")

    def load_content(self): # this function loads and raises the exceptions of the file 
        try:
            df = pd.read_csv(self.filepath)
            return df
        except Exception as e:
            raise FileNotFoundError(f"Error reading file: {e}")

        
loader = DataLoader("C:/Users/sakit/Desktop/ZAIO_Assigment/student_habits_performance.csv")
content = loader.load_content()
print(content)

class DataCleaner:
    def Missing_values(self):
        missing_values = self.load_content.check_missing_values()
        if missing_values.any():
            print("Missing values found at Columns:")
        else: 
            print("No missing values found file is good")
        return missing_values