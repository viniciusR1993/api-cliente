import re
from validate_docbr import CPF

def cpf_valido(numero_do_cpf):
        #return len(numero_do_cpf) != 11
       cpf = CPF()
       return cpf.validate(numero_do_cpf)
def nome_valido(nome):
        return not nome.isalpha()
def rg_valido(numero_do_rg):
        return len(numero_do_rg) != 9
def celular_valido(numero_celular):
    """Verifica se o celular é valido 11 91234-1234"""        
    modelo = r'[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_celular)
    return resposta
    #return len(numero_do_celular) < 11
