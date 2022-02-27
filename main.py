import random
import data as my_data

def create_new_image():
    new_image = {}

    for key in my_data.images:
        probability_key_trait = []
        for item in my_data.images[key]:
            print(item, "\n")
        # new_image[key] = random.choice()

def main():
    create_new_image()

main()
