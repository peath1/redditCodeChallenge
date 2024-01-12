import cv2
import os
import numpy as np
import csv

def binary_threshold_image(image, threshold_value=120):
    gray_mask = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_mask, threshold_value, 255, cv2.THRESH_BINARY)
    binary_image=cv2.bitwise_not(binary_image)
    return binary_image

def apply_mask_and_check_threshold(image, mask, threshold):
    # Apply the binary mask to the image
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    # Check if values in the masked region are above the threshold
    above_threshold=cv2.bitwise_and(mask, masked_image)
    finalMask = mask - above_threshold
    cv2.imshow("final",finalMask)
    cv2.waitKey(1)
    if cv2.countNonZero(finalMask) < int(0.1*cv2.countNonZero(mask)):
        found=True
    else:
        found=False


    return found,masked_image

def find_and_check_threshold(image_path, shape_directory, threshold=100):
    # Get absolute paths
    image_path = os.path.abspath(image_path)
    shape_directory = os.path.abspath(shape_directory)

    # Load the image
    img = cv2.imread(image_path)
    img=binary_threshold_image(img)
    # cv2.imshow("img",img)
    # cv2.waitKey(50)

    # List of shape filenames
    shape_filenames = ['shape1.png', 'shape2.png', 'shape3.png', 'shape4.png', 'shape5.png', 'shape6.png', 'shape7.png', 'shape8.png']

    # Loop through each shape
    binary=[]
    
    for shape_filename in shape_filenames:
        # Load the shape image
        shape_img = cv2.imread(os.path.join(shape_directory, shape_filename), cv2.IMREAD_UNCHANGED)

        # Convert to binary mask
        binary_mask = binary_threshold_image(shape_img)
        

        # Check if values in the masked region are above the threshold
        above_threshold,masked = apply_mask_and_check_threshold(img, binary_mask, threshold)
        # cv2.imshow("masked symbol",masked)
        # cv2.imshow("pattern",binary_mask)
        # cv2.waitKey(0)
        
        if above_threshold:
            print(f"shape {shape_filename} has values above the threshold. for shape {image_path}")
            binary.append(1)
            
        else:
            
            binary.append(0)
    print("")
    return binary

def split_image(image_path, square_size=50):
    # Load the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Get the dimensions of the image
    height, width = img.shape

    # Initialize an empty list to store the squares
    squares = []

    # Loop through the image in steps of square_size
    for y in range(0, height, square_size):
        for x in range(0, width, square_size):
            # Extract the current square
            square = img[y:y + square_size, x:x + square_size]

            # Ensure the square is the correct size (may not be the case for the last row/column)
            if square.shape == (square_size, square_size):
                squares.append(square)

    return squares




def append_to_csv(file_path, data_list):
    # Open the CSV file in append mode
    with open(file_path, 'a', newline='') as csv_file:
        # Create a CSV writer
        csv_writer = csv.writer(csv_file)

        # Append the list to the CSV file
        csv_writer.writerow(data_list)


def compare_symbols_in_squares(image_path, shapes_directory):
    # Split the image into squares
    squares = split_image(image_path)

    # Loop through each square and compare symbols
    for i, square in enumerate(squares):
        square_path = f'tmps/tmp_square_{i}.png'  # Temporary file to save the square
        cv2.imwrite(square_path, square)     # Save the square to a temporary file

        # Compare symbols in the square
        threshold_value = 120
        output= find_and_check_threshold(square_path, shape_directory, threshold_value)
        append_to_csv("result.csv",output)

# Example usage
image_path = 'final.png'
shape_directory = 'shapes/'


compare_symbols_in_squares(image_path, shape_directory)
