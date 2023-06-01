qtd_bolinhas = gets.to_i
qtd_galhos = gets.to_i

qtd_bolinhas_necessarias = qtd_galhos / 2
diferenca = qtd_bolinhas_necessarias - qtd_bolinhas

if diferenca <= 0 then puts "Amelia tem todas bolinhas!" else puts "Faltam #{diferenca} bolinha(s)" end