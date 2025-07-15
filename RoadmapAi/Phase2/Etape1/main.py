

"""if __name__ == '__main__':
    from fastai.vision.all import *
    from matplotlib import pyplot as plt


    path = untar_data(URLs.PETS)/'images'


    def is_cat(x): return x[0].isupper()

    dls = ImageDataLoaders.from_name_func(
        path, get_image_files(path), valid_pct=0.2, seed=42,
        label_func=is_cat, item_tfms=Resize(224), num_workers=0
    )

    learn = vision_learner(dls, resnet34, metrics=error_rate)
    learn.fine_tune(1)

    upload ="C:\\Users\\Superuser\\PycharmProjects\\RoadmapAi\\Phase2\\Etape1\\humainface.jpg"
    img= PILImage.create(upload)
    is_cat,_,probs= learn.predict(img)
    print("Est-ce un chat? (is_cat).")

    print(f'probabiliter que ce soit un chat : {probs[1].item():.6f}')

    plt.imshow(img)
    plt.axis('off')
    plt.title(f"Prediction: {is_cat} ({probs[1].item():.2%} chat)")
    plt.show()
"""

from PIL import Image, UnidentifiedImageError
import os

# Remplace ce chemin par le tien !
ROOT_DIR = r"C:\Users\Superuser\PycharmProjects\RoadmapAi\Phase2\Etape2\ours"

# Extensions acceptées (tu peux ajouter 'jpeg', 'png' si besoin)
valid_exts = ['.jpg', '.jpeg', '.png']

def convert_to_jpeg(src_path):
    try:
        img = Image.open(src_path)
        img = img.convert("RGB")
        # Ecrase l'image avec la version JPEG
        img.save(src_path, "JPEG")
        print(f"Converti : {src_path}")
        return True
    except UnidentifiedImageError:
        print(f"Image corrompue ou format non supporté : {src_path}")
        return False
    except Exception as e:
        print(f"Erreur inconnue ({src_path}) : {e}")
        return False

nb_checked = 0
nb_deleted = 0
nb_converted = 0

for root, dirs, files in os.walk(ROOT_DIR):
    for file in files:
        path = os.path.join(root, file)
        ext = os.path.splitext(file)[1].lower()
        nb_checked += 1
        # Si ce n'est pas une image d'extension attendue, supprime ou ignore
        if ext not in valid_exts:
            print(f"Suppression (extension non reconnue) : {path}")
            os.remove(path)
            nb_deleted += 1
            continue
        # Essaie d'ouvrir et de convertir l'image
        if convert_to_jpeg(path):
            nb_converted += 1
        else:
            print(f"Suppression (illisible/corrompu) : {path}")
            os.remove(path)
            nb_deleted += 1

print(f"\nBilan :\n{nb_checked} fichiers vérifiés.")
print(f"{nb_converted} images converties ou validées.")
print(f"{nb_deleted} fichiers supprimés (non-images ou corrompus).")




















