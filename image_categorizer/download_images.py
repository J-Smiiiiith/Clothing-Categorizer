from simple_image_download import simple_image_download as sim

response = sim.simple_image_download

search_terms = ["mens casual outfits", "mens formal outfits"]
# Terms to search for images

for term in search_terms:
    response().download(term, 500)