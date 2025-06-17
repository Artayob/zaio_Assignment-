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

        
class DataCleaner:
    def __init__(self,data):
        self.data = data

    def Missing_values(self):
        missing_values = self.data.isnull().sum()
        if missing_values.any():
            print("Missing values found at Columns:")
        else: 
            print("No missing values found file is good")
        return missing_values
    
    def check_duplicates(self):
        duplicates = self.data.duplicated().sum()
        if duplicates >0: 
            print(f"Found {duplicates} duplicate rows.")
        else: 
            print("No duplicates found")    
        return duplicates     
    
    def validate_ranges(self):
        

loader = DataLoader("C:/Users/sakit/Desktop/zaio_Assignment-/student_habits_performance.csv")
content = loader.load_content()
print(content)        

cleaner = DataCleaner(content)
cleaner.Missing_values()
cleaner.check_duplicates()