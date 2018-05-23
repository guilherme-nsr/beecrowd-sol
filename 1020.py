dias = int(input())

idade_anos = dias // 365
idade_meses = (dias % 365) // 30
idade_dias = dias - ((idade_anos*365) + (idade_meses*30))

print("%d ano(s)" % (idade_anos))
print("%d mes(es)" % (idade_meses))
print("%d dia(s)" % (idade_dias))
