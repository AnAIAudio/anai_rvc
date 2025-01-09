def upload_to_anai(file):
    import os
    import uuid
    import shutil
    import gradio as gr

    upload_path = ""
    for index, item in enumerate(file):
        file_extension = os.path.splitext(item)[1]
        upload_path = os.path.join(
            os.getcwd(), "temp_audio", f"{uuid.uuid4()}{file_extension}"
        )

        if not os.path.exists(upload_path):
            os.makedirs(upload_path, exist_ok=True)

        shutil.copy(file, upload_path)
    # gr.Info("File Uploaded!!!")

    return upload_path
