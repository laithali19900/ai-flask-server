from flask import Flask, request, send_file
from flask_cors import CORS
from PIL import Image, ImageDraw
import io

app = Flask(__name__)
CORS(app)

@app.route('/process', methods=['POST'])
def process_image():
    image_file = request.files['image']
    theme = request.form['theme']
    size = request.form.get('size', '512x512')
    width, height = map(int, size.split('x'))

    image = Image.open(image_file).convert("RGB")
    image = image.resize((width, height))

    draw = ImageDraw.Draw(image)
    draw.text((10, 10), f"Theme: {theme}", fill=(255, 0, 0))

    img_io = io.BytesIO()
    image.save(img_io, 'JPEG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg')

if __name__ == "__main__":
    app.run()