import cv2
import os

#  set path 
input_folder = "."
output_folder = os.path.join(input_folder, "blurred_outputs")
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"blurred_{filename}")
        
        # read the image
        image = cv2.imread(input_path)

        # Apply Gaussian blur
        blurred_image = cv2.GaussianBlur(image, (5, 5), 3)
        
        # Save the resulting image
        cv2.imwrite(output_path, blurred_image)

print("Completed.")
