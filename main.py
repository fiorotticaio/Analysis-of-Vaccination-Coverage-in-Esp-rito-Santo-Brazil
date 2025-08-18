import pandas as pd
import matplotlib.pyplot as plt

# Importar arquivos
df_vac = pd.read_csv("./data/vaccination_coverage.csv")
df_cases = pd.read_csv("./data/confirmed_cases.csv")

# Conferir colunas
print(df_vac.head())
print(df_cases.head())





# Médias nacionais por ano
mean_vac = df_vac[['2021', '2022', '2023']].mean()

# Dados do ES
es_vac = df_vac[df_vac['uf'] == 'Espírito Santo'].iloc[0, 1:]

plt.figure(figsize=(10,6))
plt.plot(mean_vac.index, mean_vac.values, marker='o', label='Brasil (média)')
plt.plot(es_vac.index, es_vac.values, marker='o', label='Espírito Santo', linewidth=3)

plt.title("Cobertura Vacinal Tríplice Viral (2021-2023)", fontsize=16)
plt.ylabel("Cobertura (%)")
plt.xlabel("Ano")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()




df_vac_2023 = df_vac[['uf','2023']].sort_values(by='2023', ascending=False)

plt.figure(figsize=(12,6))
bars = plt.bar(df_vac_2023['uf'], df_vac_2023['2023'])

# Destacar ES
for bar, uf in zip(bars, df_vac_2023['uf']):
    if uf == 'Espírito Santo':
        bar.set_color('red')

plt.xticks(rotation=90)
plt.ylabel("Cobertura (%)")
plt.title("Cobertura Vacinal Tríplice Viral em 2023 por Estado")
plt.show()




# Somar casos por estado no período
df_cases['total'] = df_cases[['2021','2022','2023']].sum(axis=1)
df_vac['media'] = df_vac[['2021','2022','2023']].mean(axis=1)

# Juntar em um único dataframe
df_merge = df_vac[['uf','media']].merge(df_cases[['uf','total']], on='uf')

plt.figure(figsize=(12,8))

# Scatter com cada estado em cor diferente
for _, row in df_merge.iterrows():
    if row['uf'] == 'Espírito Santo':
        plt.scatter(row['media'], row['total'], color='red', s=150, label='Espírito Santo', edgecolor='black', zorder=3)
        plt.text(row['media']+0.2, row['total']+0.2, row['uf'], fontsize=9, fontweight='bold', color='red')
    else:
        plt.scatter(row['media'], row['total'], s=80, alpha=0.7)
        plt.text(row['media']+0.2, row['total']+0.2, row['uf'], fontsize=8, alpha=0.7)

plt.xlabel("Cobertura Vacinal Média (2021-2023) [%]")
plt.ylabel("Casos Confirmados (2021-2023)")
plt.title("Cobertura Vacinal vs Casos Confirmados por Estado")
plt.grid(True, linestyle='--', alpha=0.7)

# plt.legend()
plt.show()





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

