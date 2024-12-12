# Card Classifier

## Overview

**Card Classifier** is a PyTorch-based machine learning project that recognizes and classifies playing cards from custom image datasets. The project follows a structured workflow, starting from preprocessing the dataset to training a neural network model, visualizing losses, and evaluating results.

This repository is designed for modular and reproducible development with key scripts for preprocessing, model training, and inference.

---

## Features

- **Custom Dataset Handling**: Loads and preprocesses card images using PyTorch datasets and dataloaders.
- **Neural Network Implementation**: Includes a customizable PyTorch model for card classification.
- **Training and Evaluation**: Contains a training loop with loss visualization and evaluation metrics.
- **Extensible Codebase**: Organized for ease of maintenance and scalability.

---

## Repository Structure

```plaintext
.
├── src/
│   ├── classifier.ipynb        # Jupyter Notebook for prototyping and training
│   ├── cropped_cards.py        # Script for cropping and preprocessing card images
│   ├── image_converter.py      # Helper script for image format conversions
├── docs/                       # Documentation folder
├── tests/                      # Unit tests
├── requirements.txt            # Python dependencies
├── setup.py                    # Project setup script
├── .gitignore                  # Ignored files for Git
├── README.md                   # Project documentation
```

---

## Workflow

### Step 1: PyTorch Dataset and Dataloader

- **Create Training and Test Datasets**: The dataset is organized into folders, each named after the card type (e.g., `5_club`, `K_heart`).
- **Dataloader**: Preprocesses the images and batches them for training.

### Step 2: PyTorch Model

- Implements a neural network tailored for card image classification.
- Customizable architecture defined in the training script or notebook.

### Step 3: Training Loop

- Includes dataset setup and a simple training loop.
- Visualizes training losses and accuracy to monitor performance.

### Step 4: Evaluate Results

- Evaluates the model on the test set using confusion matrices and accuracy scores.
- Generates predictions for individual images.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/card_classifier.git
   cd card_classifier
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### 1. Preprocess the Dataset

Use the `cropped_cards.py` script to preprocess images. Ensure your dataset is structured into folders by card type (e.g., `7_diamond`).

### 2. Train the Model

Open `classifier.ipynb` in Jupyter Notebook and follow these steps:
- Load the dataset using PyTorch Datasets and Dataloaders.
- Define the neural network architecture.
- Train the model with the provided training loop.

### 3. Visualize Losses

The notebook includes functionality to plot and analyze training losses.

### 4. Test the Model

Use the trained model to classify test images. Modify the notebook to point to test images or datasets.

---

## Dataset Format

- Organize images into folders named `<rank>_<suit>` (e.g., `A_club`, `10_spade`).
- Each folder should contain `.jpg` or `.png` images of the respective card.

---

## Requirements

This project uses Python 3.8 or higher and the following packages:
- `torch==2.0.1`
- `torchvision==0.15.2`
- `timm`
- `numpy>=1.20.0`
- `pandas>=1.3.0`
- `matplotlib>=3.4.0`
- `tqdm`
- `opencv-python>=4.5.0`
- `Pillow>=8.0.0`
- `pillow_heif>=0.9.0`
- `pathlib`
- `scikit-image`
- `pytest`
- `scikit-learn`

Install them using `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## Contribution

Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## Author

Developed by [Joby O'Brien]. For questions or feedback, reach out at [jo576@drexel.edu].
