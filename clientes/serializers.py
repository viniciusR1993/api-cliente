from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"CPF inválido"})
        #return data
        if nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Não inclua numeros nesse campo"})
        #return data
        if rg_valido(data['rg']):
                raise serializers.ValidationError({'rg':"O RG deve ter 9 digitos"})
        #return data
        if not celular_valido(data['celular']):
                raise serializers.ValidationError({'celular':"O numero de celular deve seguir esse modelo: 99 99999-9999"})
        return data
        


    # def validate_cpf(self, cpf):
    #     if len(cpf) != 11:
    #         raise serializers.ValidationError("O CPF deve ter 11 digitos")
    #     return cpf
    # def validate_nome(self, nome):
    #     if not nome.isalpha():
    #         raise serializers.ValidationError("Não inclua numeros nesse campo")
    #     return nome
    # def validate_rg(self, rg):
    #     if len(rg) != 9:
    #         raise serializers.ValidationError("O RG deve ter 9 digitos")
    #     return rg
    # def validate_celular(self, celular):
    #     if len(celular) < 11:
    #         raise serializers.ValidationError("O celular deve ter 11 digitos")
    #     return celular