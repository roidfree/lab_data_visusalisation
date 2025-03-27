import matplotlib.pyplot as plt

# --------------------------------------------------
# 1) Data Setup
# --------------------------------------------------
time_points = [0, 24, 48, 72]  # Time in hours

# Seeding densities and absorbance values
densities = ["5.0×10⁴", "3.9×10⁴", "3.04×10⁴", "2.37×10⁴", "1.85×10⁴", "1.5×10⁴"]

dm_data = [
    [0.328003, 0.439906, 0.508586, 0.319443],
    [0.380051, 0.427489, 0.473436, 0.304704],
    [0.284385, 0.402841, 0.461662, 0.311829],
    [0.252153, 0.404759, 0.456321, 0.312752],
    [0.28635,  0.377911, 0.445695, 0.315278],
    [0.280953, 0.372226, 0.430178, 0.339794],
]

hela_data = [
    [0.342276, 0.441617, 0.646196, 0.577428],
    [0.310251, 0.373875, 0.623763, 0.485233],
    [0.33684,  0.365097, 0.5693,   0.394081],
    [0.302833, 0.358662, 0.517293, 0.419843],
    [0.30624,  0.321545, 0.559839, 0.350763],
    [0.274288, 0.345019, 0.462045, 0.360551],
]

# --------------------------------------------------
# 2) Create Subplots (3 rows × 2 columns)
# --------------------------------------------------
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 10), sharex=True, sharey=True)

for i, ax in enumerate(axes.flat):
    # Plot for one density
    ax.plot(time_points, dm_data[i], marker='o', color='tab:blue', label='DM')
    ax.plot(time_points, hela_data[i], marker='o', linestyle='--', color='tab:red', label='HeLa')
    
    ax.set_title(f'Density {i+1} ({densities[i]})', fontsize=11)
    ax.set_xticks(time_points)
    ax.grid(True, linestyle='--', alpha=0.5)
    
    if i in [4, 5]:  # Bottom row
        ax.set_xlabel("Time (hr)")
    if i % 2 == 0:   # Left column
        ax.set_ylabel("Absorbance")

# --------------------------------------------------
# 3) Shared Legend and Final Styling
# --------------------------------------------------
# Add a single legend outside the plots
handles, labels = axes[0, 0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', ncol=2, fontsize=10, bbox_to_anchor=(0.5, 1.03))

fig.suptitle("Absorbance over Time: DM vs HeLa at Different Seeding Densities", fontsize=14)
plt.tight_layout(rect=[0, 0, 1, 0.97])  # Leave space for the legend
plt.show()
