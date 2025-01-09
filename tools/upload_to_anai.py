def upload_to_anai(file):
    import os
    import uuid
    import shutil

    origin_path = file.name
    file_extension = os.path.splitext(file.name)[1]
    upload_path = os.path.join(
        os.getcwd(), "temp_audio", f"{uuid.uuid4()}{file_extension}"
    )

    if not os.path.exists(upload_path):
        os.makedirs(upload_path, exist_ok=True)

    shutil.copy(origin_path, upload_path)

    return upload_path
