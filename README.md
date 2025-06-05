## 🧠 Intel Image Classification with Deep Learning

A deep learning project for **classifying natural scenes** using the Intel Image Classification dataset. This notebook demonstrates how to preprocess image data, train CNN-based models, and evaluate performance on a 6-class image dataset including scenes like forests, glaciers, mountains, and more.

---

### 🧰 Features

* 🔍 Image classification using **CNN (Convolutional Neural Network)**
* 🧼 Data preprocessing with **ImageDataGenerator**
* 📊 Real-time model training visualization with **Matplotlib**
* 🧪 Evaluation using accuracy, confusion matrix, and classification report
* 💾 Supports model saving for reuse or deployment

---

### 📁 Dataset

* **Intel Image Classification Dataset**

  * 6 Categories: `buildings`, `forest`, `glacier`, `mountain`, `sea`, `street`
  * Source: [Intel Open Image Dataset on Kaggle](https://www.kaggle.com/puneet6060/intel-image-classification)

---

### 🚀 How to Run

1. Clone this repo or open the notebook in Google Colab:

   ```bash
   git clone https://github.com/your-username/intel-image-classification.git
   ```

2. Install required packages:

   ```bash
   pip install tensorflow matplotlib scikit-learn
   ```

3. Download and unzip the dataset into the working directory.

4. Run the notebook:

   * Train the model
   * Monitor training accuracy and loss
   * Test on validation or unseen data

---

### 📊 Model Performance

* Accuracy: \~90%+ on validation data (depending on epochs/hyperparams)
* Customizable for other image classification tasks

---

### 📌 Use Cases

* Scene recognition in smart cameras
* Baseline for image classification research
* Educational demo for CNNs on real-world data

---

### 📜 License

MIT License. You’re free to use, modify, and distribute.
