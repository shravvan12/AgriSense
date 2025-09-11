import os
import cv2
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tqdm import tqdm

IMG_SIZE = 128
DATASET_DIR = "data/disease/PlantVillage"
SAVE_DIR = "artifacts/disease"

os.makedirs(SAVE_DIR, exist_ok=True)

def load_and_preprocess_data():
    X = []
    y = []
    class_names = os.listdir(DATASET_DIR)
    class_names.sort()

    print("Classes found:", class_names)

    label_map = {cls_name: i for i, cls_name in enumerate(class_names)}

    for cls_name in class_names:
        cls_folder = os.path.join(DATASET_DIR, cls_name)
        if not os.path.isdir(cls_folder):
            continue
        for img_name in tqdm(os.listdir(cls_folder), desc=f"Processing {cls_name}"):
            img_path = os.path.join(cls_folder, img_name)
            img = cv2.imread(img_path)
            if img is not None:
                img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
                img = img / 255.0
                X.append(img)
                y.append(label_map[cls_name])

    X = np.array(X)
    y = to_categorical(np.array(y))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # ✅ Save preprocessed data
    np.save(os.path.join(SAVE_DIR, "train_images.npy"), X_train)
    np.save(os.path.join(SAVE_DIR, "train_labels.npy"), y_train)
    np.save(os.path.join(SAVE_DIR, "test_images.npy"), X_test)
    np.save(os.path.join(SAVE_DIR, "test_labels.npy"), y_test)

    # ✅ Save label map
    with open(os.path.join(SAVE_DIR, "label_encoder.pkl"), "wb") as f:
        pickle.dump(label_map, f)

    print("✅ Preprocessed data saved to artifacts/disease/")

load_and_preprocess_data()
