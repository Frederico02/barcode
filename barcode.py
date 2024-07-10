import barcode
from barcode.writer import ImageWriter

# Função para gerar o código de barras Code 128 com 5 dígitos
def gerar_codigo_de_barras(matricula):
    # Verifica se a matrícula tem exatamente 5 dígitos
    if (len(matricula) > 6) or not matricula.isdigit():
        raise ValueError("A matrícula deve conter exatamente 5 dígitos numéricos.")

    # Cria um objeto de código de barras do tipo Code 128
    codigo_de_barras = barcode.get_barcode_class('code128')

    # Gera o código de barras com a matrícula
    codigo = codigo_de_barras(matricula, writer=ImageWriter())

    # Salva o código de barras em um arquivo PNG
    nome_arquivo = 'codigo_de_barras'
    codigo.save(nome_arquivo)

    return nome_arquivo  # Retorna o nome do arquivo gerado

# Obtém a matrícula do usuário
matricula = input("Digite os 5 dígitos da matrícula: ")

# Chama a função para gerar o código de barras
nome_arquivo = gerar_codigo_de_barras(matricula)

print(f'Código de barras gerado com sucesso! Salvo como {nome_arquivo}')
