### How to get Perturb-OT working (mostly):

At first, I was having a lot of trouble building `perturbot`. First, I needed to replace the `pyproject.toml` file with a `setup.py` file, graciously provided by GH copilot. In order for it to work, also need to add a README.md file to directory. This allowed me to build a non-empty `perturbot` package.

Second, I needed to start a virtual environment in python (either with `venv` or `virtualenv`)
* `source /usr/bin/activate`
* `pip install scvi-tools`, `pip install ott`, `pip install perturbot` should hopefully work (although depending on my setup îstill am getting some dependency related errors).
