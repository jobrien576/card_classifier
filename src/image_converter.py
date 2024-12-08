import os
from PIL import Image
import pillow_heif
from pathlib import Path

# Register HEIF opener with Pillow
pillow_heif.register_heif_opener()

# Source and destination paths
src_dir = r"C:\Users\jobri\OneDrive - Drexel University\MEM679\cards_data"
dest_base = r"C:\Users\jobri\Documents\679\new_cards_data"

def convert_heic_to_jpg(src_path, dest_path):
    try:
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        
        # Open and convert HEIC to JPG
        with Image.open(src_path) as img:
            # Convert to RGB (in case of RGBA images)
            img = img.convert('RGB')
            # Save as JPG
            img.save(dest_path, 'JPEG', quality=95)
            print(f"Converted: {dest_path}")
    except Exception as e:
        print(f"Error converting {src_path}: {str(e)}")

def process_folders():
    # Walk through the source directory
    for root, dirs, files in os.walk(src_dir):
        # Get the relative path from source directory
        rel_path = os.path.relpath(root, src_dir)
        
        for file in files:
            if file.lower().endswith('.heic'):
                # Construct source and destination paths
                src_file = os.path.join(root, file)
                # Replace .heic extension with .jpg
                dest_file = os.path.join(dest_base, rel_path, file.rsplit('.', 1)[0] + '.jpg')
                
                convert_heic_to_jpg(src_file, dest_file)

if __name__ == "__main__":
    # Make sure destination base directory exists
    os.makedirs(dest_base, exist_ok=True)
    
    # Start conversion
    print("Starting HEIC to JPG conversion...")
    process_folders()
    print("Conversion complete!")