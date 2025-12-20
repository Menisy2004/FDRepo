import streamlit as st

st.set_page_config(page_title='Face Detection Project', layout='wide')
st.title('Face detection Model')

section = st.sidebar.radio(
    "Go to",
    [
        "Introduction",
        "Dataset",
        "Model Architecture",
        "Training",
        "Results",
        "Live Demo",
        "Conclusion"
    ]
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



if section == "Model Architecture":

    st.header("🧠 Convolutional Neural Network (CNN) Fundamentals")

    st.markdown(
        """
        <p style='text-align: justify;'>
        A Convolutional Neural Network (CNN) is a specialized type of neural network designed to process
        image data. Unlike traditional neural networks, CNNs preserve spatial information such as height,
        width, and color channels, allowing them to detect visual patterns like edges, shapes, and objects.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.subheader("How CNNs Process Images")
    st.markdown(
        """
        <p style='text-align: justify;'>
        Images are represented as numerical tensors. A CNN applies convolutional filters that slide over
        the image to extract meaningful features. Early layers detect simple patterns such as edges,
        while deeper layers detect complex structures like facial features.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.image(
        "images/cnn_convolution.png",
        caption="Convolution operation using a sliding filter",
        use_column_width=True
    )

    st.subheader("Pooling and Feature Reduction")
    st.markdown(
        """
        <p style='text-align: justify;'>
        Pooling layers reduce the spatial dimensions of feature maps while preserving the most important
        information. Max Pooling selects the maximum value from a region, making the network robust to
        small shifts and reducing computation.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.image(
        "images/max_pooling.png",
        caption="Max Pooling operation",
        use_column_width=True
    )

    st.header("🏗️ Model Architecture Overview")

    st.markdown(
        """
        <p style='text-align: justify;'>
        The face detection model follows a multi-task learning architecture with a shared convolutional
        backbone and two parallel output heads. The shared backbone extracts visual features, while the
        heads perform classification and bounding box regression.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Backbone Network: VGG16")

    st.markdown(
        """
        <p style='text-align: justify;'>
        VGG16 is a deep convolutional neural network pretrained on the ImageNet dataset. In this project,
        it is used as a feature extractor by removing its fully connected layers and retaining only the
        convolutional layers. This allows the model to leverage powerful learned visual representations.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.image(
        "images/vgg16_architecture.png",
        caption="VGG16 convolutional backbone",
        use_column_width=True
    )

    st.subheader("Global Max Pooling")

    st.markdown(
        """
        <p style='text-align: justify;'>
        Global Max Pooling converts the final convolutional feature maps into a fixed-length feature vector
        by selecting the maximum activation from each feature map. This summarizes the most important
        visual signals detected by the network.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Classification Head")

    st.markdown(
        """
        <p style='text-align: justify;'>
        The classification head determines whether a face exists in the image. It uses fully connected
        layers to analyze the extracted features and outputs a probability using a sigmoid activation
        function.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Bounding Box Regression Head")

    st.markdown(
        """
        <p style='text-align: justify;'>
        The regression head predicts the bounding box coordinates of the detected face. The output consists
        of four normalized values representing the top-left and bottom-right corners of the bounding box.
        A sigmoid activation ensures outputs remain within valid bounds.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.image(
        "images/model_architecture.png",
        caption="Complete face detection model architecture",
        use_column_width=True
    )

    


