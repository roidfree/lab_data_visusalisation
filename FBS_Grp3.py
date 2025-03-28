import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------------------
# 1) Data Setup
# --------------------------------------------------
stiffness_labels = ['Stiff (15:1)', 'Soft (40:1)']
densities = ['Density 1', 'Density 2', 'Density 3']
cell_types = ['DM', 'HeLa']

groups = [(stiff, dens) for stiff in stiffness_labels for dens in densities]
x = np.arange(len(groups))
bar_width = 0.35

dm_counts =  [0, 0, 0, 0, 0, 0]
hela_counts = [34, 15.3, 14.3, 0, 0, 0]

# --------------------------------------------------
# 2) Color Scheme from Template
# --------------------------------------------------
colors = {
    'DM': '#87CEFA',    # Light sky blue
    'HeLa': '#FFA07A',  # Light salmon
}

# --------------------------------------------------
# 3) Plotting
# --------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(x - bar_width/2, dm_counts, width=bar_width, label='DM', color=colors['DM'])
ax.bar(x + bar_width/2, hela_counts, width=bar_width, label='HeLa', color=colors['HeLa'])

# --------------------------------------------------
# 4) Axis Styling
# --------------------------------------------------
density_labels_for_xticks = [dens for (_, dens) in groups]
ax.set_xticks(x)
ax.set_xticklabels(density_labels_for_xticks, fontsize=10)

ax.set_ylabel('Cell Count', fontsize=12)
ax.set_title('Cell count for DM and HeLa cells in FBS on two substrate stiffnesses', fontsize=14)

# Vertical divider between stiffness groups
ax.axvline(x=2.5, color='black', linestyle='--', alpha=0.6)

# Add legend
ax.legend(title='Cell Type')
ax.grid(axis='y', linestyle='--', alpha=0.4)

# --------------------------------------------------
# 5) Add Stiffness Labels on Top
# --------------------------------------------------
max_y = ax.get_ylim()[1] * 0.9

stiffness_groups = {}
for i, (stiff, _) in enumerate(groups):
    if stiff not in stiffness_groups:
        stiffness_groups[stiff] = []
    stiffness_groups[stiff].append(i)

for stiff, indices in stiffness_groups.items():
    start = x[indices[0]] - bar_width/2
    end = x[indices[-1]] + bar_width/2
    center = (start + end) / 2
    ax.text(center, max_y, stiff, ha='center', va='center', fontweight='bold', fontsize=12,
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='black', boxstyle='round,pad=0.4'))

# --------------------------------------------------
# 6) Add Density Key (Top-right corner)
# --------------------------------------------------
density_key = "Density Key:\nDensity 1: 3.90×10⁴\nDensity 2: 2.97×10⁴\nDensity 3: 1.85×10⁴"
ax.text(0.87, 0.8, density_key, ha='left', va='top', fontsize=9, transform=ax.transAxes,
        bbox=dict(facecolor='white', alpha=0.8, edgecolor='black', boxstyle='round,pad=0.5'))

plt.tight_layout()
plt.show()
