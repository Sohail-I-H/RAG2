import os
import uuid
import tempfile

import edge_tts
import asyncio


# ==========================================================
# CREATE TEMP FILE
# ==========================================================

def save_uploaded_file(uploaded_file):

    extension = os.path.splitext(
        uploaded_file.name
    )[1]

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=extension
    ) as tmp:

        tmp.write(
            uploaded_file.getbuffer()
        )

        return tmp.name


# ==========================================================
# SAVE RECORDED AUDIO
# ==========================================================

def save_audio_bytes(audio_bytes):

    filename = os.path.join(
        tempfile.gettempdir(),
        f"{uuid.uuid4().hex}.wav"
    )

    with open(filename, "wb") as f:

        f.write(audio_bytes)

    return filename


# ==========================================================
# EDGE TTS
# ==========================================================

async def _generate_audio(
    text,
    voice
):

    filename = os.path.join(
        tempfile.gettempdir(),
        f"{uuid.uuid4().hex}.mp3"
    )

    communicate = edge_tts.Communicate(
        text=text,
        voice=voice
    )

    await communicate.save(filename)

    return filename


def text_to_speech(
    text,
    voice
):

    return asyncio.run(

        _generate_audio(

            text,

            voice

        )

    )


# ==========================================================
# CLEANUP TEMP FILE
# ==========================================================

def delete_file(path):

    try:

        if os.path.exists(path):

            os.remove(path)

    except Exception:

        pass
