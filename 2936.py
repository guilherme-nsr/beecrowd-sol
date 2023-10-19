PORCAO_CURUPIRA_EM_GRAMAS = 300
PORCAO_BOITATA_EM_GRAMAS = 1500
PORCAO_BOTO_EM_GRAMAS = 600
PORCAO_MAPINGUARI_EM_GRAMAS = 1000
PORCAO_IARA_EM_GRAMAS = 150
PORCAO_DONA_CHICA_EM_GRAMAS = 225

qtd_porcoes_curupira = int(input())
qtd_porcoes_boitata = int(input())
qtd_porcoes_boto = int(input())
qtd_porcoes_mapinguari = int(input())
qtd_porcoes_iara = int(input())
qtd_porcoes_dona_chica = 1

qtd_total_em_gramas = PORCAO_CURUPIRA_EM_GRAMAS*qtd_porcoes_curupira \
					+ PORCAO_BOITATA_EM_GRAMAS*qtd_porcoes_boitata \
					+ PORCAO_BOTO_EM_GRAMAS*qtd_porcoes_boto \
					+ PORCAO_MAPINGUARI_EM_GRAMAS*qtd_porcoes_mapinguari \
					+ PORCAO_IARA_EM_GRAMAS*qtd_porcoes_iara \
					+ PORCAO_DONA_CHICA_EM_GRAMAS*qtd_porcoes_dona_chica

print(qtd_total_em_gramas)