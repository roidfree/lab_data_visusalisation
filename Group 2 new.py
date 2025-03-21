import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# --------------------------------------------------
# 1) Hard-code your Glutamine absorbance data
# --------------------------------------------------
absorbance_data = {
    # --- 0.5 mM ---
    ('0.5mM', 3.9,  'DM'):   {'0h': 0.460666667, '48h': 0.470666667},
    ('0.5mM', 3.9,  'HeLa'): {'0h': 0.495,       '48h': 0.568666667},

    ('0.5mM', 2.97, 'DM'):   {'0h': 0.399,       '48h': 0.424333333},
    ('0.5mM', 2.97, 'HeLa'): {'0h': 0.509666667, '48h': 0.426},

    ('0.5mM', 1.85, 'DM'):   {'0h': 0.392666667, '48h': 0.410666667},
    ('0.5mM', 1.85, 'HeLa'): {'0h': 0.495,       '48h': 0.437},

    # --- 2 mM ---
    ('2mM',   3.9,  'DM'):   {'0h': 0.350333333, '48h': 0.461},
    ('2mM',   3.9,  'HeLa'): {'0h': 0.522666667, '48h': 0.745},

    ('2mM',   2.97, 'DM'):   {'0h': 0.390666667, '48h': 0.428666667},
    ('2mM',   2.97, 'HeLa'): {'0h': 0.546333333, '48h': 0.615},

    ('2mM',   1.85, 'DM'):   {'0h': 0.422333333, '48h': 0.408},
    ('2mM',   1.85, 'HeLa'): {'0h': 0.569666667, '48h': 0.604},

    # --- 5 mM ---
    ('5mM',   3.9,  'DM'):   {'0h': 0.532,       '48h': 0.687},
    ('5mM',   3.9,  'HeLa'): {'0h': 0.449333333, '48h': 0.582666667},

    ('5mM',   2.97, 'DM'):   {'0h': 0.449333333, '48h': 0.628666667},
    ('5mM',   2.97, 'HeLa'): {'0h': 0.371,       '48h': 0.621333333},

    ('5mM',   1.85, 'DM'):   {'0h': 0.474,       '48h': 0.670333333},
    ('5mM',   1.85, 'HeLa'): {'0h': 0.363666667, '48h': 0.566333333},

    # --- 8 mM ---
    ('8mM',   3.9,  'DM'):   {'0h': 0.555666667, '48h': 0.683333333},
    ('8mM',   3.9,  'HeLa'): {'0h': 0.431333333, '48h': 0.741},

    ('8mM',   2.97, 'DM'):   {'0h': 0.345333333, '48h': 0.563666667},
    ('8mM',   2.97, 'HeLa'): {'0h': 0.423666667, '48h': 0.565333333},

    ('8mM',   1.85, 'DM'):   {'0h': 0.488333333, '48h': 0.605666667},
    ('8mM',   1.85, 'HeLa'): {'0h': 0.418666667, '48h': 0.517666667},
}

# --------------------------------------------------
# 1b) Hard-code your SEM data in a parallel dictionary
# --------------------------------------------------
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
# 2) Define the order of categories
# --------------------------------------------------
nutrient_concs = ['0.5mM', '2mM', '5mM', '8mM']  # 4 concentrations
cell_concs = [3.9, 2.97, 1.85]                  # 3 seeding densities
cell_types = ['DM', 'HeLa']                     # 2 cell types
time_points = ['0h', '48h']                     # 2 time points

# Build 12 groups total (4 concentrations × 3 densities)
groups = [(nc, cc) for nc in nutrient_concs for cc in cell_concs]

# --------------------------------------------------
# 3) Set up figure and bar parameters
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
# 4) Plot the data with error bars
# --------------------------------------------------
x_positions = []
labels = []

for i, (nutrient, cc) in enumerate(groups):
    # Each group has 2 cell types × 2 time points = 4 bars
    group_width = len(cell_types) * len(time_points) * bar_width
    group_left = i * (group_width + group_spacing)
    
    bar_index = 0
    for cell_type in cell_types:
        for time_point in time_points:
            val = absorbance_data[(nutrient, cc, cell_type)][time_point]
            err = sem_data[(nutrient, cc, cell_type)][time_point]  # <-- SEM lookup

            x = group_left + bar_index * bar_width
            ax.bar(
                x, val, width=bar_width,
                color=colors[(cell_type, time_point)],
                edgecolor='black', linewidth=0.5,
                yerr=err, capsize=3  # <-- Add error bars
            )
            bar_index += 1
    
    # Calculate center of the group for x-axis label
    group_center = group_left + group_width / 2 - bar_width / 2
    x_positions.append(group_center)
    labels.append(f"{nutrient}\n{cc}")

# --------------------------------------------------
# 5) Format axes, legend, etc.
# --------------------------------------------------
ax.set_title("Glutamine (0.5, 2, 5, 8 mM): 0h vs. 48h Absorbance", fontsize=14)
ax.set_xlabel("Nutrient & Cell Concentration (x10^4)", fontsize=12)
ax.set_ylabel("Absorbance", fontsize=12)

ax.set_xticks(x_positions)
ax.set_xticklabels(labels, rotation=0, fontsize=10)

# Build legend
legend_handles = []
for ct in cell_types:
    for tp in time_points:
        patch = mpatches.Patch(
            color=colors[(ct, tp)],
            label=f"{ct} {tp}",
            edgecolor='black', linewidth=0.5
        )
        legend_handles.append(patch)

# Remove duplicate labels
unique_labels = []
unique_handles = []
for h in legend_handles:
    if h.get_label() not in unique_labels:
        unique_labels.append(h.get_label())
        unique_handles.append(h)

ax.legend(handles=unique_handles, loc='upper left', ncol=2, bbox_to_anchor=(0, 1.15))

# Optional: Draw vertical dashed lines to separate nutrient concentrations
for i in range(len(groups) - 1):
    # If the next group has a different nutrient concentration, draw a divider
    if groups[i][0] != groups[i + 1][0]:
        x_line = (x_positions[i] + x_positions[i + 1]) / 2
        ax.axvline(x_line, color='black', linestyle='--', alpha=0.8)

ax.grid(axis='y', linestyle='--', alpha=0.5)

# Set y-limit a bit higher than max to accommodate error bars
max_val = max(absorbance_data[k][t] for k in absorbance_data for t in absorbance_data[k])
ax.set_ylim(0, max_val * 1.1)

plt.tight_layout()
plt.show()
