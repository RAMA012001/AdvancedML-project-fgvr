import os
from PIL import Image
import cv2
import matplotlib.pyplot as plt

# Downsampling Functions
def nearest_neighbor_downsample(image, size):
    """Downsamples an image using nearest neighbor interpolation."""
    return image.resize(size, Image.NEAREST)

def bilinear_downsample(image, size):
    """Downsamples an image using bilinear interpolation."""
    return image.resize(size, Image.BILINEAR)

def bicubic_downsample(image, size):
    """Downsamples an image using bicubic interpolation."""
    return image.resize(size, Image.BICUBIC)

def gaussian_downsample(image, size):
    """Downsamples an image using Gaussian smoothing before resizing."""
    img_array = cv2.GaussianBlur(cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR), (5, 5), 0)
    img_resized = cv2.resize(img_array, size, interpolation=cv2.INTER_LINEAR)
    return Image.fromarray(cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB))

# Display Function
def display_image(image, title="Image"):
    """Displays a single image."""
    plt.figure(figsize=(8, 8))
    plt.imshow(image)
    plt.axis('off')
    plt.title(title)
    plt.show()

# Dataset Processing Function
def downsample_dataset(dataset_dir, output_dir, downsample_func, size):
    """
    Applies the given downsampling function to all images in the dataset directory.
    
    Args:
        dataset_dir (str): Path to the dataset directory (organized into subfolders).
        output_dir (str): Path to save the downsampled dataset.
        downsample_func (function): Function to downsample a single image.
        size (tuple): Target size (width, height) for downsampling.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for root, dirs, files in os.walk(dataset_dir):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'tiff')):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_dir, os.path.relpath(input_path, dataset_dir))
                
                # Create output directory if it doesn't exist
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                # Load, process, and save the image
                try:
                    image = Image.open(input_path)
                    downsampled_image = downsample_func(image, size)
                    downsampled_image.save(output_path)
                    # print("image saved to :",output_path)
                except Exception as e:
                    print(f"Failed to process {input_path}: {e}")

# Example Usage
# Display an example image
# example_image = Image.open("plane_data/train/A300/0063290.jpg")
# display_image(example_image, title="Original Image")

# Downsample the image
new_size = (128, 128)
# downsampled_image = bilinear_downsample(example_image, new_size)
# display_image(downsampled_image, title="Downsampled Image")

# Downsample the whole dataset
dataset_dir = "StanfordCars_data"
output_dir = "downsampled_StanfordCars_data"
downsample_dataset(dataset_dir, output_dir, bilinear_downsample, new_size)
