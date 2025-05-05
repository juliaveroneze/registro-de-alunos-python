velocidade = 66 #velocidade do carro
local_carro = 102 #kmtragem local que está na estrada

radar_1 = 60
local_1 = 100 #kmtragem onde está o primeiro radar
radar_range = 1 #distancia onde o radar pega
carro_multado = velocidade > radar_1

local_radar_menor = local_1 - radar_range #99
local_radar_maior =local_1 + radar_range #101
status_passagem_carro = local_carro >= local_radar_maior
 
if status_passagem_carro:
    print('passou pelo radar')
else:
    print('você não passou pelo radar')

if carro_multado:
    print('estava acima da velocidade')
else:
    print('de acordo com a velocidade')

