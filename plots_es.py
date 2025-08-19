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


def plot_vaccination_coverage_es():
    df_es = pd.read_csv("./data/vaccination_coverage_es.csv")

    mean_es = df_es[['2021', '2022', '2023']].mean()

    df_high = df_es[(df_es[['2021','2022','2023']] >= 95).any(axis=1) &
                    (df_es[['2021','2022','2023']] < 100).all(axis=1) &
                    (df_es[['2021','2022','2023']].gt(mean_es).any(axis=1))]
    if not df_high.empty:
        mun_high_data = df_high.iloc[0, 1:]
        mun_high_name = df_high.iloc[0]['city']
    else:
        mun_high_data = None
        mun_high_name = None

    df_low = df_es[(df_es[['2021','2022','2023']].lt(mean_es)).all(axis=1)]
    if not df_low.empty:
        mun_low_data = df_low.iloc[0, 1:]
        mun_low_name = df_low.iloc[0]['city']
    else:
        mun_low_data = None
        mun_low_name = None

    mpl.rcParams['font.family'] = 'Times New Roman'
    plt.figure(figsize=(10, 6))

    plt.axhspan(95, 100, color='lightgreen', alpha=0.3)
    plt.text(2.11, 96, 'Faixa ideal', color='green',
             fontsize=FONT_TEXT, fontweight='bold')

    plt.plot(mean_es.index, mean_es.values,
             marker='o', markersize=MARKER_SIZE, linewidth=LINE_WIDTH,
             label='Espírito Santo', color='blue')

    if mun_high_data is not None:
        plt.plot(mun_high_data.index, mun_high_data.values,
                 marker='o', markersize=MARKER_SIZE, linewidth=LINE_WIDTH,
                 label=mun_high_name.capitalize(), color='green')

    if mun_low_data is not None:
        plt.plot(mun_low_data.index, mun_low_data.values,
                 marker='o', markersize=MARKER_SIZE, linewidth=LINE_WIDTH,
                 label=mun_low_name.capitalize(), color='orange')

    plt.title("Cobertura Vacinal Tríplice Viral no Espírito Santo (2021–2023)", fontsize=FONT_TITLE)
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


def plot_coverage_es_cities_es(year: str):
    df_es = pd.read_csv("./data/vaccination_coverage_es.csv")

    df_es_year = df_es[['city', year]].sort_values(by=year, ascending=False)

    mpl.rcParams['font.family'] = 'Times New Roman'
    plt.figure(figsize=(16, 6))

    colors = ['green' if v >= 95 else 'red' for v in df_es_year[year]]
    plt.bar(df_es_year['city'], df_es_year[year], color=colors, width=0.8)

    plt.axhline(95, color='blue', linestyle='--', linewidth=LINE_WIDTH)
    plt.text(len(df_es_year)-10, 98, 'Meta 95%', color='blue', fontsize=FONT_TEXT, fontweight='bold')

    plt.ylabel("Cobertura (%)", fontsize=FONT_AXES)

    x_ticks = df_es_year['city']
    x_colors = ['limegreen' if v >= 95 else 'firebrick' for v in df_es_year[year]]

    ticks = plt.xticks(ticks=range(len(x_ticks)), labels=x_ticks, rotation=90, fontsize=15)[1]
    for tick, color in zip(ticks, x_colors):
        tick.set_color(color)

    plt.yticks(fontsize=FONT_TICKS)
    plt.title(f"Cobertura Vacinal Tríplice Viral por Município do ES ({year})", fontsize=FONT_TITLE)

    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.subplots_adjust(bottom=0.30)
    plt.show()

