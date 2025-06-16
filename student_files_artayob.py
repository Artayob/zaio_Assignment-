import pandas as pd
import os

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        if not os.path.isfile(self.filepath):
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