import os
import glob
from PIL import Image

def optimize_images():
    image_dir = 'images'
    # Find all jpg/png files larger than 1MB
    large_files = []
    for ext in ('*.jpg', '*.JPG', '*.png', '*.PNG'):
        for path in glob.glob(os.path.join(image_dir, '**', ext), recursive=True):
            if os.path.getsize(path) > 1024 * 1024: # > 1MB
                large_files.append(path)
                
    print(f"Found {len(large_files)} large images.")
    for path in large_files:
        print(f"Optimizing {path}...")
        img = Image.open(path)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        webp_path = os.path.splitext(path)[0] + '.webp'
        
        # Save as webp
        img.save(webp_path, 'WEBP', quality=80)
        
        print(f"Saved {webp_path}")

if __name__ == '__main__':
    optimize_images()
