# csce-470-final-project
Shared final project for CSCE 470.

# Local Setup Guide
To run our program you should have a valid Python 3 installation (Python 3.12 is the version used in testing) and valid up to date Node and NPM installations.

## Frontend Setup
The working directory for the frontend is `frontend/`.

1. Run `npm install` to collect the JS dependencies.
2. Run `npm start` to run the frontend.

## Backend Setup
The working directory for the backend is `frontend/api/`. Our recommendation is first to set up a Python virtual environment using `python -m venv .venv` (run using `.venv/Scripts/activate`).

1. Install Python dependencies using `pip install -r requirements.txt`
2. Run `install_dependencies.py` to ensure nltk data (such as it's stopwords collection) is downloaded.
2. Run `download.py` to download our stable copy of the Minecraft wiki and generate the `data/` folder.
3. Run `python index.py` to convert the wiki XML file into a useable index.
4. Run `flask --app app.py run` to start up the backend.

After this you should be able to run `install_dependencies.py` which should resolve the various Python dependencies so long as pip is also installed. 

# Evaluation
Assuming the setup steps have been done for the backend, you can run `evaluation.py` (currently set to use the quicker test function) in the backend working directory. 
