import os
import uuid
from PIL import Image
import tensorflow as tf
import numpy as np

# Load the trained model
model = tf.keras.models.load_model(r'C:\Users\Lenovo\Downloads\fold_1_Xception_model.h5')


# Define a list of class labels for mapping predictions to disease names
class_labels = [ 'Potato___Early_Blight', 'Potato___Healthy', 'Potato___Late_Blight']

def preprocess_image(image):
    # Convert the TemporaryUploadedFile object to a PIL.Image object
    image_pil = Image.open(image)

    # Convert the image to RGB color mode
    image_rgb = image_pil.convert('RGB')

    # Resize the color image to match the input size of the model (71x71)
    image_resized = image_rgb.resize((71, 71))

    # Convert the resized image to a NumPy array
    img_array = np.array(image_resized)

    # Normalize the pixel values
    img_array = img_array / 255.0

    # Expand the dimensions to match the model's input shape
    img_array = np.expand_dims(img_array, axis=0)

    return img_array

def predict_disease(image):
    # Preprocess the image
    preprocessed_image = preprocess_image(image)

    # Generate a unique filename for the temporary image
    unique_filename = str(uuid.uuid4()) + '.png'
    temp_image_path = os.path.join('media', unique_filename)

    # Save the temporary image
    Image.fromarray((preprocessed_image[0] * 255).astype('uint8')).save(temp_image_path)

    # Perform prediction
    predictions = model.predict(preprocessed_image)
    predicted_class_index = np.argmax(predictions)
    predicted_class_label = class_labels[predicted_class_index]

    return predicted_class_label, temp_image_path
