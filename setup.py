from setuptools import setup, find_packages

setup(
    name="card_classifier",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "torch==2.0.1",
        "torchvision==0.15.2",
        "timm",
        "numpy>=1.20.0",
        "pandas>=1.3.0",
        "matplotlib>=3.4.0",
        "tqdm",
        "opencv-python>=4.5.0",
        "Pillow>=8.0.0",
        "pillow_heif>=0.9.0",
        "pathlib",
        "scikit-image"
    ],
    python_requires=">=3.6",
)

