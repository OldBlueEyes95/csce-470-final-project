import subprocess
import sys

# List of required packages
required_packages = [
    'pandas',
    'bs4',
    'nltk',
    'requests'
]

def install(package):
    '''Install a package using pip.'''
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

def ensure_dependencies_installed():
    '''Check and install missing dependencies.'''
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f'{package} not found, installing...')
            install(package)

    # For 'nltk', ensure stopwords are downloaded
    try:
        import nltk
        nltk.data.find('corpora/stopwords.zip')
    except (ImportError, LookupError):
        print('Downloading NLTK stopwords...')
        nltk.download('stopwords')

if __name__ == '__main__':
    ensure_dependencies_installed()
    print('All dependencies are installed and ready to use.')
