
def calcular_investimento(capital_inicial, taxa_anual, meses):
    taxa_mensal = (taxa_anual/100) / 12
    resultado_bruto = capital_inicial*(1+taxa_mensal)**meses
    lucro_bruto = resultado_bruto-capital_inicial
    if meses <= 6: aliquota_ir = 0.225
    elif meses <= 12:
        aliquota_ir = 0.20
    elif meses <= 24:
        aliquota_ir = 0.175
    else:
        aliquota_ir = 0.15
    lucro_liquido = lucro_bruto- (lucro_bruto*aliquota_ir)
    valor_final = capital_inicial+lucro_liquido
    return valor_final

resultado_teste = calcular_investimento(1000, 10.75, 12)
print(resultado_teste)

Teste de Sincronização com repositório local
