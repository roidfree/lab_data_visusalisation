import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# --------------------------------------------------
# 1) Glucose absorbance data + SEM
# --------------------------------------------------
absorbance_data = {
    # 2.5 mM
    ('2.5mM', 3.9,  'DM'):   {'0h': 0.259333333, '48h': 0.237},
    ('2.5mM', 3.9,  'HeLa'): {'0h': 0.173,       '48h': 0.402},

    ('2.5mM', 2.97, 'DM'):   {'0h': 0.251,       '48h': 0.237333333},
    ('2.5mM', 2.97, 'HeLa'): {'0h': 0.135,       '48h': 0.400666667},

    ('2.5mM', 1.85, 'DM'):   {'0h': 0.218333333, '48h': 0.214},
    ('2.5mM', 1.85, 'HeLa'): {'0h': 0.138666667, '48h': 0.347666667},

    # 5 mM
    ('5mM',   3.9,  'DM'):   {'0h': 0.232333333, '48h': 0.401333333},
    ('5mM',   3.9,  'HeLa'): {'0h': 0.158333333, '48h': 0.588},

    ('5mM',   2.97, 'DM'):   {'0h': 0.211,       '48h': 0.290333333},
    ('5mM',   2.97, 'HeLa'): {'0h': 0.134666667, '48h': 0.417666667},

    ('5mM',   1.85, 'DM'):   {'0h': 0.193666667, '48h': 0.402},
    ('5mM',   1.85, 'HeLa'): {'0h': 0.136,       '48h': 0.503666667},

    # 15 mM
    ('15mM',  3.9,  'DM'):   {'0h': 0.194,       '48h': 0.144666667},
    ('15mM',  3.9,  'HeLa'): {'0h': 0.197666667, '48h': 0.451666667},

    ('15mM',  2.97, 'DM'):   {'0h': 0.153,       '48h': 0.138666667},
    ('15mM',  2.97, 'HeLa'): {'0h': 0.155,       '48h': 0.370666667},

    ('15mM',  1.85, 'DM'):   {'0h': 0.160666667, '48h': 0.127666667},
    ('15mM',  1.85, 'HeLa'): {'0h': 0.152,       '48h': 0.350333333},

    # 25 mM
    ('25mM',  3.9,  'DM'):   {'0h': 0.174333333, '48h': 0.196333333},
    ('25mM',  3.9,  'HeLa'): {'0h': 0.17,        '48h': 0.503},

    ('25mM',  2.97, 'DM'):   {'0h': 0.201,       '48h': 0.146},
    ('25mM',  2.97, 'HeLa'): {'0h': 0.143,       '48h': 0.47},

    ('25mM',  1.85, 'DM'):   {'0h': 0.158666667, '48h': 0.132666667},
    ('25mM',  1.85, 'HeLa'): {'0h': 0.138333333, '48h': 0.348666667},
}

sem_data = {
    # 2.5 mM
    ('2.5mM', 3.9,  'DM'):   {'0h': 0.00851143,  '48h': 0.003},
    ('2.5mM', 3.9,  'HeLa'): {'0h': 0.015567059, '48h': 0.022007574},

    ('2.5mM', 2.97, 'DM'):   {'0h': 0.011676187, '48h': 0.006064468},
    ('2.5mM', 2.97, 'HeLa'): {'0h': 0.004041452, '48h': 0.063399089},

    ('2.5mM', 1.85, 'DM'):   {'0h': 0.004630815, '48h': 0.008},
    ('2.5mM', 1.85, 'HeLa'): {'0h': 0.010170764, '48h': 0.032271418},

    # 5 mM
    ('5mM',   3.9,  'DM'):   {'0h': 0.009333333, '48h': 0.026187359},
    ('5mM',   3.9,  'HeLa'): {'0h': 0.010806377, '48h': 0.11561286},

    ('5mM',   2.97, 'DM'):   {'0h': 0.005507571, '48h': 0.019427929},
    ('5mM',   2.97, 'HeLa'): {'0h': 0.000881917, '48h': 0.099683388},

    ('5mM',   1.85, 'DM'):   {'0h': 0.000881917, '48h': 0.059651767},
    ('5mM',   1.85, 'HeLa'): {'0h': 0.006244998, '48h': 0.063891401},

    # 15 mM
    ('15mM',  3.9,  'DM'):   {'0h': 0.008621678, '48h': 0.004484541},
    ('15mM',  3.9,  'HeLa'): {'0h': 0.016374099, '48h': 0.045285514},

    ('15mM',  2.97, 'DM'):   {'0h': 0.004358899, '48h': 0.003179797},
    ('15mM',  2.97, 'HeLa'): {'0h': 0.020297783, '48h': 0.02073912},

    ('15mM',  1.85, 'DM'):   {'0h': 0.001763834, '48h': 0.000333333},
    ('15mM',  1.85, 'HeLa'): {'0h': 0.007505553, '48h': 0.040960686},

    # 25 mM
    ('25mM',  3.9,  'DM'):   {'0h': 0.002027588, '48h': 0.002333333},
    ('25mM',  3.9,  'HeLa'): {'0h': 0.024131584, '48h': 0.029143324},

    ('25mM',  2.97, 'DM'):   {'0h': 0.04350862,  '48h': 0.005859465},
    ('25mM',  2.97, 'HeLa'): {'0h': 0.020132892, '48h': 0.054775299},

    ('25mM',  1.85, 'DM'):   {'0h': 0.014402932, '48h': 0.002666667},
    ('25mM',  1.85, 'HeLa'): {'0h': 0.004977728, '48h': 0.020537229},
}

# --------------------------------------------------
# 2) Plot categories
# --------------------------------------------------
nutrient_concs = ['2.5mM', '5mM', '15mM', '25mM']
cell_concs = [3.9, 2.97, 1.85]
density_labels = {3.9: "Density-1", 2.97: "Density-2", 1.85: "Density-3"}
cell_types = ['DM', 'HeLa']
time_points = ['0h', '48h']
groups = [(nc, cc) for nc in nutrient_concs for cc in cell_concs]

# --------------------------------------------------
# 3) Set up figure
# --------------------------------------------------
fig, ax = plt.subplots(figsize=(14, 6))
bar_width = 0.1
group_spacing = 0.4

colors = {
    ('DM','0h'):    '#87CEFA',  # Light sky blue
    ('DM','48h'):   '#0000CD',  # Medium blue
    ('HeLa','0h'):  '#FFA07A',  # Light salmon
    ('HeLa','48h'): '#B22222',  # Firebrick
}

# --------------------------------------------------
# 4) Plot with error bars
# --------------------------------------------------
x_positions = []
labels = []
concentration_positions = []  # Track positions for concentration labels

current_nutrient = None
nutrient_start_pos = 0

for i, (nutrient, cc) in enumerate(groups):
    group_width = len(cell_types) * len(time_points) * bar_width
    group_left = i * (group_width + group_spacing)
    
    # Track concentration group boundaries
    if current_nutrient != nutrient:
        if current_nutrient is not None:
            # Calculate center position for the previous concentration group
            center_pos = (nutrient_start_pos + group_left) / 2
            concentration_positions.append((center_pos, current_nutrient))
        
        current_nutrient = nutrient
        nutrient_start_pos = group_left
    
    bar_index = 0
    for ct in cell_types:
        for tp in time_points:
            val = absorbance_data[(nutrient, cc, ct)][tp]
            err = sem_data[(nutrient, cc, ct)][tp]
            
            x = group_left + bar_index * bar_width
            ax.bar(x, val, width=bar_width,
                   color=colors[(ct, tp)],
                   edgecolor='black', linewidth=0.5,
                   yerr=err, capsize=3)
            bar_index += 1
    
    group_center = group_left + group_width / 2 - bar_width / 2
    x_positions.append(group_center)
    labels.append(f"{density_labels[cc]}")  # Use density label instead of cell concentration

# Add the last concentration group
if current_nutrient is not None:
    center_pos = (nutrient_start_pos + group_left + group_width) / 2
    concentration_positions.append((center_pos, current_nutrient))

ax.set_title("Glucose: 2.5, 5, 15, 25 mM (0h vs. 48h, DM vs. HeLa)", fontsize=14)
ax.set_xlabel("Cell Seeding Density", fontsize=12)
ax.set_ylabel("Absorbance", fontsize=12)

ax.set_xticks(x_positions)
ax.set_xticklabels(labels, fontsize=8)  # Smaller but still legible font size

# Add concentration labels at the top of each group
max_y = ax.get_ylim()[1] * 0.9  # Position at 90% of the y-axis height

# Calculate the center position for each concentration group
concentration_centers = {}
for i in range(len(groups) - 1):
    if groups[i][0] != groups[i + 1][0]:
        # This is a boundary between concentration groups
        boundary = (x_positions[i] + x_positions[i + 1]) / 2
        
        # Find the center of the current group
        if groups[i][0] not in concentration_centers:
            concentration_centers[groups[i][0]] = {'start': None, 'end': None}
        concentration_centers[groups[i][0]]['end'] = boundary
        
        # Find the center of the next group
        if groups[i+1][0] not in concentration_centers:
            concentration_centers[groups[i+1][0]] = {'start': None, 'end': None}
        concentration_centers[groups[i+1][0]]['start'] = boundary

# Set the start of the first group and end of the last group
first_nutrient = groups[0][0]
last_nutrient = groups[-1][0]
if first_nutrient not in concentration_centers:
    concentration_centers[first_nutrient] = {'start': None, 'end': None}
if concentration_centers[first_nutrient]['start'] is None:
    # Get position of first bar
    concentration_centers[first_nutrient]['start'] = x_positions[0] - (len(cell_types) * len(time_points) * bar_width) / 2

if last_nutrient not in concentration_centers:
    concentration_centers[last_nutrient] = {'start': None, 'end': None}
if concentration_centers[last_nutrient]['end'] is None:
    # Get position of last bar
    concentration_centers[last_nutrient]['end'] = x_positions[-1] + (len(cell_types) * len(time_points) * bar_width) / 2

# Add the labels at the center of each group
for nutrient, positions in concentration_centers.items():
    center = (positions['start'] + positions['end']) / 2
    ax.text(center, max_y, nutrient, ha='center', va='center', 
            fontweight='bold', fontsize=12, 
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='black', boxstyle='round,pad=0.4'))

# Add a key for density labels
density_key = "Density Key:\nDensity-1: 3.90×10⁴\nDensity-2: 2.97×10⁴\nDensity-3: 1.85×10⁴"
# Position within the chart (moved more to the left, same height)
ax.text(0.87, 0.95, density_key, ha='left', va='top', fontsize=9, transform=ax.transAxes,
       bbox=dict(facecolor='white', alpha=0.8, edgecolor='black', boxstyle='round,pad=0.5'))

# Build legend
legend_handles = []
for ct in cell_types:
    for tp in time_points:
        patch = mpatches.Patch(color=colors[(ct, tp)],
                               label=f"{ct} {tp}",
                               edgecolor='black', linewidth=0.5)
        legend_handles.append(patch)

seen = set()
unique_handles = []
for h in legend_handles:
    if h.get_label() not in seen:
        unique_handles.append(h)
        seen.add(h.get_label())

ax.legend(handles=unique_handles, loc='upper left', ncol=2, bbox_to_anchor=(0, 1.15))

for i in range(len(groups) - 1):
    if groups[i][0] != groups[i + 1][0]:
        x_line = (x_positions[i] + x_positions[i + 1]) / 2
        ax.axvline(x_line, color='black', linestyle='--', alpha=0.8)

ax.grid(axis='y', linestyle='--', alpha=0.5)

# --------------------------------------------------
# Force the SAME y-axis range across all 3 plots
# --------------------------------------------------
ax.set_ylim(0, 1.1)

plt.tight_layout()
plt.show()
