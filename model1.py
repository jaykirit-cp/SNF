import os 
import joblib


class SNF_Detect:
    
    # Directories for Model --> Change if subdirectories created
    CURR_DIR         = os.getcwd()
    
    model_dir        = "./Model/savedmodel.pkl"


    # Change Response Text 
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
