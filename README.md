# 🏥 Blood Cell Classifier

A simple AI project that classifies blood cells using Convolutional Neural Networks.

## What Does It Do?

Upload a blood cell image → AI predicts the cell type → See results!

**8 Blood Cell Types:** Basophil, Eosinophil, Erythroblast, Immature Granulocytes, Lymphocyte, Monocyte, Neutrophil, Platelet

## Live Demo

Try it here: [Blood Cell Classifier](https://huggingface.co/spaces/sharddha123/Blood-cell-classifier)

## Quick Start

### Run Locally

```bash
# Install packages
pip install -r requirements.txt

# Run app
streamlit run app.py

# Open browser
http://localhost:8501
```

### Or Just Use Online

No installation needed! Click the link above.

## Dataset

- **Source:** BloodMNIST
- **Images:** 17,092 blood cell microscope images
- **Size:** 28×28 pixels
- **Train/Val/Test:** 10,234 / 2,594 / 3,421 images

## Model

- **Type:** Convolutional Neural Network (CNN)
- **Framework:** TensorFlow/Keras
- **Accuracy:** 88.51% on test data
- **Training Data:** 10,234 images
- **Epochs:** 30

## How I Built It

1. Downloaded BloodMNIST dataset
2. Loaded & explored the data
3. Built a CNN with 3 conv layers
4. Added dropout to prevent overfitting
5. Trained for 30 epochs
6. Got 88.51% accuracy
7. Deployed on Hugging Face

## Files

├── app.py # Streamlit web app
├── requirements.txt # Python packages
├── README.md # This file
└── best_blood_cell_model.keras # Trained model


## Results

| Metric | Value |
|--------|-------|
| Train Accuracy | 93.2% |
| Validation Accuracy | 90.2% |
| **Test Accuracy** | **88.51%** |

## Technologies Used

- Python
- TensorFlow/Keras
- Streamlit
- NumPy
- Pillow

## How to Use

1. Go to the [live demo](https://huggingface.co/spaces/sharddha123/Blood-cell-classifier)
2. Click "Browse Files"
3. Upload a blood cell image (JPG/PNG)
4. See the prediction!

**Or run locally:**
```bash
streamlit run app.py
```

## What I Learned

- How CNNs work for image classification
- Data preprocessing & augmentation
- Training neural networks
- Model deployment on Hugging Face

## Future Ideas

- Improve accuracy to 95%+
- Add more cell types
- Build mobile app
- Add explainability features

## About This Project

This is a medical AI project I built to learn deep learning. The model can classify blood cells with 88.51% accuracy. It's deployed on Hugging Face and anyone can use it!

**Not for real medical diagnosis** - just a learning project.

## Contact

- GitHub: [@sharddha123](https://github.com/sharddha123)
- Hugging Face: [sharddha123](https://huggingface.co/sharddha123)

## Dataset Credit

Dataset from [BloodMNIST](https://github.com/MedMNIST/MedMNIST)

---

**Made with ❤️ for learning AI** 🚀
