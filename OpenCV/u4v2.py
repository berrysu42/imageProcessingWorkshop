"""
import cv2 as cv
import numpy as np
import gradio as gr

def nostalji(image):
    image = np.array(image)
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return gray_image

# Gradio arayüzünü oluştur
with gr.Blocks() as demo:
    gr.Markdown("Görseli Siyah beyaza çevir!")
    gr.Markdown("Bir resim yükleyin ve siyah beyaza çevrilsin!")

    image_input = gr.Image(type='pil')
    image_output = gr.Image(type="numpy", label="Sonuç Resmi")

    # Fonksiyonu gradio bileşenlerine bağlayalım
    gr.Interface(fn=nostalji, inputs=[image_input], outputs=[image_output]).launch()

# Arayüzü başlatma
if __name__ == "__main__":
    demo.launch()
"""
"""
import cv2 as cv
import numpy as np
import gradio as gr

def nostalji(image):
    image = np.array(image)  # PIL'den NumPy dizisine çevir
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # Görüntüyü siyah-beyaza çevir
    return gray_image

# Gradio arayüzünü oluştur
with gr.Blocks() as demo:
    gr.Markdown("Görseli Siyah beyaza çevir!")
    gr.Markdown("Bir resim yükleyin ve siyah beyaza çevrilsin!")

    image_input = gr.Image(type='pil')
    image_output = gr.Image(type="numpy", label="Sonuç Resmi")

    btn= gr.Button("Çevir!")
    btn.click(fn=nostalji,inputs=image_input,outputs=image_output)

    # Fonksiyonu gradio bileşenlerine bağlayalım
    demo = gr.Interface(fn=nostalji, inputs=[image_input], outputs=[image_output])
    demo.launch(share=True)


# Arayüzü başlatma
if __name__ == "__main__":
    demo.launch()
"""