# mnist_streamlit_app.py
# Streamlit App: MNIST Handwritten Digit Classifier (Train + Predict)

import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps
import os

# ===============================
# Load or Train Model
# ===============================
@st.cache_resource
def load_or_train_model():
    model_path = "mnist_cnn_model.h5"

    if os.path.exists(model_path):
        st.info("✅ Loading existing trained model...")
        model = tf.keras.models.load_model(model_path)
    else:
        st.warning("⚙️ No saved model found. Training a new model, please wait...")

        # Load MNIST dataset
        (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
        x_train = x_train.reshape(-1, 28, 28, 1) / 255.0
        x_test = x_test.reshape(-1, 28, 28, 1) / 255.0
        y_train = tf.keras.utils.to_categorical(y_train, 10)
        y_test = tf.keras.utils.to_categorical(y_test, 10)

        # Define CNN model
        model = tf.keras.Sequential([
            tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
            tf.keras.layers.MaxPooling2D((2,2)),
            tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
            tf.keras.layers.MaxPooling2D((2,2)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(10, activation='softmax')
        ])

        # Compile and train
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        model.fit(x_train, y_train, epochs=3, validation_data=(x_test, y_test))
        model.save(model_path)
        st.success("🎉 Model trained and saved successfully!")

    return model

model = load_or_train_model()

# ===============================
# Streamlit UI
# ===============================
st.title("🖌️ MNIST Handwritten Digit Classifier 🤖")
st.write("Upload or draw a digit (0–9), and the AI will predict it!")

# Upload image
uploaded_file = st.file_uploader("Upload a 28x28 grayscale image", type=["png","jpg","jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("L")
    st.image(image, caption="Uploaded Digit", use_column_width=True)

    # Preprocess image
    image = ImageOps.invert(image)
    image = image.resize((28, 28))
    image_array = np.array(image) / 255.0
    image_array = image_array.reshape(1, 28, 28, 1)

    # Predict
    prediction = model.predict(image_array)
    predicted_digit = np.argmax(prediction)
    st.success(f"Predicted Digit: {predicted_digit}")

# ===============================
# Drawing Canvas
# ===============================
try:
    from streamlit_drawable_canvas import st_canvas

    st.subheader("Or draw your digit below:")

    canvas_result = st_canvas(
        fill_color="black",
        stroke_width=10,
        stroke_color="white",
        background_color="black",
        height=280,
        width=280,
        drawing_mode="freedraw",
        key="canvas"
    )

    if canvas_result.image_data is not None:
        img = Image.fromarray(canvas_result.image_data[:,:,0]).convert("L")
        img = ImageOps.invert(img)
        img = img.resize((28, 28))
        img_array = np.array(img) / 255.0
        img_array = img_array.reshape(1, 28, 28, 1)

        pred = model.predict(img_array)
        st.success(f"Predicted Digit from Drawing: {np.argmax(pred)}")

except ModuleNotFoundError:
    st.info("🖍️ To enable drawing, install with: pip install streamlit-drawable-canvas")
