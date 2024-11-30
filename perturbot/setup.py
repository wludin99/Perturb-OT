from setuptools import setup, find_packages

setup(
    name="perturbot",
    version="0.0.1",
    author="Jayoung Ryu",
    author_email="jayoung_ryu@g.harvard.edu",
    description="OT for aligning multimodal perturbation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Genentech/Perturb-OT",
    packages=find_packages(include=["perturbot*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "scanpy>=1.6",
        "POT>=0.9",
        "lightning",
        "ott-jax==0.4.6a",
        "scvi-tools==1.1.0a"
    ],
    project_urls={
        "Homepage": "https://github.com/Genentech/Perturb-OT",
        "Issues": "https://github.com/Genentech/Perturb-OT/issues",
    },
)