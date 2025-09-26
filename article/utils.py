import os
import uuid


def article_image_path(instance, filename: str) -> str:
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    return os.path.join(f"article/{instance.id}/", filename)
