import numpy as np

from flask import Flask, request, jsonify, render_template
import pickle
from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
pkl_file = open('model.pkl','rb')
model = pickle.load(open('model.pkl', 'rb'))
index_dict = pickle.load(pkl_file)

#procfile.txt 
#web: gunicorn app:app
#first file that we have to run first : flask server name
@app.route('/')
def home():
	        
  return render_template('index.html')
        
@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method=='POST':
        result=request.form
		
		#Prepare the feature vector for prediction
        pkl_file = open('cat', 'rb')
        index_dict = pickle.load(pkl_file)
        #new_vector = np.zeros(91)
        new_vector = np.zeros(93)
   

 

        try:
             new_vector[index_dict[str(result['Negeri'])]] = 1
        except:
          pass
        try:    
            new_vector[index_dict[str(result['House'])]] = 1
        except:
          pass
        try:
            new_vector[index_dict[str(result['flooring_material'])]] = 1
        except:
          pass
        try:
            new_vector[index_dict[str(result['Siling_material'])]] = 1
        except:
          pass
        try:
            new_vector[index_dict[str(result['Design_Cabinet'])]] = 1
        except:
          pass
        try:
            new_vector[index_dict[str(result['Jenis_Cabinet'])]] = 1
        except:
          pass
        try:
            new_vector[index_dict[str(result['Buitin_cabinet'])]] = 1
        except:
          pass
        try:
           new_vector[index_dict[str(result['materia_pintukabinet'])]] = 1
        except:
          pass
        try:
          new_vector[index_dict[str(result['material_handle'])]] = 1
        except:
          pass
        try:
          new_vector[index_dict[str(result['Materialcountertop'])]] = 1
        except:
          pass
        try:
          new_vector[index_dict[str(result['Material_backsplash'])]] = 1
        except:
          pass
        try:
          new_vector[index_dict[str(result['sinki'])]] = 1
        except:
          pass 
        try:
          new_vector[index_dict[str(result['Wiring_surface'])]] = 1
        except:
          pass
        try:
          new_vector[index_dict[str(result['wiring_conceal'])]] = 1
        except:
          pass
        try:
          new_vector[index_dict[str(result['Salary'])]] = 1
        except:
          pass
          """
        try:
             new_vector[index_dict[str(result['Years'])]] = 1
        except:
          pass
        try:    
            new_vector[index_dict[str(result['Housesize'])]] = 1
        except:
          pass
        try:
            new_vector[index_dict[str(result['flooring'])]] = 1
        except:
          pass
        try:
            new_vector[index_dict[str(result['siling'])]] = 1
        except:
          pass
        try:
            new_vector[index_dict[str(result['saizbaseunit(ft)'])]] = 1
        except:
          pass
        try:
            new_vector[index_dict[str(result['saizwallunit(ft)'])]] = 1
        except:
          pass
        try:
            new_vector[index_dict[str(result['Saiztinggibaseunit(ft)'])]] = 1
        except:
          pass
        try:
           new_vector[index_dict[str(result['Saiztinggiwallunit (ft)'])]] = 1
        except:
          pass
        try:
          new_vector[index_dict[str(result['Kerja_mengecat'])]] = 1
        except:
          pass
        try:
          new_vector[index_dict[str(result['Elektrik'])]] = 1
        except:
          pass
           """
        new_vector[0] = result['Years']
        new_vector[1] = result['Housesize']
        new_vector[2] = result['flooring']
        new_vector[3] = result['siling']
        new_vector[4] = result['saizbaseunit(ft)']
        new_vector[5] = result['saizwallunit(ft)']
       
        new_vector[6] = result['Kerja_mengecat']
        new_vector[7] = result['Elektrik']
        new_vector[8] = result['kitchensize']
      

    new = [new_vector]

    prediction = model.predict(new)
    #print(prediction)
    prediction = str(np.round(prediction, 2))
    return render_template('index.html', Predict_score ='Anggaran  ubahsuai dapur bermula dari  RM {} '.format(prediction))
if __name__ == '__main__':app.run()