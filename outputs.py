import yaml
import json
from tqdm import tqdm
from pathlib import Path

contents_files = Path("data/contents/").glob("*.yaml")
new_files = Path("data/products").glob("*.yaml")

products_contents = {}

for file in contents_files:
	with open(file, "rb") as f:
		data = yaml.safe_load(f)
	for product, contents in data["products"].items():
		if contents:
			if data["code"] not in products_contents:
				products_contents[data["code"]] = {}
			products_contents[data["code"]][product] = contents

with open("outputs/contents.json", "w") as outfile:
	json.dump(products_contents, outfile)

products_new = {}

for file in new_files:
	with open(file, "rb") as f:
		data = yaml.safe_load(f)
	products_new[data["code"]] = data["products"]

with open("outputs/products.json", "w") as outfile:
	json.dump(products_new, outfile)