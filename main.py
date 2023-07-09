from PIL import Image
import pandas as pd

image_path = 'imagen.jpg'
image = Image.open(image_path)

pixel_data = list(image.getdata())

df = pd.DataFrame(pixel_data, columns=['R', 'G', 'B'])

output_path = 'imagen.parquet'
df.to_parquet(output_path)