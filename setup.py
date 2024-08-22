from setuptools import setup

setup(
    name="BBAudioTranscriber",
    version="0.1",
    description="Audio Transcriber using whisper-medium. Local deployment.",
    url="xxxmaskedxxx",
    author="blackbird",
    author_email="jicong.ao@tum.de",
    license="MIT",
    packages=["BBAudioTranscriber"],
    install_requires=[
        "numpy<2",
        "scipy",
        # "fastapi[standard]",
        # "transformers",
        "sounddevice",
        "pydub",
        "pynput",
    ],
    # duplicated in requirements.txt
    zip_safe=False,
)
