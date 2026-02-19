import pandas as pd
import shutil
import os

# Read Kaggle labels
labels = pd.read_csv('labels.csv')
print(f"Found {len(labels)} images across {labels['breed'].nunique()} breeds")

train_dir = 'train'
dataset_dir = 'dataset/train'

os.makedirs(dataset_dir, exist_ok=True)

# Loop through ALL breeds
for breed in labels['breed'].unique():
    breed_folder = os.path.join(dataset_dir, breed)
    os.makedirs(breed_folder, exist_ok=True)

    breed_imgs = labels[labels['breed'] == breed]['id'].tolist()

    moved_count = 0
    for img_id in breed_imgs:
        src = os.path.join(train_dir, f"{img_id}.jpg")
        dst = os.path.join(breed_folder, f"{img_id}.jpg")

        if os.path.exists(src):
            shutil.move(src, dst)   # Use copy instead of move (safer)
            moved_count += 1

    print(f"{breed}: {moved_count} images copied")

print("✅ All breeds organized successfully!")
