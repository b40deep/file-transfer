import gradio as gr
import os

def save_file(file):
    if not os.path.exists('incoming'):
        os.makedirs('incoming')
    file_path = file.name
    file_size = os.path.getsize(file_path)
    with open(os.path.join('incoming', os.path.basename(file_path)), "wb") as dest:
        with open(file_path, "rb") as source:
            bytes_copied = 0
            while True:
                # chunk = source.read(8192)  # Read in 8KB chunks
                chunk = source.read(8192000)  # Read in 8MB chunks
                if not chunk:
                    break
                dest.write(chunk)
                bytes_copied += len(chunk)
                progress = int((bytes_copied / file_size) * 100)
                gr.update(value=f"Progress: {progress}%")
                yield f"Progress: {progress}%"
    return "File saved successfully!"

with gr.Blocks() as demo:
    file_input = gr.File(label="Upload File")
    status = gr.Textbox("completion will show here")
    save_button = gr.Button("Save File")
    save_button.click(save_file, inputs=file_input, outputs=status)

demo.launch(share=True)