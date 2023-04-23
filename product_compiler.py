
import ijson
from tqdm import tqdm
import yaml
from pathlib import Path

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
		with open(output_file, 'r') as file:
			products = yaml.safe_load(file)
	else:
		products = {}
	with open(file, 'rb') as ifile:
		sealed_product = list(ijson.items(ifile, "data.sealedProduct.item"))
		for p in sealed_product:
			if p["name"] not in products:
				products[p["name"]] = []
	with open(output_file, 'w') as write:
		yaml.dump(products, write)
t.close
del(t)


