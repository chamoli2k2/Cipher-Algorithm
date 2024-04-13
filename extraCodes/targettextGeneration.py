import cv2

def image_to_text(image, filename):
    with open(filename, 'w') as outFile:
        if not outFile:
            print(f"Error: Unable to open file {filename}")
            return
        
        # Write image data to the text file
        for row in image:
            for pixel in row:
                # Write each color channel value to the file
                for channel_value in pixel:
                    outFile.write(f"{int(channel_value)} ")
            outFile.write('\n')  # Move to the next line

    print(f"Image data saved to '{filename}'.")

def main():
    # Read the image
    image = cv2.imread("target.jpg", cv2.IMREAD_COLOR)  # Read in color mode

    if image is None:
        print("Error: Unable to read image.")
        return

    # Save the image data to a text file
    image_to_text(image, "Targettext.txt")

if __name__ == "__main__":
    main()
