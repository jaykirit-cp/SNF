import os 
import joblib


class SNF_Detect:
    
    # Directories for Model --> Change if subdirectories created
    CURR_DIR         = os.getcwd()
    
    model_dir        = "./Model/savedmodel.pkl"


    # Change Response Text
    
    response_text = {
        'Severity_Mild':"Your are affected by Covid mildly.",
        'Severity_Moderate': "You are affected by Covid Moderately",
        'Severity_Severe':"You are affected by Covid Severely",
        'Severity_None':"You are safe from Covid",
        'Other_Severity':"You have been affected from other Disease apart from Covid "
    }
    
    def __init__(self):
        
        self.clf = joblib.load(self.model_dir)
    
    def predict(self,X):

        try:
            label = self.clf.predict([X])[0]
            
        except:
            return {"response":"","status":'OK'}
        
        else:
            return {"response":self.response_text[label],"status":'OK'}
        
    def save_model(self):
        print("Saving the model")
        return
