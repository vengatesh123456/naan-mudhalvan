import numpy as np
import matplotlib.pyplot as plt

# Simulate random urban building footprint locations
np.random.seed(42)
points = np.random.rand(500, 2)

# Plot the points
plt.figure(figsize=(6, 6))
plt.scatter(points[:, 0], points[:, 1], s=10)
plt.title('Simulated Urban Building Locations')
plt.xlabel('Normalized X Coordinate')
plt.ylabel('Normalized Y Coordinate')
plt.axis('equal')

# Save as PNG
output_path = '/mnt/data/urban_building_locations.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')

# Convert to JPEG
from PIL import Image
img = Image.open(output_path)
rgb_img = img.convert('RGB')
rgb_img.save('/mnt/data/urban_building_locations.jpg', 'JPEG', quality=95)
