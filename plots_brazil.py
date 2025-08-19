import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

FONT_TITLE = 28
FONT_AXES = 24
FONT_TICKS = 24
FONT_LEGEND = 22
FONT_TEXT = 24
LINE_WIDTH = 4
MARKER_SIZE = 14


def plot_vaccination_coverage_brazil():
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

    plt.title("Cobertura Vacinal Tríplice Viral no Brasil (2021–2023)", fontsize=FONT_TITLE)
    plt.xlabel("Ano", fontsize=FONT_AXES)
    plt.ylabel("Cobertura (%)", fontsize=FONT_AXES)

    yticks = list(range(0, 100, 10)) + [95] + [100]
    yticks = sorted(set(yticks))
    plt.yticks(yticks, fontsize=FONT_TICKS)
    plt.xticks(fontsize=FONT_TICKS)

    plt.ylim(0, 100)
    plt.legend(fontsize=FONT_LEGEND)
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()


def plot_cases_brazil():
    df_cases = pd.read_csv("./data/confirmed_cases.csv")

    mean_cases = df_cases[['2021', '2022', '2023']].mean()

    es_cases = df_cases[df_cases['uf'] == 'Espírito Santo'].iloc[0, 1:]

    mpl.rcParams['font.family'] = 'Times New Roman'

    color_brasil = 'darkorange'
    color_es = 'purple'

    plt.figure(figsize=(10, 6))

    plt.plot(mean_cases.index, mean_cases.values,
             marker='o', markersize=MARKER_SIZE, linewidth=LINE_WIDTH,
             label='Brasil', color=color_brasil)
    plt.plot(es_cases.index, es_cases.values,
             marker='o', markersize=MARKER_SIZE, linewidth=LINE_WIDTH,
             label='Espírito Santo', color=color_es)

    plt.title("Casos Confirmados de Sarampo/Rubéola no Brasil (2021-2023)", fontsize=FONT_TITLE)
    plt.ylabel("Casos Confirmados", fontsize=FONT_AXES)
    plt.xlabel("Ano", fontsize=FONT_AXES)
    plt.xticks(fontsize=FONT_TICKS)
    plt.yticks(fontsize=FONT_TICKS)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=FONT_LEGEND)

    plt.tight_layout()
    plt.show()


def plot_cases_vs_vaccination_brazil():
    df_vac = pd.read_csv("./data/vaccination_coverage.csv")
    df_cases = pd.read_csv("./data/confirmed_cases.csv")

    df_cases['total'] = df_cases[['2021', '2022', '2023']].sum(axis=1)
    df_vac['media'] = df_vac[['2021', '2022', '2023']].mean(axis=1)

    df_merge = df_vac[['uf', 'media']].merge(df_cases[['uf', 'total']], on='uf')

    mpl.rcParams['font.family'] = 'Times New Roman'

    plt.figure(figsize=(12, 8))

    destaque_ufs = ['Amapá', 'Pará', 'Acre', 'Espírito Santo']

    for _, row in df_merge.iterrows():
        if row['uf'] == 'Espírito Santo':
            plt.scatter(row['media'], row['total'], color='red', s=200, label='Espírito Santo',
                        edgecolor='black', zorder=3)
            plt.text(row['media'] + 0.5, row['total'] - 25, row['uf'], fontsize=FONT_TEXT, fontweight='bold', color='red')
        elif row['uf'] in destaque_ufs:
            plt.scatter(row['media'], row['total'], color='blue', s=200, zorder=2)
            plt.text(row['media'] + 0.5, row['total'] + 0.2, row['uf'], fontsize=FONT_TEXT, fontweight='bold', color='blue')
        else:
            plt.scatter(row['media'], row['total'], s=200, alpha=0.7, color='gray', zorder=1)

    plt.xlabel("Cobertura Vacinal Média 2021-2023 (%)", fontsize=FONT_AXES)
    plt.ylabel("Casos Confirmados 2021-2023", fontsize=FONT_AXES)
    plt.xticks(fontsize=FONT_TICKS)
    plt.yticks(fontsize=FONT_TICKS)
    plt.title("Cobertura Vacinal vs Casos Confirmados por Estado", fontsize=FONT_TITLE)
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()