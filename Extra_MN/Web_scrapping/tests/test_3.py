import requests as req
import os
from PIL import Image
import cairosvg  


logo_url = "https://www.epn.edu.ec/wp-content/uploads/2023/12/logo-epn-web.svg"


output_folder = r"C:\Users\johan\OneDrive\Escritorio\Universidad\Semestre 4\Métodos Numéricos\GithubRepository\MetodosNumericos_PasquelJohann\Extra_MN\Web_scrapping\img"
svg_file = "logo-epn.svg"
png_file = "logo-epn.png"
jpg_file = "logo-epn.jpg"


os.makedirs(output_folder, exist_ok=True)
svg_path = os.path.join(output_folder, svg_file)
png_path = os.path.join(output_folder, png_file)
jpg_path = os.path.join(output_folder, jpg_file)

response = req.get(logo_url)
if response.status_code == 200:
    with open(svg_path, 'wb') as file:
        file.write(response.content)
    print(f"Archivo SVG guardado en: {svg_path}")

    cairosvg.svg2png(url=svg_path, write_to=png_path)
    print(f"Archivo PNG guardado en: {png_path}")

    png_image = Image.open(png_path)
    rgb_image = png_image.convert('RGB')  
    rgb_image.save(jpg_path)
    print(f"Archivo JPG guardado en: {jpg_path}")
else:
    print(f"Error al descargar el archivo SVG: {response.status_code}")
