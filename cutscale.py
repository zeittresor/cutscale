import os
from PIL import Image
import sys

def resize_and_crop(image_path, output_size):
    img = Image.open(image_path)
    width, height = img.size
    
    if width < height:
        new_width = output_size
        new_height = int(height * (output_size / width))
    else:
        new_height = output_size
        new_width = int(width * (output_size / height))
    
    img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    left = (new_width - output_size) / 2
    top = (new_height - output_size) / 2
    right = (new_width + output_size) / 2
    bottom = (new_height + output_size) / 2
    
    img_cropped = img_resized.crop((left, top, right, bottom))
    
    directory, filename = os.path.split(image_path)
    new_filename = f"{output_size}_{filename}"
    new_image_path = os.path.join(directory, new_filename)
    
    img_cropped.save(new_image_path)

    print(f"Image successfully saved: {new_image_path}")

def batch_process_images(output_size):
    current_directory = os.getcwd()
    supported_formats = ('.png', '.jpg', '.jpeg')

    for filename in os.listdir(current_directory):
        if filename.lower().endswith(supported_formats):
            image_path = os.path.join(current_directory, filename)
            try:
                resize_and_crop(image_path, output_size)
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scriptname.py [resolution]")
        sys.exit(1)

    try:
        output_size = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid number for the resolution.")
        sys.exit(1)

    batch_process_images(output_size)
