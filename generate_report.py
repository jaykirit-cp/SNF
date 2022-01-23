from fpdf import FPDF

import pandas as pd
import os 
import joblib
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier


class SNF_Detect:
    
    # Directories for Model --> Change if subdirectories created
    CURR_DIR         = os.getcwd()
    
    model_dir        = "./Model/savedmodel.pkl"


    def __init__(self):
        
        self.clf = joblib.load(self.model_dir)
    
    def predict(self):
        df=pd.read_csv('./Model/content/diabetes.csv')
        X=df.drop('Outcome',axis=1)
        y=df['Outcome']
        X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=0)
        sc_x=StandardScaler()
        X_train=sc_x.fit_transform(X_train)
        X_test=sc_x.transform(X_test)
        knn=KNeighborsClassifier(n_neighbors=5,metric='euclidean',p=2)
        knn.fit(X_train,y_train)
        target_names = ['Diabetes', 'Normal']
        y_pred = knn.predict(X_test)
        return(classification_report(y_test, y_pred, target_names=target_names,output_dict=True))
        
    def save_model(self):
        print("Saving the model")
        return


class Report:

    # Creating pdf object
    pdf = None

  
     

    # inx declaration
    inx = 60

    def __init__(self):
        # format ('A3','A4','Letter','Legal')
        self.pdf = FPDF('P','mm','A4')

        # Adding a page to the pdf file
        self.pdf.add_page()

        # Setting up font
        self.pdf.set_font('helvetica','',16)

        

    def header(self):

        # Arial bold 15
        self.pdf.set_font('Arial', 'B', 15)

        # Move to the right
        self.pdf.cell(46)

        # Title
        self.pdf.cell(90, 20, 'MEDICAL REPORT', 1, 0, 'C')

        # Logo
        self.pdf.image('./static/images/dl.jpg', 170, 4, 33)

        self.pdf.line(0, 40,220,40)

        # Line break
        self.pdf.ln(20)

    def insert_text(self,user_details):
        # Add Text
        # w = width
        # h = height

        # Adding Title
        # for key,value

        inx  = self.inx
        for key,value in user_details.items():
            self.pdf.cell(0,inx,key + " : " + value)
            self.pdf.ln(2)
            inx+=5

        self.pdf.ln(1)
        inx+=5
        self.inx = inx


    def generate_report(self,user_details):

        # print(os.getcwd())
        self.header()
        model = SNF_Detect()
        classification_report = model.predict()
        print(classification_report)

        # Setting up Personal Details header
        self.pdf.cell(90,self.inx,"PERSONAL DETAILS")
        self.pdf.ln(10)
        self.insert_text(
            {
                "Name":user_details["Name"],
                "Gender":user_details["Gender"],
                "Age":user_details["Age"],
                "Pregnancies":user_details["Pregnancies"],
                "Glucose":user_details["Glucose"],
                "Blood Pressure":user_details["Bloodpressure"],
                "Skin Thickness":user_details["Skinthickness"],
                "Insulin":user_details["Insulin"],
                "BMI":user_details["BMI"],
                "Diabetes Pedigree Function":user_details["Diabetes Pedigree Function"],
                "Email ID":user_details["Email Address"]


            }
            )


        self.pdf.cell(0,self.inx,"ANALYSIS")
        self.pdf.line(0,120,220,120)#Horizontal Line
        self.pdf.ln(10)#Horizontal space
        

        #{'Diabetes': {'precision': 0.8454545454545455, 'recall': 0.8691588785046729, 'f1-score': 0.8571428571428571, 'support': 107}, 'Normal': {'precision': 0.6818181818181818, 'recall': 0.6382978723404256, 'f1-score': 0.6593406593406593, 'support': 47}, 'accuracy': 0.7987012987012987, 'macro avg': {'precision': 0.7636363636363637, 'recall': 0.7537283754225492, 'f1-score': 0.7582417582417582, 'support': 154}, 'weighted avg': {'precision': 0.7955135773317591, 'recall': 0.7987012987012987, 'f1-score': 0.796774653917511, 'support': 154}}
        self.pdf.cell(0,self.inx,"DIABETES")
        self.pdf.ln(4)#2
        self.inx += 5
        self.insert_text(
            {
                "precision":" 0.8454545454545455",
                "recall":" 0.8691588785046729",
                "f1-score":"0.8571428571428571",
                "support": "107"

            }
            )


        #self.pdf.line(0,200,220,200) SELF NORMAL COMES IN NEXT LINE
        self.pdf.cell(0,self.inx,"NORMAL")
        self.pdf.ln(3)
        self.inx += 5
        self.insert_text(
            {
                "precision":"0.6818181818181818",
                "recall":"  0.6382978723404256",
                "f1-score":"0.6593406593406593",
                "support": "47"

            }
            )

        self.pdf.ln(16)

        self.pdf.output('./report.pdf')

    def refresh(self):
        # format ('A3','A4','Letter','Legal')
        self.pdf = FPDF('P','mm','A4')

        # Adding a page to the pdf file
        self.pdf.add_page()

        # Setting up font
        self.pdf.set_font('helvetica','',16)



# if __name__ == '__main__':
#     report = Report()
#     report.generate_report()
