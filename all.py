from pycpfcnpj import cpfcnpj
from itertools import product

def is_valid_cnpj(cnpj: str) -> bool:
    # Removendo caracteres que não sejam números
    cnpj = ''.join(filter(str.isdigit, cnpj))

    # Verificando se o CNPJ tem 14 dígitos
    if len(cnpj) != 14:
        return False

    # Verificando se o CNPJ é formado por dígitos repetidos
    if cnpj == cnpj[0] * 14:
        return False

    # Usando a função cpfcnpj.validate para validar o CNPJ
    return cpfcnpj.validate(cnpj)

def generate_combinations(number: str, additional_digits: str, control_digits: str) -> dict:
    num_asterisks = number.count('*') + control_digits.count('*')

    combinations = {}
    for idx, comb in enumerate(product(additional_digits, repeat=num_asterisks)):
        temp_number = number
        temp_control_digits = control_digits
        for digit in comb:
            if '*' in temp_number:
                temp_number = temp_number.replace('*', digit, 1)
            else:
                temp_control_digits = temp_control_digits.replace('*', digit, 1)
        temp_cnpj = temp_number + temp_control_digits
        if is_valid_cnpj(temp_cnpj):
            combinations[idx] = temp_cnpj

    return combinations

number = '2498206000**' #informe aqui o cnpj mascarado (SEM OS DIGITOS DE VERIFICAÇÃO)
control_digits = '**' #se possuir o dígito verificador do cnpj, informe aqui. caso contrario deixe ** ou ainda 3*
additional_digits = '0123456789' #estes são os digitos usando para preencher as lacunas, não altere!

combinations = generate_combinations(number, additional_digits, control_digits)
counter = 0  # Inicializa o contador como 0
for combination_list in combinations.values():
    cnpj_number = combination_list.replace('-', '')  # Remove o traço do número de CNPJ
    print(cnpj_number)
    counter += 1  # Incrementa o contador

print("Quantidade de resultados encontrados:", counter)
