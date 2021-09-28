import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hugging-gan-test",
    version="0.2.3",
    author="Javi and Vicc",
    author_email="vipermu97@gmail.com",
    description="Testing pip",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/javismiles/HuggingGAN",
    project_urls={
        "Docs": "https://github.com/javismiles/HuggingGAN/docs",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # package_dir={
    #     "": ".",
    #     "taming": "./bigotis/models/taming/modeling_taming",
    # },
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "tqdm==4.60.0",
        "clip_by_openai",
        "dall-e==0.1",
        "imageio-ffmpeg==0.4.3",
        "PyYAML==5.4.1",
        "omegaconf==2.0.6",
        "pytorch-lightning==1.3.3",
        "einops==0.3.0",
        "imageio==2.9.0",
        "torch==1.7.1",
        "torchvision==0.8.2",
        "tensorboard>=2.2.0",
        "transformers>=4.10.0",
        "flax>=0.3.4",
        "jaxlib==0.1.69",
    ],
)