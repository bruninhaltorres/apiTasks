from validate_docbr import CPF

from datetime import datetime

def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)

def nome_valido(nome):
    if all(char.isalpha() or char.isspace() for char in nome):
        return True
    return False   

def datas_validas(data_inicio, data_limite):
    data_atual = datetime.now().date()

    if data_inicio > data_limite:
        return False
    if data_atual > data_inicio or data_atual > data_limite:
        return False
    
    return True
