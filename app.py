from flask import Flask
app = Flask(__name__)

CORS(app)

@app.route('/process', methods=['POST'])
def process_image():
    image_file = request.files['image']
    theme = request.form['theme']

    # افتح الصورة
    image = Image.open(image_file).convert("RGB")
    
    # رسم وهمي: نكتب اسم الثيم على الصورة
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), f"Theme: {theme}", fill=(255, 0, 0))

    # حفظ الصورة بذاكرة مؤقتة
    img_io = io.BytesIO()
    image.save(img_io, 'JPEG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)

