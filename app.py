import streamlit as st  #use to create web interface
import tensorflow as tf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


# set the web page
st.set_page_config(page_title = 'Blood cell classifier', page_icon= '🔬')
st.title('Blood Cell Classifier 💉')

#Model loading
@st.cache_resource   #load model once and reuse it 
del load_model():
	return tf.keras.models.load_model('best_blood_cell_model_1.keras')


model = load_model()

# classes names of blood cell
classes = ['basophil', 'eosinophil', 'erythroblast', 'immature granulocytes',
           'lymphocyte', 'monocyte', 'neutrophil', 'platelet']


# side bar information
st.sidebar.info('''
**Blood Cell Classifier**
- Accuracy : 87.43
- Dataset : BloodMNIST
- Framework : Tensorflow
''')

#file uploader
uploaded_file = st.file_uploader('📤 Upload blood cell image' type = ['jpg','jpeg','png'])  #creates the button '📤 Upload blood cell image' to upload image

# checking file uploaded
if uploaded_file is not None:
	#creates two columns
	col_1, col_2 = st.columns(2)  #Splits screen into 2 equal columns

	with col_1:
		st.subheader('"📷 Uploaded File')
		image = image.open(uploaded_file)
		st.image(image,use_column_width = True) #"Show the image, make it fill the space"
		
		#resize image
		image_resized = image.resize((28,28))
		
		#normalised image
		image_array = np.array(image_resize)/255.0  #output: (28,28,3)
		
		# Add the fake batch dimension using the simple shortcut
		image_batch = image_array[None,...]
		print(f"New batch shape for the model: {image_batch.shape}")
		Output: (1, 28, 28, 3)

		#prediction
		prediction = model.predict('image_batch')
		#give the highest value prediction for each image classes
		predicted_class = np.argmax(prediction[0])
		
		confidence = prediction[0][predected_classes]*100


	with col_2:
		st.subheader("🩺 Model's Prediction")
		st.metric('Predicted Cell Type', classes[prediction_class].upper())
		st.metric('Confidence', f'{confidence:.2f}%'}
		
		if confidence>90:
			st.success('✅ High Confidence!') #Show green success box with message
		elif confidence>80:
			st.info('Good Confidence')  #Show blue info box
		else:
			st.warning('⚠️ Low Confidence') #Show yellow warning box


	
else:
	#no file uploaded
	st.info('📤Please upload an image to check the result')








