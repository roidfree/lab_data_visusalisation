import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#-------------------------------
# 1) PREPARE THE DATA
#-------------------------------

# A) FBS data: DM & HeLa
#   Columns = concentrations, Rows = replicates
fbs_dm = pd.DataFrame({
    2.5: [61.28370471, -448.077965,   154.3160059],
    5:   [98.59463052, -293.9796182,  -98.17424833],
    10:  [2451.722973, -356.7276466, -1023.826917],
    12.5:[-5044.244794, -237.8070206, -156.8098972]
})

fbs_hela = pd.DataFrame({
    2.5: [50.23870478,  18.92534822,  18.57341396],
    5:   [17.11420074,  21.32089817, -84.67832333],
    10:  [26.82638277,  40.34208207, 73.30217933],
    12.5:[43.20696532,  82.54094679, 846.2237001]
})

# B) Glucose data: Normal (N), DM, HeLa
glucose_n = pd.DataFrame({
    2.5: [56.30116752, -40.22372995, 73.56758606],
    5:   [221.307664,  1417.651964,  280.1536171],
    15:  [22.29097021, 76.66600295,  146.4286683],
    25:  [48.6459865,  72.50405977,  77.30936668]
})

glucose_dm = pd.DataFrame({
    2.5: [-682.8209521, -594.2607507, 3129.82711],
    5:   [60.86698701,  104.2419482,  45.55722875],
    15:  [-113.3882971, -338.2410578, -144.7139807],
    25:  [409.1533188,  -104.0702002, 1829.858145]
})

glucose_hela = pd.DataFrame({
    2.5: [39.45994256,  30.58409733, 36.19680954],
    5:   [25.35857095,  29.39448794, 25.41211834],
    15:  [40.26207789,  38.16022657, 39.84536876],
    25:  [30.67046296,  27.96150803, 35.99011325]
})

# C) Glutamine data: DM & HeLa
glut_dm = pd.DataFrame({
    0.5: [-2212.484107,   0,          -1447.227573],
    2:   [0,            -574.6895545, -185.0519443],
    5:   [-2911.186471, 4441.666364,   624.8730966],
    8:   [406.5875259,   267.9037185,  620.1189558]
})

glut_hela = pd.DataFrame({
    0.5: [239.8144848,   -185.542691,   -266.9703522],
    2:   [93.86930349,   281.0222811,   568.5145394],
    5:   [128.0393718,    64.52061536,  75.11328599],
    8:   [61.48562087,   115.3368893,   156.74935]
})

# Helper function to get mean & std in a convenient form
def get_mean_std(df, cell_line_name):
    """ 
    Returns a DataFrame with columns = ['Concentration','CellLine','Mean','Std'] 
    from a DataFrame where columns=concentrations, rows=replicates.
    """
    means = df.mean(axis=0)
    stds  = df.std(axis=0)
    out_df = pd.DataFrame({
        'Concentration': means.index,
        'Mean': means.values,
        'Std': stds.values
    })
    out_df['CellLine'] = cell_line_name
    return out_df

# Build a tidy DataFrame for plotting each nutrient type:

# 1) FBS -> DM & HeLa
fbs_dm_stats   = get_mean_std(fbs_dm,   'DM')
fbs_hela_stats = get_mean_std(fbs_hela, 'HeLa')
fbs_all = pd.concat([fbs_dm_stats, fbs_hela_stats], ignore_index=True)

# 2) Glucose -> N, DM, HeLa
glu_n_stats   = get_mean_std(glucose_n,   'Normal')
glu_dm_stats  = get_mean_std(glucose_dm,  'DM')
glu_hela_stats= get_mean_std(glucose_hela,'HeLa')
glu_all = pd.concat([glu_n_stats, glu_dm_stats, glu_hela_stats], ignore_index=True)

# 3) Glutamine -> DM & HeLa
gluT_dm_stats   = get_mean_std(glut_dm,   'DM')
gluT_hela_stats = get_mean_std(glut_hela, 'HeLa')
gluT_all = pd.concat([gluT_dm_stats, gluT_hela_stats], ignore_index=True)

#-------------------------------
# 2) PLOT THE GROUPED BAR CHARTS
#-------------------------------
sns.set(style='whitegrid', font_scale=1.1)

fig, axes = plt.subplots(1, 3, figsize=(18, 5), sharey=False)

# A) FBS Plot
sns.barplot(
    data=fbs_all, 
    x='Concentration', y='Mean', hue='CellLine',
    ax=axes[0], capsize=0.1, palette='Set2'
)
axes[0].errorbar(
    x=np.arange(len(fbs_all['Concentration'].unique())).repeat(2),  # 2 bars per group
    y=fbs_all['Mean'], 
    yerr=fbs_all['Std'], 
    fmt='none', c='black', capsize=3
)
axes[0].set_title("FBS (DM vs HeLa)")
axes[0].set_ylabel("Measurement")
axes[0].legend()

# B) Glucose Plot
sns.barplot(
    data=glu_all, 
    x='Concentration', y='Mean', hue='CellLine',
    ax=axes[1], capsize=0.1, palette='Set1'
)
axes[1].errorbar(
    x=np.arange(len(glu_all['Concentration'].unique())).repeat(3),  # 3 bars per group
    y=glu_all['Mean'], 
    yerr=glu_all['Std'], 
    fmt='none', c='black', capsize=3
)
axes[1].set_title("Glucose (Normal vs DM vs HeLa)")
axes[1].set_ylabel("Measurement")
axes[1].legend()

# C) Glutamine Plot
sns.barplot(
    data=gluT_all, 
    x='Concentration', y='Mean', hue='CellLine',
    ax=axes[2], capsize=0.1, palette='Set2'
)
axes[2].errorbar(
    x=np.arange(len(gluT_all['Concentration'].unique())).repeat(2),  # 2 bars per group
    y=gluT_all['Mean'], 
    yerr=gluT_all['Std'], 
    fmt='none', c='black', capsize=3
)
axes[2].set_title("Glutamine (DM vs HeLa)")
axes[2].set_ylabel("Measurement")
axes[2].legend()

plt.tight_layout()
plt.show()
