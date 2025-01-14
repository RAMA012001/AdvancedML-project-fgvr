# Advanced ML Project: Progressive Multi-task Anti-Noise Learning and Distilling Frameworks for Fine-grained Vehicle Recognition

This repository contains the main notebook for conducting various tasks such as pretraining, model training, data visualization, model distillation, and robustness testing. Below is a detailed outline of what this notebook contains and how to set up the required datasets and pretrained models.

---

## **Contents of the Notebook**

1. **Importation and Setup:**
   - Necessary libraries are imported.
   - Model architecture is defined along with various utility functions.

2. **Notebook Sections:**
   - **Pretraining Data Augmentation:** Prepares the data with various augmentation techniques to improve training robustness.
   - **Training the PMAL Model (Teacher Model):** Trains a primary model with the preprocessed dataset.
   - **Visualization of Image Transformation and Model Classification:** Visualizes how the data is transformed and classified by the model.
   - **Model Distillation (Training the Student Model):** Trains a compact model by leveraging the knowledge of the teacher model.
   - **Testing Robustness to Noise:** Tests the trained models under noisy conditions to assess their robustness.

---

## **Dataset Setup**

This project requires the following datasets to be downloaded and placed in specific folders:

### **1. Stanford Cars Dataset (Selected Subset)**
- **Drive Link:** [Stanford Cars Dataset](https://drive.google.com/drive/folders/1-4DMGkHbD_oR6Wi3C5c3A4EBXpNn_8ow?usp=sharing)
- **Folder:** `downsampled_StanfordCars_data`

### **2. Planes Dataset**
- **Drive Link:** [Planes Dataset](https://drive.google.com/drive/folders/1nW-bGxuaZ9LiXrIti9tr39cIGbiojAW5?usp=sharing)
- **Folder:** `downsampled_plane_data`

---

## **Pretrained Models**

Pretrained models can be downloaded to save time and resources. Place these models in the folder `pretrained_models`.

- **Download Link:** [Pretrained Models](https://drive.google.com/drive/folders/1mcgaF1Fo8PiTyHCE40YHzS97NpNYTmeq?usp=sharing)

---

## **Recorded Results**

For benchmarking and reference, previously recorded results can be downloaded and placed in the folder `recorded_results`.

- **Download Link:** [Recorded Results](https://drive.google.com/drive/folders/1qPcbxjxQ-vCfHsfO0U4l1lAEX1ElvUfc?usp=sharing)

---

## **Instructions**

1. **Setup the Datasets:**
   - Download the Stanford Cars and Planes datasets using the links above.
   - Place them in the corresponding folders (`downsampled_StanfordCars_data` and `downsampled_plane_data`).

2. **Setup Pretrained Models and Results (Optional):**
   - Download the pretrained models and recorded results.
   - Place them in the folders `pretrained_models` and `recorded_results`, respectively.

3. **Run the Notebook:**
   - Open `main_notebook.ipynb` in your preferred Jupyter Notebook environment.
   - Follow the step-by-step sections for training, evaluation, and testing.

---
