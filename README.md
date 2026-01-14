#  AgriSense: Smart Agriculture Data & Prediction System

AgriSense is a **Streamlit-based machine learning project** designed to assist farmers and researchers by analyzing agricultural datasets and providing predictions on crop yield, weather patterns, and plant health.  
It also includes a **CNN model** to detect plant diseases from images.

---

##  Project Structure
AgriSense/
|── artifacts
│── app.py # Main Streamlit app
│── models/ # ML models (download separately)
│── data/ # Datasets (download separately)
│── README.md

---

##  Features

-  Crop prediction and recommendations  
-  Weather pattern analysis  
-  Plant disease detection using images (CNN Model)  
-  Interactive data visualization  
-  Easy-to-use Streamlit interface  

---

##  How It Works

 **User Input**  
  
 **Data Collection** (Crop info, Weather data, Plant images)  
  
 **ML Model Processing**  
- Data cleaning & preprocessing  
- Feature extraction  
- Predictions & recommendations  
- CNN model for disease detection  
    
 **Output & Visualization**  
- Crop yield prediction  
- Weather alerts 
- Plant disease detection 
  
 **Streamlit App**  
- Interactive dashboards  
- Charts & graphs  
- User notifications  

 Users can also **download datasets or models** for offline use.

---

##  Tech Stack

**Framework:** Streamlit  
**Machine Learning:** Python (Scikit-learn, Pandas, NumPy, TensorFlow/Keras for CNN)  
**Deployment:** Streamlit Cloud / Localhost  

---

##  Models & Datasets

The trained models and large datasets are **not included** in this repo (too large).  
Please download them using the links below:

-  [Download Artifacts (Google Drive)](https://drive.google.com/drive/folders/1hKQ0gPgWHKkQJ4cpoKfIOuePlZGuNIhu?usp=drive_link)  
-  [Download Datasets (Google Drive)](https://drive.google.com/drive/folders/1FVcyWGiLzmxPanqzbyqG7ALbHLccybqZ?usp=drive_link)  
-  [Plant Disease Dataset (Kaggle)](https://www.kaggle.com/datasets/emmarex/plantdisease)  

After downloading, place them in this structure:
AgriSense/
|── artifacts/
│── models/
│── data/
##  Getting Started

### 1️ Clone the Repository
git clone https://github.com/shravvan12/AgriSense.git
cd AgriSense

### 2️ Install Dependencies
pip install -r requirements.txt

### 3️ Run the App
streamlit run app.py

---
###  Contribution

Contributions are welcome! Feel free to open issues or submit PRs.


