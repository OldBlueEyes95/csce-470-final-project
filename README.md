# csce-470-final-project
Shared final project for CSCE 470.

# Setup
To run our program you should have a valid Python 3 installation (Python 3.12 is the version used in testing). After this you should be able to run `install_dependencies.py` which will resolve the various Python dependencies.

# Running the Project
To try the project for yourself, you can use `download.py` to import an XML file of the entire Minecraft Wiki; this file can then be indexed via `index.py` which is saved using Pickle. The core algorithm for the search tool itself is `query_crafter.py` which uses the pickled index to create its search results.