import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

FONT_TITLE = 28
FONT_AXES = 24
FONT_TICKS = 24
FONT_LEGEND = 22
FONT_TEXT = 24
LINE_WIDTH = 4
MARKER_SIZE = 14

def plot_vaccination_coverage():
    df_vac = pd.read_csv("./data/vaccination_coverage.csv")

    mean_vac = df_vac[['2021', '2022', '2023']].mean()
    es_vac = df_vac[df_vac['uf'] == 'Espírito Santo'].iloc[0, 1:]

    mpl.rcParams['font.family'] = 'Times New Roman'

    plt.figure(figsize=(10, 6))

    plt.axhspan(95, 100, color='lightgreen', alpha=0.3)
    plt.text(2.11, 96, 'Faixa ideal', color='green',
             fontsize=FONT_TEXT, fontweight='bold')

    plt.plot(mean_vac.index, mean_vac.values,
             marker='o', markersize=MARKER_SIZE, linewidth=LINE_WIDTH,
             label='Brasil', color='gray')
    plt.plot(es_vac.index, es_vac.values,
             marker='o', markersize=MARKER_SIZE, linewidth=LINE_WIDTH,
             label='Espírito Santo', color='blue')

    plt.title("Cobertura Vacinal Tríplice Viral (2021–2023)", fontsize=FONT_TITLE)
    plt.xlabel("Ano", fontsize=FONT_AXES)
    plt.ylabel("Cobertura (%)", fontsize=FONT_AXES)

    yticks = list(range(0, 110, 10)) + [95]
    yticks = sorted(set(yticks))
    plt.yticks(yticks, fontsize=FONT_TICKS)
    plt.xticks(fontsize=FONT_TICKS)

    plt.ylim(0, 105)
    plt.legend(fontsize=FONT_LEGEND)
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()