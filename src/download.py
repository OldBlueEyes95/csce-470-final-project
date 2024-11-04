import requests
import os

output_dir = 'data'
filename = 'pages_export.xml'
api_url = "https://minecraft.wiki/api.php"
export_url = "https://minecraft.wiki/w/Special:Export"

def download_pages() -> None:
    # GET the pages and their titles.
    categories = [
        'Trading', 'Brewing', 'Enchanting', 'Mobs', 'Blocks', 'Items', 'Biomes', 'Effects', 
        'Crafting', 'Smelting', 'Smithing', 'Structures', 'Redstone', 'Archaeology', 'History', 'Tutorials'
    ]
    
    titles = []
    for category in categories:
        params = {
            "action": "query",
            "list": "categorymembers",
            "cmtitle": f"Category:{category}",
            "cmlimit": "max",
            "format": "json"
        }
        response = requests.get(api_url, params=params)
        if response.status_code == 200 and response.text.strip():
            try:
                data = response.json()
            except ValueError:
                print("Error: Response is not JSON.")
                print(response.text)  # Print the response to debug
                return
        else:
            print(f"Failed to fetch data for category {category}. Status code: {response.status_code}")
            return
        pages = data['query']['categorymembers']
        titles.extend([page['title'] for page in pages])
    
    # Export all the pages
    response = requests.post(export_url, data={
        "pages": "\n".join(titles),
        "curonly": 1  # Only current version
    })
    
    # Save response
    if response.status_code == 200:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        with open(f"{output_dir}/{filename}", "wb") as f:
            f.write(response.content)
        print(f"Downloaded to {output_dir}/{filename}")
    else:
        print(f"Download request failed: {response.status_code}")


if __name__ == "__main__":
    download_pages()