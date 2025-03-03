from PIL import Image, ImageDraw, ImageFont

def text_to_image(text, output_path="output.png", image_size=(500, 300), font_size=40):
    # Create a blank image with white background
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)
    
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
    
    # Get text size and position it in the center
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)
    
    # Draw text on the image
    draw.text(position, text, fill="black", font=font)
    
    # Save the image
    image.save(output_path)
    print(f"Image saved as {output_path}")

if __name__ == "__main__":
    user_text = input("Enter the text to convert into an image: ")
    text_to_image(user_text)
