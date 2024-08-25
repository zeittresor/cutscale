# cutscale (Python Script to scale Images in a batch to squares)

Script to Scale (up / down all Images of a folder to a square with a given Resolution ex. "python cutscale.py 768" will scale up/down every image using LANCZOS algorithm (using the pillow library) to a square of 768x768 (out of the middle of the image from the shortest side while cutting off the left/right or top/down parts not required to get the square).

Usage:
python cutscale.py 1152
-> Result: Every image of the folder where you execute the script will be scaled to new files with a resolution of 1152 x 1152 with the name 1152_[filename].[png/jpg/jpeg]. The orig. Image will stay untouched.

The Script should work with any resolution to get squares. (Might be useful for ex. using Kohya_ss / Dreambooth lora or embeddings training in Stable Diffusion).
