from student_files_artayob import DataLoader
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
        if 'study_hours_per_day' in self.data.columns:
            invalid = self.data[(self.data['study_hours_per_day'] < 0) | (self.data['study_hours_per_day'] > 24)]
            if not invalid.empty:
                print("Invalid study_hours values found:")
                print(invalid[['study_hours_per_day']])
            else:
                print("All study_hours values are within the valid range.")
        else:
            print("Column 'study_hours_per_day' not found, skipping range validation.")


loader = DataLoader("C:/Users/sakit/Desktop/zaio_Assignment-/student_habits_performance.csv")
content = loader.load_content()
cleaner = DataCleaner(content)
cleaner.Missing_values()
cleaner.check_duplicates()
cleaner.validate_ranges()