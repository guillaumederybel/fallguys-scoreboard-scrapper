import cv2
import pytesseract
from PIL import Image
from pytesseract import Output

def qualified_title(image):
    """This function will retreive the number of
    qualified people for the next round."""

    title_top = 40
    title_height = 180
    title_left = 550
    title_lenght = 1370

    cropped_title = original_image[title_top:title_height, title_left:title_lenght]
    gray_title = cv2.cvtColor(cropped_title, cv2.COLOR_BGR2GRAY)
    title = Image.fromarray(gray_title)

    text = pytesseract.image_to_string(title)

    return text

original_image = cv2.imread('images/fgafter.png')
qualified = qualified_title(original_image)
print(qualified)
