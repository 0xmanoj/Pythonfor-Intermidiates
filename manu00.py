import random
from PIL import Image

# Set the dimensions of the image
width = 500
height = 500

# Create a new image with the specified dimensions
image = Image.new('RGB', (width, height))

# Loop through each pixel in the image
for x in range(width):
    for y in range(height):
        
        # Generate a random color for each pixel
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        
        # Set the color of the pixel to the generated color
        image.putpixel((x, y), (red, green, blue))

# Save the generated image
image.save('generated_image.png')
