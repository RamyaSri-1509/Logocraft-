from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog

def generate_logo(text, font_size, font_color, background_color, output_file):
    try:
        # Create a new image with white background
        img = Image.new('RGB', (500, 200), color=background_color)
        
        # Create a drawing context
        d = ImageDraw.Draw(img)
        
        # Load the font
        font = ImageFont.truetype("arial.ttf", font_size)
        
        # Draw the text on the image
        d.text((10, 10), text, fill=font_color, font=font)
        
        # Save the image to a file
        img.save(output_file)
        
        print("Logo generated successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Create a new Tkinter window
    window = tk.Tk()
    window.title("Logo Generator")
    
    # Create a label and entry field for the text
    tk.Label(window, text="Enter text:").grid(row=0, column=0)
    text_entry = tk.Entry(window)
    text_entry.grid(row=0, column=1)
    
    # Create a label and entry field for the font size
    tk.Label(window, text="Font size:").grid(row=1, column=0)
    font_size_entry = tk.Entry(window)
    font_size_entry.grid(row=1, column=1)
    
    # Create a label and entry field for the font color
    tk.Label(window, text="Font color:").grid(row=2, column=0)
    font_color_entry = tk.Entry(window)
    font_color_entry.grid(row=2, column=1)
    
    # Create a label and entry field for the background color
    tk.Label(window, text="Background color:").grid(row=3, column=0)
    background_color_entry = tk.Entry(window)
    background_color_entry.grid(row=3, column=1)
    
    # Create a button to generate the logo
    def generate_logo_button_clicked():
        text = text_entry.get()
        font_size = int(font_size_entry.get())
        font_color = font_color_entry.get()
        background_color = background_color_entry.get()
        output_file = filedialog.asksaveasfilename(defaultextension=".png")
        generate_logo(text, font_size, font_color, background_color, output_file)
    
    tk.Button(window, text="Generate Logo", command=generate_logo_button_clicked).grid(row=4, column=0, columnspan=2)
    
    # Start the Tkinter event loop
    window.mainloop()

if __name__ == "__main__":
    main()
