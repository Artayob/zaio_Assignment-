import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"File not found at: {self.filepath}")

    def load_content(self): # this function loads and raises the exceptions of the file 
        try:
            df = pd.read_csv(self.filepath, delimiter=';')
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
        if 'study_hours_per_day' in self.data.columns:
            invalid = self.data[(self.data['study_hours_per_day'] < 0) | (self.data['study_hours_per_day'] > 24)]
            if not invalid.empty:
                print("Invalid study_hours values found:")
                print(invalid[['study_hours_per_day']])
            else:
                print("All study_hours values are within the valid range.")
        else:
            print("Column 'study_hours_per_day' not found, skipping range validation.")


class StudentAnalyzer:

    def __init__(self,data):
        self.data = data 

    def mean_median(self):
        if 'mental_health_rating' in self.data.columns and 'study_hours_per_day' in self.data.columns:
            group = self.data.groupby('mental_health_rating')['study_hours_per_day']
            result = group.agg(['mean', 'median'])
            print(result)
            return result
        else:
            print("Required columns not found.")
            return None
        
    def correlation(self):
        correlation = self.data['sleep_hours'].corr(self.data['exam_score'])
        print("Correlation between sleep hours and exams scores are: ", correlation)
        return correlation
    
    def outliers(self):
        Q1 = self.data['social_media_hours'].quantile(0.25)
        Q3 = self.data['social_media_hours'].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = self.data[(self.data['social_media_hours'] < lower_bound) | (self.data['social_media_hours'] > upper_bound)]
        print("The out lier values are:", outliers)
        return outliers


class Visualizer:
    def __init__(self, data):
        self.data = data

    def Histogram(self):
        plt.hist(self.data["study_hours_per_day"], bins= 10, color= 'Orange', edgecolor="black")
        plt.xlabel("Study Hours")
        plt.ylabel("How many days") 
        plt.title("Histogram showing students study hours per day")
        plt.grid(False)
        plt.show()

    def ScatterPlot(self):
        plt.scatter(self.data["sleep_hours"], self.data["exam_score"], edgecolors="darkblue")
        plt.xlabel("Sleep time")
        plt.ylabel("Exam Scores")
        plt.title("Scatter plot showing students sleep times compared to exam scores")
        plt.grid(True)
        plt.show()

    def BoxPlot(self):
        plt.figure(figsize=(8,5))
        sns.boxplot(x ="diet_quality", y = "exam_score", data = self.data, palette="pastel")
        plt.title("Box plot showing diet and final scores")
        plt.xlabel("Diet Quality")
        plt.ylabel("Final Score")
        plt.grid(True)
        plt.show() 

class ScorePredictor:
    def __init__(self, data):
        self.data = data
    
    def Model(self):
        try:            
            for col in ['diet_quality', 'mental_health_rating']:
                if self.data[col].dtype == 'object':
                    encoder = LabelEncoder()
                    self.data[col] = encoder.fit_transform(self.data[col])
            
            
            self.model = LinearRegression()
            X = self.data[['study_hours_per_day', 'diet_quality', 'sleep_hours', 'mental_health_rating']]
            y = self.data['exam_score']

            self.model.fit(X, y)

            y_pred = self.model.predict(X)[0]
            print(f"The predicted scores are: {y_pred: 2f}")

        except Exception as e:
            print(f"Error: {e}")

    def save_model(self):
        if self.model is None:
            print("No model to save. Train the model first.")
            return
        filename = 'linear_regression_model.pkl'
        with open(filename, 'wb') as file:
            pickle.dump(self.model, file)
        print(f"Model saved to {filename}")



loader = DataLoader("C:/Users/sakit/Desktop/zaio_Assignment-/student_habits_performance.csv")
content = loader.load_content()
print(content) 

analyzer = StudentAnalyzer(content)
cleaner = DataCleaner(content)
visualization = Visualizer(content)
machine = ScorePredictor(content)   
cleaner.Missing_values()
cleaner.check_duplicates()
cleaner.validate_ranges()
analyzer.mean_median()
analyzer.correlation()
analyzer.outliers()
visualization.Histogram()
visualization.ScatterPlot()
visualization.BoxPlot()
machine.Model()
machine.save_model()