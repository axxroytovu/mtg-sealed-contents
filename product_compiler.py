import ijson
from tqdm import tqdm
import yaml
from pathlib import Path
import logging

alt_codes = {
	"CON_": "con"
}
logging.basicConfig(filename='product.log', encoding='utf-8', level=logging.INFO)

parentPath = Path("mtgJson/AllSetfiles/")
files = parentPath.glob("*.json")
t = tqdm(files)
codes = set()
for file in t:
	'''
	with open(file, 'rb') as ifile:
		booster_types = ijson.kvitems(ifile, "data.booster")
		types = list(dict(booster_types).keys())
		for t in types:
			print(file, "booster:", t)
	'''
	output_file = Path("data/contents/").joinpath(file.with_suffix(".yaml").name)
	if output_file.is_file():
		with open(output_file, 'r') as f:
			full = yaml.safe_load(f)
		try:
			products = full["products"]
		except:
			products = full
	else:
		products = {}
	with open(file, 'rb') as ifile:
		sealed_product = list(ijson.items(ifile, "data.sealedProduct.item"))
		for p in sealed_product:
			if p["name"] not in products:
				logging.info("Added new product %s/%s", file.stem, p["name"])
				products[p["name"]] = []
	code = alt_codes.get(file.stem.lower(), file.stem.lower())
	with open(output_file, 'w') as write:
		yaml.dump({"code": code, "products": products}, write)
t.close
del(t)


