import csv

print("--- Lendo o arquivo dados.csv ---")

# Código que você executou com sucesso na imagem:
with open('02-python/aula-02/dados.csv', 'r', newline='') as f:
    leitor = csv.reader(f)
    for linha in leitor:
        print(linha)
