<h1>Automatic HTML Generator Using Mockup Images</h1>

<h2>Overview</h2>

---

### Sketch to Code: Automatic HTML Code Generator

This project involves automatically generating HTML code from a given sketch or mockup image using deep learning techniques. The system interprets the design and generates corresponding HTML code. Below are the steps involved in the project:

#### 1. **Project Setup**
   - Initialize the project repository and set up the necessary environment using **Python**.
   - Install required libraries such as **YOLOv5**, **TensorFlow**, **OpenCV**, **Pillow**, **NLP tools**, and others.

#### 2. **Data Collection and Preprocessing**
   - Make dataset by sketching mock up images and these images are labelled by using Roboflow.
   - Preprocess the images and HTML files to make them suitable for training the deep learning model.

#### 3. **Object Detection with YOLOv5**
   - Implement the **YOLOv5** algorithm to detect various web page elements such as buttons, text boxes, images, and navigation bars.
   - Train the YOLOv5 model on the mockup images to recognize and classify web elements.

#### 4. **HTML Code Generation**
   - Combine the detected web elements and text content to generate the corresponding **HTML** code.
   - Structure the HTML code based on the positions, sizes, and relationships of elements detected in the mockup.

#### 5. **Model Evaluation**
   - Test the system by providing various mockup images and evaluating the accuracy of the generated HTML code.
   - Compare the generated HTML with the original mockup to assess how closely it matches the design.

#### 6. **Optimization and Refinement**
   - Optimize the model and HTML generation logic to handle more complex mockup designs.
   - Improve the performance and accuracy of the object detection and text content extraction processes.


<h1>Outcome</h1>

![Screenshot 2025-01-26 155850](https://github.com/user-attachments/assets/e5ec4bad-6e5e-4715-9fe0-656e6a2af245)


