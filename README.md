# cutscale (Python Script to scale Images in a batch to squares)

Script to Scale (up / down all Images of a folder to a square with a given Resolution ex. "python cutscale.py 768" will scale up/down every image using LANCZOS algorithm (using the pillow library) to a square of 768x768 (out of the middle of the image from the shortest side while cutting off the left/right or top/down parts not required to get the square).

The new file do not overwrite the original file, just a new file will be created with the choosen resolution in front ex. 768_[filename].png (should work with .png, .jpg and .jpeg images).

The Script should work with any resolution to get squares. (Might be useful for ex. using Kohya_ss / Dreambooth lora or embeddings training in Stable Diffusion).
