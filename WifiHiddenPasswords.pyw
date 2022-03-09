import os

ssids = [rede.split(':')[1].strip() for rede in os.popen('netsh wlan show profiles') if "Todos" in rede]
passwords = [ [info for info in os.popen("netsh wlan show profiles \"%s\" key=clear"%name).readlines() if 'da Chave' in info][0] .split(':')[1].strip() for name in ssids]

capture = open("wifi_senhas.txt",'a')
capture.write("senhas capturadas:\n\n")

for redes in range(len(ssids)):
	net = ssids[redes]+' = '+passwords[redes]+'\n'
	capture.write(net)
capture.close()