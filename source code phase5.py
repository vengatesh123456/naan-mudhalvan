import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Load India states shapefile
india = gpd.read_file("india_states.shp")

# Example urban planning datasets
datasets = {
    'Urban Population Density (2023)': {
        'state': ['Delhi', 'Maharashtra', 'Tamil Nadu', 'West Bengal', 'Karnataka'],
        'value': [1320, 3650, 5550, 10500, 4400]  # people per sq.km
    },
    'Green Space Ratio (2023)': {
        'state': ['Delhi', 'Maharashtra', 'Tamil Nadu', 'West Bengal', 'Karnataka'],
        'value': [12, 18, 20, 15, 22]  # percentage
    },
    'Public Transport Coverage (2023)': {
        'state': ['Delhi', 'Maharashtra', 'Tamil Nadu', 'West Bengal', 'Karnataka'],
        'value': [85, 70, 65, 75, 68]  # percentage of urban area served
    }
}

# Create multipage PDF
with PdfPages("urban_planning_report.pdf") as pdf:
    for title, data in datasets.items():
        df = pd.DataFrame(data)
        merged = india.merge(df, left_on='st_nm', right_on='state', how='left')
        merged['value'] = merged['value'].fillna(0)

        # Plot
        fig, ax = plt.subplots(figsize=(10, 10))
        merged.plot(column='value', cmap='viridis', linewidth=0.8, edgecolor='black',
                    legend=True, legend_kwds={'label': title}, ax=ax)
        plt.title(f"{title} by State", fontsize=14)
        plt.axis('off')
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
