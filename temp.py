df_es = pd.read_csv("./data/vaccination_coverage_es.csv")


df_es_2023 = df_es[['city','2022']].sort_values(by='2022', ascending=False)

plt.figure(figsize=(12,6))

# Pintar barras de acordo com a meta (verde acima, vermelho abaixo)
colors = ['green' if v >= 95 else 'red' for v in df_es_2023['2022']]

bars = plt.bar(df_es_2023['city'], df_es_2023['2022'], color=colors)

# Linha de meta em 95%
plt.axhline(95, color='blue', linestyle='--', linewidth=2, label='Meta 95%')

plt.xticks(rotation=90)
plt.ylabel("Cobertura (%)")
plt.title("Cobertura Vacinal Tríplice Viral por Município do ES (2021)")
plt.legend()
plt.show()






plt.figure(figsize=(12,8))

for _, row in df_es.iterrows():
    plt.plot(['2021','2022','2023'], row[1:], alpha=0.6)

plt.title("Evolução da Cobertura Vacinal por Município (ES)")
plt.xlabel("Ano")
plt.ylabel("Cobertura (%)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()




plt.figure(figsize=(8,6))
df_es[['2021','2022','2023']].boxplot()
plt.title("Distribuição da Cobertura Vacinal por Ano (Municípios do ES)")
plt.ylabel("Cobertura (%)")
plt.show()





df_sorted = df_es[['city','2023']].sort_values(by='2023')

bottom5 = df_sorted.head(5)
top5 = df_sorted.tail(5)

plt.figure(figsize=(10,6))
plt.bar(bottom5['city'], bottom5['2023'], color='red', label='Menor cobertura')
plt.bar(top5['city'], top5['2023'], color='green', label='Maior cobertura')
plt.xticks(rotation=45)
plt.ylabel("Cobertura (%)")
plt.title("Municípios com Maior e Menor Cobertura Vacinal em 2023 (ES)")
plt.legend()
plt.show()







# Carregar dados municipais
df_es = pd.read_csv("./data/vaccination_coverage_es.csv")

# Identificar municípios que atingiram >=95 em algum ano
mask_high = (df_es[['2021','2022','2023']] >= 95).any(axis=1)
df_high = df_es[mask_high]
df_low = df_es[~mask_high]  # nunca atingiram 95

# Média apenas dos municípios que nunca atingiram 95
mean_low = df_low[['2021','2022','2023']].mean()

plt.figure(figsize=(10,7))

# Faixa de destaque (95–100%)
plt.axhspan(95, 100, color='lightgreen', alpha=0.3, label='Meta 95–100%')

# Plotar média dos que nunca atingiram 95
plt.plot(['2021','2022','2023'], mean_low.values,
         marker='o', linewidth=3, color='blue', label='Média (nunca ≥95%)')

# Plotar individualmente os municípios que atingiram >=95%
for _, row in df_high.iterrows():
    plt.plot(['2021','2022','2023'], row[1:],
             marker='o', linestyle='--', alpha=0.8, label=row['city'])

plt.title("Cobertura Vacinal da Tríplice Viral (Municípios do ES, 2021–2023)")
plt.xlabel("Ano")
plt.ylabel("Cobertura (%)")
plt.ylim(0, 130)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()