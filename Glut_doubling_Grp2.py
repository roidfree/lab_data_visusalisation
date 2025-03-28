import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# --------------------------------------------------
# 1) Doubling Time Data
# --------------------------------------------------
doubling_data = {
    # 0.5 mM
    ('0.5mM', 1.85, 'DM'):   1549.263036,
    ('0.5mM', 1.85, 'HeLa'): 239.8144848,
    ('0.5mM', 2.97, 'DM'):   540.4841369,
    ('0.5mM', 2.97, 'HeLa'): -185.542691,
    ('0.5mM', 3.9,  'DM'):   742.3133813,
    ('0.5mM', 3.9,  'HeLa'): -266.9703522,

    # 2 mM
    ('2mM',   1.85, 'DM'):   121.2003418,
    ('2mM',   1.85, 'HeLa'): 93.86930349,
    ('2mM',   2.97, 'DM'):   358.4280968,
    ('2mM',   2.97, 'HeLa'): 281.0222811,
    ('2mM',   3.9,  'DM'):   -963.6045275,
    ('2mM',   3.9,  'HeLa'): 568.5145394,

    # 5 mM
    ('5mM',   1.85, 'DM'):   130.1222582,
    ('5mM',   1.85, 'HeLa'): 128.0393718,
    ('5mM',   2.97, 'DM'):   99.06933043,
    ('5mM',   2.97, 'HeLa'): 64.52061536,
    ('5mM',   3.9,  'DM'):   96.00160962,
    ('5mM',   3.9,  'HeLa'): 75.11328599,

    # 8 mM
    ('8mM',   1.85, 'DM'):   160.8741874,
    ('8mM',   1.85, 'HeLa'): 61.48562087,
    ('8mM',   2.97, 'DM'):   67.90665571,
    ('8mM',   2.97, 'HeLa'): 115.3368893,
    ('8mM',   3.9,  'DM'):   154.51087,
    ('8mM',   3.9,  'HeLa'): 156.74935,
}

# --------------------------------------------------
# 2) Plot Categories
# --------------------------------------------------
nutrient_concs = ['0.5mM', '2mM', '5mM', '8mM']
cell_concs = [3.9, 2.97, 1.85]  # from highest to lowest or vice versa
density_labels = {3.9: "Density-1", 2.97: "Density-2", 1.85: "Density-3"}
cell_types = ['DM', 'HeLa']

# Combine each nutrient × density as a single “group”
groups = [(nc, cc) for nc in nutrient_concs for cc in cell_concs]

# --------------------------------------------------
# 3) Set up the Figure
# --------------------------------------------------
fig, ax = plt.subplots(figsize=(14, 6))

bar_width = 0.15
group_spacing = 0.4

# Colors for DM vs. HeLa
colors = {
    'DM':   '#90EE90',  # Light green
    'HeLa': '#FFA07A',  # Light salmon
}

# --------------------------------------------------
# 4) Plot Bars
# --------------------------------------------------
x_positions = []
labels = []

current_nutrient = None
nutrient_start_pos = 0
concentration_positions = []

for i, (nutrient, cc) in enumerate(groups):
    # Each group has 2 bars (DM, HeLa)
    group_width = len(cell_types) * bar_width
    group_left = i * (group_width + group_spacing)

    # Track the boundaries of each nutrient group for labeling
    if current_nutrient != nutrient:
        if current_nutrient is not None:
            # Mark the center for the previous nutrient group
            center_pos = (nutrient_start_pos + group_left) / 2
            concentration_positions.append((center_pos, current_nutrient))
        current_nutrient = nutrient
        nutrient_start_pos = group_left

    # Plot each cell type
    for bar_index, ct in enumerate(cell_types):
        val = doubling_data[(nutrient, cc, ct)]
        x = group_left + bar_index * bar_width
        ax.bar(x, val, width=bar_width,
               color=colors[ct],
               edgecolor='black', linewidth=0.5)

    # Center position of this group (for x-axis tick label)
    group_center = group_left + group_width / 2 - bar_width / 2
    x_positions.append(group_center)
    labels.append(density_labels[cc])

# Final nutrient group label
if current_nutrient is not None:
    center_pos = (nutrient_start_pos + group_left + group_width) / 2
    concentration_positions.append((center_pos, current_nutrient))

# --------------------------------------------------
# 5) Axes Labels & Title
# --------------------------------------------------
ax.set_title("Glutamine Doubling Times: 0.5, 2, 5, 8 mM (DM vs. HeLa)", fontsize=14)
ax.set_xlabel("Cell Seeding Density", fontsize=12)
ax.set_ylabel("Doubling Time (hrs)", fontsize=12)

# Position the x-axis ticks in the center of each group
ax.set_xticks(x_positions)
ax.set_xticklabels(labels, fontsize=8)

# --------------------------------------------------
# 6) Top Labels for Each Nutrient Concentration
# --------------------------------------------------
# Place them at 90% of the current maximum Y-limit
max_y = ax.get_ylim()[1] * 0.9

# Find the “start” and “end” boundary for each nutrient group
concentration_centers = {}
for i in range(len(groups) - 1):
    if groups[i][0] != groups[i + 1][0]:
        boundary = (x_positions[i] + x_positions[i + 1]) / 2
        # End of the current group
        if groups[i][0] not in concentration_centers:
            concentration_centers[groups[i][0]] = {'start': None, 'end': None}
        concentration_centers[groups[i][0]]['end'] = boundary
        # Start of the next group
        if groups[i + 1][0] not in concentration_centers:
            concentration_centers[groups[i + 1][0]] = {'start': None, 'end': None}
        concentration_centers[groups[i + 1][0]]['start'] = boundary

first_nutrient = groups[0][0]
last_nutrient = groups[-1][0]
if first_nutrient not in concentration_centers:
    concentration_centers[first_nutrient] = {'start': None, 'end': None}
if concentration_centers[first_nutrient]['start'] is None:
    # Left edge of the first group
    concentration_centers[first_nutrient]['start'] = x_positions[0] - (len(cell_types) * bar_width) / 2

if last_nutrient not in concentration_centers:
    concentration_centers[last_nutrient] = {'start': None, 'end': None}
if concentration_centers[last_nutrient]['end'] is None:
    # Right edge of the last group
    concentration_centers[last_nutrient]['end'] = x_positions[-1] + (len(cell_types) * bar_width) / 2

# Add text boxes for each nutrient concentration
for nutrient, positions in concentration_centers.items():
    center = (positions['start'] + positions['end']) / 2
    ax.text(center, max_y, nutrient, ha='center', va='center',
            fontweight='bold', fontsize=12,
            bbox=dict(facecolor='white', alpha=0.8,
                      edgecolor='black', boxstyle='round,pad=0.4'))

# --------------------------------------------------
# 7) Density Key
# --------------------------------------------------
density_key = (
    "Density Key:\n"
    "Density-1: 3.90×10⁴\n"
    "Density-2: 2.97×10⁴\n"
    "Density-3: 1.85×10⁴"
)
ax.text(0.87, 0.9, density_key, ha='left', va='top', fontsize=9, transform=ax.transAxes,
        bbox=dict(facecolor='white', alpha=0.8, edgecolor='black', boxstyle='round,pad=0.5'))

# --------------------------------------------------
# 8) Legend (DM vs. HeLa)
# --------------------------------------------------
legend_handles = []
for ct in cell_types:
    patch = mpatches.Patch(color=colors[ct],
                           label=ct,
                           edgecolor='black', linewidth=0.5)
    legend_handles.append(patch)

ax.legend(handles=legend_handles, loc='upper left', ncol=1, bbox_to_anchor=(0, 1.15))

# --------------------------------------------------
# 9) Vertical Lines Between Nutrient Groups
# --------------------------------------------------
for i in range(len(groups) - 1):
    if groups[i][0] != groups[i + 1][0]:
        x_line = (x_positions[i] + x_positions[i + 1]) / 2
        ax.axvline(x_line, color='black', linestyle='--', alpha=0.8)

# --------------------------------------------------
# 10) Grid & Layout
# --------------------------------------------------
ax.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('Glut_doubling_Grp2.png', dpi=300, bbox_inches='tight')
plt.show()
