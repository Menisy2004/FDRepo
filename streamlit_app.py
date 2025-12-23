import streamlit as st

st.set_page_config(page_title='Face Detection Project', layout='wide')
st.title('Face detection Model')


section = st.sidebar.selectbox(
    "Navigate to section:",
    ["Introduction", "Dataset", "Model Architecture", "Training", "Live Demo", "Conclusion"]
)



if section == "Introduction":
    st.header("Introduction")
    st.markdown(
        """
        <p style="text-align: justify;">
        Face detection is a fundamental problem in computer vision that focuses on locating and identifying human faces within digital images or video streams. It serves as a critical preprocessing step for many real-world applications such as face recognition, surveillance systems, human–computer interaction, and biometric authentication. Traditional face detection methods relied on handcrafted features and rule-based classifiers; however, these approaches often struggle with variations in lighting, pose, scale, and background complexity.
        </p>

        <p style="text-align: justify;">
        With the advancement of deep learning, convolutional neural networks (CNNs) have become the dominant approach for face detection tasks due to their ability to automatically learn hierarchical feature representations from raw image data. In this project, a face detection model based on the VGG16 convolutional neural network architecture is implemented. VGG16 is a deep CNN composed of 16 trainable layers and is well known for its use of small 3×3 convolutional filters stacked in depth, which enables effective extraction of high-level visual features. By leveraging a VGG16 network pretrained on the ImageNet dataset, the model benefits from transfer learning, allowing it to achieve improved accuracy and faster convergence even with limited training data. The extracted features are then utilized to detect facial regions accurately, making the proposed system robust to variations in facial appearance and environmental conditions.
        </p>
        """,
        unsafe_allow_html=True
    )

if section == "Dataset":
    st.header("Tools for Dataset Generation")
    st.markdown(
        """
        <p style='text-align: justify;'>
        To build and train the face detection model, several essential libraries were installed. 
        These tools provide functionality for dataset preparation, deep learning, image processing, 
        visualization, and augmentation.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Installation")
    st.code("!pip install labelme tensorflow opencv-python matplotlib albumentations", language="bash")

    # Library descriptions
    st.subheader("Library Descriptions")
    st.markdown(
        """
        - **Labelme**  
          A graphical image annotation tool used to create bounding boxes, polygons, and masks for training datasets.  
          In this project, it helps generate labeled data for supervised learning.

        - **TensorFlow**  
          A powerful deep learning framework that provides the core infrastructure for building and training 
          the VGG16‑based face detection model. It handles neural network layers, optimization, and GPU acceleration.

        - **OpenCV (opencv-python)**  
          A computer vision library used for image preprocessing tasks such as resizing, color conversion, 
          and drawing bounding boxes on detected faces.

        - **Matplotlib**  
          A visualization library that allows plotting of training curves, accuracy graphs, 
          and displaying sample detection results.

        - **Albumentations**  
          A fast and flexible image augmentation library that improves model robustness by applying transformations 
          such as rotation, flipping, scaling, and brightness adjustments to training images.
        """
    )
    st.header("📸Image Collection using OpenCV")
    st.markdown(
        """
        <p style='text-align: justify;'>
        OpenCV (cv2) provides direct access to the webcam, allowing us to capture images or video frames 
        in real time. This is essential for building datasets dynamically, where each frame can be saved 
        and later annotated for training. The following code snippet shows the libraries used to support 
        this process.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Imports")
    st.code(
        """import os
           import time
           import uuid
           import cv2""",
           language="python"
    )

    st.subheader("Explanation of Libraries")
    st.markdown(
        """
        - **os**  
          Provides functions to interact with the operating system, such as creating folders 
          to store captured images.
        - **time**  
          Used to manage delays or timestamps, ensuring frames are captured at specific intervals.

        - **uuid**  
          Generates unique identifiers for each captured image, preventing filename conflicts 
          and making dataset organization easier.

        - **cv2 (OpenCV)**  
          The core library for computer vision tasks. Here, it connects to the webcam, 
          captures frames, and allows saving them as images for dataset creation.
        """
    )
    st.subheader("Capturing Images")
    st.code("""
            IMAGES_PATH = os.path.join('data','images')
            number_images = 30
            cap = cv2.VideoCapture(1)
            for imgnum in range(number_images):
            print('Collecting image {}'.format(imgnum))
            ret, frame = cap.read()
            imgname = os.path.join(IMAGES_PATH,f'{str(uuid.uuid1())}.jpg')
            cv2.imwrite(imgname, frame)
            cv2.imshow('frame', frame)
            time.sleep(0.5)

            if cv2.waitKey(1) & 0xFF == ord('q'):
               break
            cap.release()
            cv2.destroyAllWindows()""",language="python"
           )
    st.markdown("""
    <p style='text-align: justify;'>
    This code connects to the webcam, captures 30 images, saves each one with a unique filename, 
    and displays the frame while collecting. A short delay is added between captures, and the user 
    can press <code>q</code> to stop early. The images are stored in the <code>data/images</code> folder.
    </p>
    """,
    unsafe_allow_html=True
    )
    st.subheader('Live Image from Webcam')
    st.image('44d63787-dd02-11f0-8374-189341bd87be.jpg', width=300, caption="Sample image from dataset")
    st.subheader('Annotation')
    st.code("""!labelme""",language="python")
    st.markdown("""<p style='text-align: justify;'> Get into labelme to annotate images of dataset</p>""",unsafe_allow_html=True)
    st.image('i3.png',width=300,caption="Bounding box on human face")

    st.subheader("📊 Dataset Segmentation")

    st.markdown(
        """
        <p style='text-align: justify;'>
        A total of <b>100 images</b> were captured using the webcam for building the dataset. 
        To ensure proper training and evaluation of the face detection model, the dataset was 
        divided into three subsets:
        </p>
        """,
        unsafe_allow_html=True
       )
    st.code("""
     for folder in ['train','test','val']:
      for file in os.listdir(os.path.join('data', folder, 'images')):
        
        filename = file.split('.')[0]+'.json'
        existing_filepath = os.path.join('data','labels', filename)
        if os.path.exists(existing_filepath): 
            new_filepath = os.path.join('data',folder,'labels',filename)
            os.replace(existing_filepath, new_filepath)""", language="python")
    st.markdown(
      """
       - **Training Set (70 images)** → Used to train the model and learn feature representations.  
       - **Testing Set (15 images)** → Used to evaluate the model during development and measure performance.  
       - **Validation Set (15 images)** → Used to fine-tune hyperparameters and prevent overfitting.  
      """
     )

    st.subheader("🖼Apply Image Augmentation on Images and Labels using Albumentations")
    st.markdown(
    """
    <p style='text-align: justify;'>
    To improve model robustness and increase the effective dataset size, 
    we apply <b>data augmentation</b> using the Albumentations library. 
    Augmentation generates new variations of existing images by applying 
    random transformations such as cropping, flipping, brightness adjustment, 
    and color shifting. This helps the model generalize better to unseen data 
    and reduces overfitting.
    </p>
    """,
    unsafe_allow_html=True
    )

    st.subheader("Code Snippet")
    st.code(
    """augmentor = alb.Compose([
    alb.RandomCrop(width=450, height=450),
    alb.HorizontalFlip(p=0.5),
    alb.RandomBrightnessContrast(p=0.2),
    alb.RandomGamma(p=0.2),
    alb.RGBShift(p=0.2),
    alb.VerticalFlip(p=0.5)],
    bbox_params=alb.BboxParams(format='albumentations',
                               label_fields=['class_labels']))
    """,
    language="python"
    )

    st.subheader("Explanation of Transformations")
    st.markdown(
    """
    - **RandomCrop** → Crops images to a fixed size (450×450), focusing on different regions.  
    - **HorizontalFlip** → Flips images left-to-right with 50% probability.  
    - **RandomBrightnessContrast** → Adjusts brightness and contrast randomly (20% chance).  
    - **RandomGamma** → Alters gamma values to simulate lighting changes.  
    - **RGBShift** → Randomly shifts color channels to add variation.  
    - **VerticalFlip** → Flips images top-to-bottom with 50% probability.  
    - **bbox_params** → Ensures bounding boxes and labels remain consistent after transformations.  
    """
  )

    st.subheader("📊 Results After Augmentation")

    st.markdown(
        """
        - **Training Set** → 4,140 images  
        - **Testing Set** → 900 images  
        - **Validation Set** → 900 images  
        - Total images 5940 images
        """
    )



if section == "Model Architecture":

    st.header("🧠 Convolutional Neural Networks (CNNs) – Background")

    st.markdown(
        """
        <p style='text-align: justify;'>
        A Convolutional Neural Network (CNN) is a type of deep learning model specifically designed
        to process image data. Unlike traditional neural networks, CNNs preserve the spatial structure
        of images, allowing them to learn visual patterns such as edges, textures, shapes, and objects.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style='text-align: justify;'>
        CNNs work by applying small learnable filters (kernels) across an image. These filters detect
        local patterns, and deeper layers combine simpler patterns into more complex features.
        This hierarchical feature learning makes CNNs especially effective for computer vision tasks.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.header("🏗️ VGG16 Architecture")

    st.markdown(
        """
        <p style='text-align: justify;'>
        VGG16 is a deep convolutional neural network architecture developed by the Visual Geometry Group
        (VGG) at Oxford University. It is one of the most well-known and widely used CNN architectures
        due to its simplicity, depth, and strong performance on image recognition tasks.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Why VGG16?")

    st.markdown(
        """
        <p style='text-align: justify;'>
        VGG16 is chosen in this project because it provides powerful feature extraction while maintaining
        a simple and uniform architecture. It uses only 3×3 convolution filters and a consistent stacking
        pattern, which makes it easy to understand, explain, and extend for custom tasks such as face detection.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Core Building Blocks of VGG16")

    st.markdown(
        """
        <p style='text-align: justify;'>
        The VGG16 architecture is composed of repeated blocks, each consisting of convolutional layers
        followed by a pooling layer. These blocks gradually reduce spatial dimensions while increasing
        feature depth.
        </p>
        """,
        unsafe_allow_html=True
    )

    # VGG16 Architecture Image
    st.image(
        "vgg-16.bak.png",
        caption="VGG16 convolutional backbone",
        use_column_width=True
    )

    st.subheader("Depth and Feature Extraction")

    st.markdown(
        """
        <p style='text-align: justify;'>
        VGG16 contains 16 weight layers, with depth increasing as spatial resolution decreases.
        Early layers focus on low-level features such as edges, while deeper layers learn high-level
        semantic information. By the final convolutional block, the network has a rich understanding
        of the image content.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.header("🔄 Using VGG16 as a Feature Extractor")

    st.markdown(
        """
        <p style='text-align: justify;'>
        In this project, VGG16 is used as a feature extractor rather than a classifier.
        The fully connected layers originally designed for ImageNet classification are removed
        by setting <code>include_top=False</code>.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style='text-align: justify;'>
        This allows the model to reuse the learned convolutional filters while adapting the network
        to a new task: face detection. The output of the VGG16 backbone is a high-level feature map
        that summarizes important visual information from the input image.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.header("📉 Global Max Pooling")

    st.markdown(
        """
        <p style='text-align: justify;'>
        After feature extraction, Global Max Pooling is applied. This operation converts each feature
        map into a single value by selecting the maximum activation. As a result, the spatial dimensions
        are removed while preserving the most significant features detected by the network.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style='text-align: justify;'>
        Global Max Pooling produces a fixed-length feature vector regardless of image size,
        making it ideal for connecting convolutional layers to fully connected layers.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.header("🎯 Multi-Task Model Architecture")

    st.markdown(
        """
        <p style='text-align: justify;'>
        The extracted features from VGG16 are shared between two parallel output branches.
        This design follows a multi-task learning approach, where a single backbone supports
        multiple objectives.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.subheader("1️⃣ Face Classification Head")

    st.markdown(
        """
        <p style='text-align: justify;'>
        The classification head determines whether a face is present in the image.
        It consists of fully connected layers that analyze the extracted features and
        output a single probability value using a sigmoid activation function.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        - Output: Probability between 0 and 1  
        - Purpose: Face presence detection (face / no face)
        """
    )

    st.subheader("2️⃣ Bounding Box Regression Head")

    st.markdown(
        """
        <p style='text-align: justify;'>
        The regression head predicts the location of the face by estimating four normalized
        values representing the bounding box coordinates.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        - Output format: [x_min, y_min, x_max, y_max]  
        - Values are normalized to the range [0, 1]  
        - Sigmoid activation ensures valid coordinate predictions
        """
    )

    st.header("⚙️ Summary of the Architecture")

    st.markdown(
        """
        <p style='text-align: justify;'>
        In summary, this model combines a pretrained VGG16 convolutional backbone with a
        multi-task learning strategy. The shared feature extractor enables efficient and
        accurate face detection, while the dual-head design allows simultaneous classification
        and localization in a single forward pass.
        </p>
        """,
        unsafe_allow_html=True
    )

if section == 'Training':

    st.header("⚙️ Model Training")
    
    st.markdown(
        """
        <p style='text-align: justify;'>
        The face detection model is trained using the <code>model.fit()</code> function, which takes in the training data, 
        validation data, and a callback for TensorBoard logging. The training runs for <b>10 epochs</b>, meaning the model 
        sees the entire training dataset 10 times. This number was chosen based on early experimentation — it provides 
        enough iterations for the model to learn meaningful features without overfitting.
        </p>
    
        <p style='text-align: justify;'>
        During training, the model optimizes both classification and regression losses. Classification focuses on identifying 
        whether a region contains a face, while regression predicts the bounding box coordinates. Validation data is used to 
        monitor generalization performance after each epoch.
        </p>
        """,
        unsafe_allow_html=True
    )
    
    st.subheader("Training Code")
    st.code(
        """hist = model.fit(train, epochs=10, validation_data=val, callbacks=[tensorboard_callback])""",
        language="python"
    )
    
    st.subheader("📷 Training Results Snapshot")
    st.image("res-2.jpeg")
    
    # --- Continue with previous visualization section ---
    st.header("📈 Training Performance Visualization")
    
    st.markdown(
        """
        <p style='text-align: justify;'>
        After training the face detection model, we visualize its performance using three key loss metrics: 
        <b>total loss</b>, <b>classification loss</b>, and <b>regression loss</b>. 
        These graphs help evaluate how well the model is learning and generalizing to validation data.
        </p>
    
        <p style='text-align: justify;'>
        The following code generates three side-by-side line plots using Matplotlib. Each plot compares 
        training loss and validation loss across epochs. This allows us to monitor convergence, detect 
        overfitting, and assess the balance between classification and regression components.
        </p>
        """,
        unsafe_allow_html=True
    )
    
    st.subheader("Loss Visualization Code")
    st.code(
        """fig, ax = plt.subplots(ncols=3, figsize=(20,5))
    
    ax[0].plot(hist.history['total_loss'], color='teal', label='loss')
    ax[0].plot(hist.history['val_total_loss'], color='orange', label='val loss')
    ax[0].title.set_text('Loss')
    ax[0].legend()
    
    ax[1].plot(hist.history['class_loss'], color='teal', label='class loss')
    ax[1].plot(hist.history['val_class_loss'], color='orange', label='val class loss')
    ax[1].title.set_text('Classification Loss')
    ax[1].legend()
    
    ax[2].plot(hist.history['regress_loss'], color='teal', label='regress loss')
    ax[2].plot(hist.history['val_regress_loss'], color='orange', label='val regress loss')
    ax[2].title.set_text('Regression Loss')
    ax[2].legend()
    
    plt.show()""",
        language="python"
    )
    
    st.subheader("Explanation of Graphs")
    st.markdown(
        """
        - **Loss Plot** → Shows overall training and validation loss across epochs.  
        - **Classification Loss Plot** → Tracks how well the model classifies face regions.  
        - **Regression Loss Plot** → Measures accuracy of bounding box predictions.  
        - **Color Coding** → Teal for training loss, orange for validation loss.  
        - **Layout** → Three plots arranged horizontally using `ncols=3` and `figsize=(20,5)`.  
        """
    )
    st.image('res-1.jpeg')
if section == "Conclusion":
    st.header("🏁 Conclusion")

    st.markdown(
        """
        <p style="text-align: justify;">
        This project demonstrates the development of a <b>face detection system</b> using
        deep learning and an interactive <b>Streamlit interface</b>.
        The system covers the main stages of a computer vision pipeline, including
        dataset collection, annotation, model training, and real-time face detection.
        </p>

        <p style="text-align: justify;">
        A pretrained <b>VGG16</b> model was used as a feature extractor to improve accuracy
        and reduce training time through transfer learning.
        The model performs two tasks at the same time: detecting whether a face exists
        and predicting the bounding box location.
        </p>

        <p style="text-align: justify;">
        Data augmentation helped improve the model’s ability to handle different lighting
        conditions and face positions.
        Streamlit provided a simple and user-friendly interface that allows easy navigation
        and live webcam testing.
        </p>

        <p style="text-align: justify;">
        In conclusion, this project shows how deep learning can be applied to solve
        real-world face detection problems.
        Future improvements may include using larger datasets, detecting multiple faces,
        or applying more advanced detection models.
        </p>
        """,
        unsafe_allow_html=True
    )


if section == "Live Demo":

    st.header("🎥 Live Face Detection Demo")

    st.markdown(
        """
        <p style='text-align: justify;'>
        The following video demonstrates the real-time face detection system in action.
        The model processes each frame, predicts the presence of a face, and draws a
        bounding box around the detected region when a face is identified.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.video("videos/face_detection_demo.mp4")

