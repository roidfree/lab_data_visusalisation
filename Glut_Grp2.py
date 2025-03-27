import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# --------------------------------------------------
# 1) Glutamine absorbance data + SEM
# --------------------------------------------------
absorbance_data = {
    # 0.5 mM
    ('0.5mM', 3.9,  'DM'):   {'0h': 0.460666667, '48h': 0.470666667},
    ('0.5mM', 3.9,  'HeLa'): {'0h': 0.495,       '48h': 0.568666667},

    ('0.5mM', 2.97, 'DM'):   {'0h': 0.399,       '48h': 0.424333333},
    ('0.5mM', 2.97, 'HeLa'): {'0h': 0.509666667, '48h': 0.426},

    ('0.5mM', 1.85, 'DM'):   {'0h': 0.392666667, '48h': 0.410666667},
    ('0.5mM', 1.85, 'HeLa'): {'0h': 0.495,       '48h': 0.437},

    # 2 mM
    ('2mM',   3.9,  'DM'):   {'0h': 0.350333333, '48h': 0.461},
    ('2mM',   3.9,  'HeLa'): {'0h': 0.522666667, '48h': 0.745},

    ('2mM',   2.97, 'DM'):   {'0h': 0.390666667, '48h': 0.428666667},
    ('2mM',   2.97, 'HeLa'): {'0h': 0.546333333, '48h': 0.615},

    ('2mM',   1.85, 'DM'):   {'0h': 0.422333333, '48h': 0.408},
    ('2mM',   1.85, 'HeLa'): {'0h': 0.569666667, '48h': 0.604},

    # 5 mM
    ('5mM',   3.9,  'DM'):   {'0h': 0.532,       '48h': 0.687},
    ('5mM',   3.9,  'HeLa'): {'0h': 0.449333333, '48h': 0.582666667},

    ('5mM',   2.97, 'DM'):   {'0h': 0.449333333, '48h': 0.628666667},
    ('5mM',   2.97, 'HeLa'): {'0h': 0.371,       '48h': 0.621333333},

    ('5mM',   1.85, 'DM'):   {'0h': 0.474,       '48h': 0.670333333},
    ('5mM',   1.85, 'HeLa'): {'0h': 0.363666667, '48h': 0.566333333},

    # 8 mM
    ('8mM',   3.9,  'DM'):   {'0h': 0.555666667, '48h': 0.683333333},
    ('8mM',   3.9,  'HeLa'): {'0h': 0.431333333, '48h': 0.741},

    ('8mM',   2.97, 'DM'):   {'0h': 0.345333333, '48h': 0.563666667},
    ('8mM',   2.97, 'HeLa'): {'0h': 0.423666667, '48h': 0.565333333},

    ('8mM',   1.85, 'DM'):   {'0h': 0.488333333, '48h': 0.605666667},
    ('8mM',   1.85, 'HeLa'): {'0h': 0.418666667, '48h': 0.517666667},
}

sem_data = {
    # 0.5 mM
    ('0.5mM', 3.9,  'DM'):   {'0h': 0.088161468, '48h': 0.019376389},
    ('0.5mM', 3.9,  'HeLa'): {'0h': 0.023586719, '48h': 0.100800683},

    ('0.5mM', 2.97, 'DM'):   {'0h': 0.044185216, '48h': 0.009134793},
    ('0.5mM', 2.97, 'HeLa'): {'0h': 0.008171767, '48h': 0.032746501},

    ('0.5mM', 1.85, 'DM'):   {'0h': 0.052941267, '48h': 0.013119112},
    ('0.5mM', 1.85, 'HeLa'): {'0h': 0.009643651, '48h': 0.010692677},

    # 2 mM
    ('2mM',   3.9,  'DM'):   {'0h': 0.030024064, '48h': 0.003},
    ('2mM',   3.9,  'HeLa'): {'0h': 0.013169831, '48h': 0.067300322},

    ('2mM',   2.97, 'DM'):   {'0h': 0.021457969, '48h': 0.019547663},
    ('2mM',   2.97, 'HeLa'): {'0h': 0.018351506, '48h': 0.051393904},

    ('2mM',   1.85, 'DM'):   {'0h': 0.070385447, '48h': 0.022233608},
    ('2mM',   1.85, 'HeLa'): {'0h': 0.02459223,  '48h': 0.018770544},

    # 5 mM
    ('5mM',   3.9,  'DM'):   {'0h': 0.006350853, '48h': 0.0090185},
    ('5mM',   3.9,  'HeLa'): {'0h': 0.047361494, '48h': 0.014426057},

    ('5mM',   2.97, 'DM'):   {'0h': 0.061941729, '48h': 0.031497795},
    ('5mM',   2.97, 'HeLa'): {'0h': 0.187820245, '48h': 0.051969008},

    ('5mM',   1.85, 'DM'):   {'0h': 0.008504901, '48h': 0.018764624},
    ('5mM',   1.85, 'HeLa'): {'0h': 0.214045426, '48h': 0.030123819},

    # 8 mM
    ('8mM',   3.9,  'DM'):   {'0h': 0.022849751, '48h': 0.041025737},
    ('8mM',   3.9,  'HeLa'): {'0h': 0.199474588, '48h': 0.032347076},

    ('8mM',   2.97, 'DM'):   {'0h': 0.147248467, '48h': 0.061553048},
    ('8mM',   2.97, 'HeLa'): {'0h': 0.168262691, '48h': 0.072014659},

    ('8mM',   1.85, 'DM'):   {'0h': 0.017816971, '48h': 0.036771064},
    ('8mM',   1.85, 'HeLa'): {'0h': 0.191704924, '48h': 0.042557151},
}

# --------------------------------------------------
# 2) Plot categories
# --------------------------------------------------
nutrient_concs = ['0.5mM', '2mM', '5mM', '8mM']
cell_concs = [3.9, 2.97, 1.85]
# Map cell concentrations to density labels
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
    ('DM','0h'):    '#90EE90',  # Light green
    ('DM','48h'):   '#228B22',  # Forest green
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

ax.set_title("Glutamine: 0.5, 2, 5, 8 mM (0h vs. 48h, DM vs. HeLa)", fontsize=14)
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
density_key = "Density Key:\nDensity-1: 3.9×10⁴\nDensity-2: 2.97×10⁴\nDensity-3: 1.85×10⁴"
# Position within the chart
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

# Vertical lines between different nutrient concs
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
