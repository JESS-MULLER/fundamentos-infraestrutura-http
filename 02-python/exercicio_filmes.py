lista_filmes = ["Matrix", "A Rede Social", "Interestelar", "Blade Runner 2049"]
datas_assistidos = ("12-01-2026", "22-03-2026", "10-06-2026", "05-09-2026")
historico_filmes = {}

for i in range(len(lista_filmes)):
    nome_filme = lista_filmes[i]
    data_filme = datas_assistidos[i]
    historico_filmes[nome_filme] = data_filme

print("Histórico de Filmes Gerado:")
print(historico_filmes)
