import requests
import os

output_dir = 'data'
filename = 'pages_export.xml'
api_url = "https://minecraft.wiki/api.php"
export_url = "https://minecraft.wiki/w/Special:Export"

def download_pages() -> None:
    # GET the pages and their titles.
    categories = [
        'Category:Enchantments',
        'Category:Mobs',
        'Category:Neutral_mobs',
        'Category:Passive_mobs',
        'Category:Hostile_mobs',
        'Category:Removed_mobs',
        'Category:Unused_mobs',
        'Category:Planned_mobs',
        'Category:Boss_mobs',
        'Category:Tameable_mobs',
        'Category:Nether_mobs',
        'Category:End_mobs',
        'Category:Illagers',
        'Category:Animal_mobs',
        'Category:Undead_mobs',
        'Category:Flying_mobs',
        'Category:Aquatic_mobs',
        'Category:Arthropod_mobs',
        'Category:Monster_mobs',
        'Category:Joke_mobs',
        'Category:Jockeys',
        'Category:Humanoid_mobs',
        'Category:Minecraft_Education_mobs',
        'Category:Piglins',
        'Category:Defensive_mobs',
        'Category:Blocks',
        'Category:Ore',
        'Category:Fluids',
        'Category:Manufactured_blocks',
        'Category:Mechanisms',
        'Category:Natural_blocks',
        'Category:Nether_blocks',
        'Category:Removed_blocks',
        'Category:Utility_blocks',
        'Category:Non-solid_blocks',
        'Category:Block_entities',
        'Category:End_blocks',
        'Category:Generated_structure_blocks',
        'Category:Compacted_blocks',
        'Category:Animal_blocks',
        'Category:Flammable_blocks',
        'Category:Joke_blocks',
        'Category:Minecraft_Education_blocks',
        'Category:Climbable_blocks',
        'Category:Light_sources',
        'Category:MinecraftEdu_blocks',
        'Category:Creative_or_commands_only_blocks',
        'Category:Chiseled_bookshelf_states',
        'Category:Blocks_with_GUI',
        'Category:Createable_blocks',
        'Category:Readable_by_comparators',
        'Category:Hazardous_blocks',
        'Category:Falling_blocks',
        'Category:Items',
        'Category:Planned_items',
        'Category:Dyes',
        'Category:Combat',
        'Category:Joke_items',
        'Category:Minecraft_Education_items',
        'Category:Invalid_data_value_items',
        'Category:Smithing_templates',
        'Category:Utilities',
        'Category:Pottery_sherds',
        'Category:Biomes',
        'Category:Biome_screenshots',
        'Category:Nether_biomes',
        'Category:End_biomes',
        'Category:Effects',
        'Category:Structures',
        'Category:Generated_structures',
        'Category:Terrain_features',
        'Category:Structure_subpages',
        'Category:Player-built_structures',
        'Category:Generated_features',
        'Category:World_features',
        'Category:Redstone',
        'Category:Redstone_mechanics',
        'Category:History',
        'Category:Asset_history_pages',
        'Category:Easter_eggs',
        'Category:Online_content',
        'Category:Historical_screenshots',
        'Category:Structure_Blueprints',
        'Category:Piglin_characters',
        'Category:Minecraft_Legends_piglins',
        'Category:Minecraft_Dungeons_piglins',
        'Category:Slabs',
        'Category:Stairs',
        'Category:Walls',
        'Category:Job_blocks',
        'Category:Tools',
        'Category:Armor',
        'Category:Music_discs',
        'Category:Minecraft_Legends_structures',
        'Category:Redstone_circuits',
        'Category:Animated_content',
        'Category:Game_trailers',
        'Category:Redstone_circuits/Clock',
        'Category:Redstone_circuits/Logic',
        'Category:Redstone_circuits/Memory',
        'Category:Redstone_circuits/Piston',
        'Category:Redstone_circuits/Pulse',
        'Category:Village_blueprints',
        'Category:Minecraft_Legends_Hordes',
        'Category:Minecraft_Legends_runts',
        'Category:Minecraft_Legends_clanger',
        'Category:Minecraft_Legends_obstacles',
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