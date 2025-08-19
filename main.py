import pandas as pd
import matplotlib.pyplot as plt
from plots_brazil import plot_vaccination_coverage, plot_cases_vs_vaccination

# plot_vaccination_coverage()
# plot_cases_vs_vaccination()




# Importar arquivos
df_vac = pd.read_csv("./data/vaccination_coverage.csv")
df_cases = pd.read_csv("./data/confirmed_cases.csv")

# Conferir colunas
print(df_vac.head())
print(df_cases.head())














mean_cases = df_cases[['2021','2022','2023']].mean()
es_cases = df_cases[df_cases['uf']=='Espírito Santo'].iloc[0, 1:-1]

plt.figure(figsize=(10,6))
plt.plot(mean_cases.index, mean_cases.values, marker='o', label='Brasil (média)')
plt.plot(es_cases.index, es_cases.values, marker='o', label='Espírito Santo', linewidth=3)

plt.title("Casos Confirmados de Sarampo/Rubéola (2021-2023)", fontsize=16)
plt.ylabel("Casos Confirmados")
plt.xlabel("Ano")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

