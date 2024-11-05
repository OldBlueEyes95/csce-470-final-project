# csce-470-final-project
Shared final project for CSCE 470.

# Setup
To run our program you should have a valid Python 3 installation (Python 3.12 is the version used in testing). After this you should be able to run `install_dependencies.py` which should resolve the various Python dependencies so long as pip is also installed. 

# Running the Project
To try the project for yourself, you can use `download.py` to import an XML file of the entire Minecraft Wiki; this file can then be indexed via `index.py` which is saved using in a serialized format. The core algorithm for the search tool itself is `scoring.py` which uses the pickled index to create its search results.
1. `install_dependencies.py`
2. `python download.py`
3. `python index.py`
4. `python simple_searcher.py`

We have some an evaluation module that uses NDCG and MAP to evaluate performance using a set of test queries.
1. `python evaluation.py`

## Project Dependencies

This python3 project has some pip package dependencies. 

- `pandas` - Data manipulation and analysis.
- `bs4` (BeautifulSoup) - HTML and XML parsing.
- `nltk` - Natural language processing.
- `requests` - HTTP requests for web content access.
- `lxml` - XML and HTML parsing with enhanced performance.
- `matplotlib` - Data visualization.

We do have a script that will install these dependencies and more: `install_dependencies.py`. NLTK has some data of its own that must be downloaded, and this script will fetch those as well.
