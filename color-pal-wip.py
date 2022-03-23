import math
import PIL
try:
    import Image
except ImportError:
    from PIL import Image
import extcolors
import numpy as np
import urllib.request
import matplotlib.pyplot as plt
from PIL import ImageDraw
from matplotlib import gridspec

def understand_image(path_to_image):
  img = fetch_image(path_to_image)
  colors = extract_colors(img)
  color_palette = render_color_palette(colors)
  overlay_palette(img, color_palette)
  
def fetch_image(image_path):
  urllib.request.urlretrieve(image_path, "image")
  img = PIL.Image.open("image")
  return img

def extract_colors(img):
  tolerance = 32
  limit = 24
  colors, pixel_count = extcolors.extract_from_image(img, tolerance, limit)
  return colors

def render_color_palette(colors):
  size = 100
  columns = 6
  width = int(min(len(colors), columns) * size)
  height = int((math.floor(len(colors) / columns) + 1) * size)
  result = Image.new("RGBA", (width, height), (0, 0, 0, 0))
  canvas = ImageDraw.Draw(result)
  for idx, color in enumerate(colors):
      x = int((idx % columns) * size)
      y = int(math.floor(idx / columns) * size)
      canvas.rectangle([(x, y), (x + size - 1, y + size - 1)], fill=color[0])
  return result

def overlay_palette(img, color_palette):
  nrow = 2
  ncol = 1
  f = plt.figure(figsize=(20,30), facecolor='None', edgecolor='k', dpi=55, num=None)
  gs = gridspec.GridSpec(nrow, ncol, wspace=0.0, hspace=0.0) 
  f.add_subplot(2, 1, 1)
  plt.imshow(img, interpolation='nearest')
  plt.axis('off')
  f.add_subplot(1, 2, 2)
  plt.imshow(color_palette, interpolation='nearest')
  plt.axis('off')
  plt.subplots_adjust(wspace=0, hspace=0, bottom=0)
  plt.show(block=True)
  
image_url1 = 'https://nypost.com/wp-content/uploads/sites/2/2021/01/coachella-2021-cancelled.jpg?quality=80&strip=all'
understand_image(image_url1)

image_url2 = 'https://media.newyorker.com/photos/590976111c7a8e33fb38f667/master/pass/Battan-TheAppealoftheCoachellaWayofLife.jpg'
understand_image(image_url2)

image_url3 = 'https://www.glamourstylephotobooth.com/wp-content/uploads/2019/03/GSPB_COLOR_0073.jpg'
understand_image(image_url3)
