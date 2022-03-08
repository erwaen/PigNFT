import random
import data as my_data
from PIL import Image
import json
import os
from os.path import abspath






def create_new_image_obj():
    new_image = {}

    for trait, values in my_data.images.items():
        probability_key_trait = [] # To save all probability of the items by one trait

        for item in values:
            probability_item = item["rank"]["probability"]
            probability_key_trait.append(probability_item)
       
        new_image[trait] = random.choices(values, probability_key_trait)[0] # Ej new_image["Mouth"] = {name: dsdasd, file_name: dsmkads}

    # Now we have fully charge the new_image object

    # the recursive function call is on the occasion that the image was created a repeated
    if new_image in all_images:
        return create_new_image_obj()
    else:
        return new_image

def put_ids_to_all_images():
    i = 0
    for image in all_images:
        image["tokenId"] = i
        i = i + 1

def generate_image(image_obj):

    # Creates the first layer that will replace with the same too
    first_type = my_data.order[0]
    file_name = f'./images/{first_type}/{image_obj[first_type]["file_name"]}.png'
    combined_image = Image.open(file_name).convert('RGBA')


    # We traverse in the order of the layers decided in my_data.order
    current_image = None
    for trait in my_data.order:
        file_name = f'./images/{trait}/{image_obj[trait]["file_name"]}.png'
        current_image = Image.open(file_name).convert('RGBA')
        combined_image = Image.alpha_composite(combined_image, current_image)

    # Convert to RGB
    rgb_im = combined_image.convert('RGB')
    file_name = str(image_obj["tokenId"]) + ".png"
    path_result = "./result"

    total_file_path = f"{path_result}" + "/" + file_name
     
    # Create a new directory because it does not exist 
    if not os.path.exists(path_result):
        os.makedirs(path_result)
    
    rgb_im.save(total_file_path)
    generate_metadata_of_image(image_obj, total_file_path)


def generate_metadata_of_image(image_obj, file_path):
    full_path = abspath( file_path)
  
    
    metadata_of_img = {}
    metadata_of_img["file_path"] = full_path
    metadata_of_img["nft_name"] = "PIG #"+str(image_obj["tokenId"])
    metadata_of_img["description"] = "Hope you like mud!" 
    metadata_of_img["properties"] = []
    price = 0
    for key_property in image_obj:
        if key_property != "tokenId":
            property = key_property
            value_property = image_obj[property]["name"]
            a_property = {
                "type": property,
                "value": value_property
            }
            price += image_obj[key_property]["rank"]["price"]
            metadata_of_img["properties"].append(a_property)
    
    metadata_of_img["price"] = str(price)

    for key, val in metadata_of_img.items():
        print(key,": ", val)

    metadata["nft"].append(metadata_of_img)

 
def generate_metadata_json():

    if not os.path.exists("./metadata"):
        os.makedirs("./metadata")
    with open("./metadata/" + "_metadata" ".json", "w") as outfile:
        json.dump(metadata, outfile, indent=4)
    
    

    



def main():
    TOTAL_IMAGES =  int(input("How many images do you want generate? "))

    # TODO a for loop len of TOTAL_IMAGES
    for i in range(0, TOTAL_IMAGES):
        new_trait_image = create_new_image_obj()
        all_images.append(new_trait_image)

    put_ids_to_all_images()

    
    for image in all_images:
        print("imagen es:" , image)
        generate_image(image)

    generate_metadata_json()
        


all_images = []
metadata = {"nft": []}
main()
