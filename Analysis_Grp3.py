import matplotlib.pyplot as plt
import numpy as np

# --------------------------
# 1) Organized Data
# --------------------------
data_by_stiffness = {
    '10:1': {
        'Glucose': {
            'HeLa 3.9x10^4': 54.3,
            'HeLa 2.37x10^4': 34.7,
            'HeLa 1.85x10^4': 17.0
        }
    },
    '15:1': {
        'FBS 2.5%': {
            'HeLa 3.9x10^4': 34.0,
            'HeLa 2.37x10^4': 13.0,
            'HeLa 1.85x10^4': 14.3,
            'DM 3.9x10^4': 0.0,
            'DM 2.37x10^4': 0.0,
            'DM 1.85x10^4': 0.0
        },
        'Glutamine': {
            'HeLa 3.9x10^4': 6.0,
            'HeLa 2.37x10^4': 2.0,
            'HeLa 1.85x10^4': 0.0
        },
        'Glucose': {
            'HeLa 3.9x10^4': 70.7,
            'HeLa 2.37x10^4': 224.3,
            'HeLa 1.85x10^4': 423.3
        }
    },
    '25:1': {
        'Glutamine': {
            'HeLa 3.9x10^4': 4.7,
            'HeLa 2.37x10^4': 2.0,
            'HeLa 1.85x10^4': 1.3
        }
    },
    '35:1': {
        'Glutamine': {
            'HeLa 3.9x10^4': 17.3,
            'HeLa 2.37x10^4': 7.4,
            'HeLa 1.85x10^4': 1.0
        }
    },
    '40:1': {
        'FBS 2.5%': {
            'HeLa 3.9x10^4': 0.0,
            'HeLa 2.37x10^4': 0.0,
            'HeLa 1.85x10^4': 0.0,
            'DM 3.9x10^4': 0.0,
            'DM 2.37x10^4': 0.0,
            'DM 1.85x10^4': 0.0
        },
        'Glutamine': {
            'HeLa 3.9x10^4': 280.3,
            'HeLa 2.37x10^4': 156.3,
            'HeLa 1.85x10^4': 15.3
        },
        'Glucose': {
            'HeLa 3.9x10^4': 28.7,
            'HeLa 2.37x10^4': 44.7,
            'HeLa 1.85x10^4': 57.3
        }
    }
}

# --------------------------
# 2) Define Categories
# --------------------------
stiffness_ratios = ['10:1', '15:1', '25:1', '35:1', '40:1']
cell_concs       = ['3.9x10^4', '2.37x10^4', '1.85x10^4']
cell_types       = ['DM', 'Normal', 'HeLa']  # 'Normal' may be absent in data

# We want 3 separate charts, one per nutrient
nutrient_types = ['FBS 2.5%', 'Glutamine', 'Glucose']

# --------------------------
# 3) Helper: Get value from data
# --------------------------
def get_value(data, ratio, nutrient, cell_type, cell_conc):
    """
    Return the value for (stiffness, nutrient, "cellType cellConc") if it exists,
    otherwise 0. E.g. "HeLa 3.90x10^4".
    """
    if ratio not in data:
        return 0
    if nutrient not in data[ratio]:
        return 0
    key = f"{cell_type} {cell_conc}"
    return data[ratio][nutrient].get(key, 0)

# --------------------------
# 4) Loop Over Each Nutrient -> One Figure Per Nutrient
# --------------------------
for nutrient in nutrient_types:
    fig, ax = plt.subplots(figsize=(12, 6))
    
    bar_width = 0.12
    group_spacing = 0.5  # spacing between stiffness-ratio groups
    sub_spacing   = 0.02 # spacing between cell-concentration sub-groups
    
    x_positions = []
    x_labels = []
    
    # We'll compute x-coordinates manually
    for i, ratio in enumerate(stiffness_ratios):
        # Left boundary for the group i (this stiffness ratio)
        group_left = i * (len(cell_concs)*len(cell_types)*bar_width + group_spacing)
        
        # For each cell concentration j
        for j, conc in enumerate(cell_concs):
            # left boundary for sub-group j within group i
            sub_left = group_left + j * (len(cell_types)*bar_width + sub_spacing)
            
            # Now place bars for each cell type
            for k, ctype in enumerate(cell_types):
                x = sub_left + k * bar_width
                val = get_value(data_by_stiffness, ratio, nutrient, ctype, conc)
                
                # We'll color by cell type, or you can do a dictionary if you like
                if ctype == 'DM':
                    color = 'royalblue'
                elif ctype == 'Normal':
                    color = 'forestgreen'
                else:  # HeLa
                    color = 'firebrick'
                
                # Label only once to avoid legend repetition
                label = ctype if (i == 0 and j == 0 and k == 0) else None
                
                ax.bar(x, val, bar_width, color=color, edgecolor='black', label=label)
        
        # Center of the entire group for x-tick labeling
        # total width of subgroups = len(cell_concs)*(len(cell_types)*bar_width + sub_spacing)
        # But we subtract the last sub_spacing to be exact
        total_subgroups_width = len(cell_concs)*len(cell_types)*bar_width + (len(cell_concs)-1)*sub_spacing
        group_center = group_left + total_subgroups_width / 2.0
        x_positions.append(group_center)
        x_labels.append(ratio)
    
    # X-axis labels
    ax.set_xticks(x_positions)
    ax.set_xticklabels(x_labels, fontsize=11)
    
    # Title & axis labels
    ax.set_title(f"{nutrient}: DM, Normal, HeLa side-by-side\nGrouped by Cell Conc, Divided by Stiffness Ratio", fontsize=13)
    ax.set_xlabel("Stiffness Ratio", fontsize=12)
    ax.set_ylabel("Proliferation / Cell Count", fontsize=12)
    
    # Legend & grid
    ax.legend(title="Cell Type")
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.show()
