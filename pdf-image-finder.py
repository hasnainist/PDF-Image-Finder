import fitz # PyMuPDF
import io
from PIL import Image
# file path you want to extract images from
file = "document.pdf"
# open the file
pdf_file = fitz.open(file)

# iterate over PDF pages
for page_index in range(len(pdf_file)):
    # get the page itself
    page = pdf_file[page_index]
    # get image list
    image_list = page.get_images()

    for image_index, img in enumerate(image_list, start=1):
        # get the XREF of the image
        xref = img[0]
        # extract the image bytes
        base_image = pdf_file.extract_image(xref)
        image_bytes = base_image["image"]
        # # get the image extension
        # image_ext = base_image["ext"]
        # load it to PIL
        image = Image.open(io.BytesIO(image_bytes))

        #image we want to search the pdf for
        image2 = Image.open("test.png")

# Compare the pixel data of the two images
        if image.mode == image2.mode and image.size == image2.size:
          image1_data = image.tobytes()
          image2_data = image2.tobytes()
          if image1_data == image2_data:
              print("")
              print("image match found on page "+str(page_index+1))
              print("")
              
          
    