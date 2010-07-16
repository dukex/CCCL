#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import sys
import urllib
import urllib2
import time
import datetime


if __name__ == '__main__':
	parser = argparse.ArgumentParser(
		description='Speak with correios via Command Line.')

    # add the arguments
	parser.add_argument(
   		'msg', nargs="?",
		help='Mensagem a ser enviada' 
		)
	parser.add_argument(
   		'--tipo', required=True, nargs=1, choices='SEDC',
		help='O que deseja Registrar:'
			 '[S]ugestao;'
 			 '[E]logio;'
			 '[D]uvida;'
			 '[C]ritica' 
		)
	parser.add_argument(
   		'--nome', required=True, nargs=1,
		help='Seu nome ou nome do rementente'
		)
	parser.add_argument(
   		'--cep', required=True, nargs=1,
		help='Seu Cep sem traço e.g. 00000123'
		)

	parser.add_argument('--endereco',  required=True)
	parser.add_argument('--numero',  required=True)
	parser.add_argument('--complemento', default=" ")
	parser.add_argument('--bairro', required=True)
	parser.add_argument('--cidade', required=True)
	parser.add_argument('--uf', required=True)
	parser.add_argument('--pais', default="Brasil")
	parser.add_argument('--ddd', required=True)
	parser.add_argument('--tel', required=True)
	parser.add_argument('--email', required=True)
	
    # parse the command line
	args = parser.parse_args()
	post = {
			'Browser' 	  	   : 'DukeBot (v1 Python)',
			'Server_Name' 	   : 'www.correios.com.br',
			'Remote_Name' 	   : '127.0.0.1&',
	 		'Data'		  	   : '{ts '+datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S")+'}', 
	        'origem'	   	   : '0',
	        'cod_fale_com'	   : '0',
	        'usuario_rede'	   : 'O próprio',
	        'tipo'	  	  	   :  args.tipo[0],
	        'OptCPFCNPJ'  	   : 'CPF',
	        'Nome'		       : args.nome[0],
	        'CEP'		  	   : args.cep[0],
	        'Endereco'	  	   : args.endereco[0],
	        'Numero'      	   : args.numero[0],
	        'Complemento' 	   : args.complemento[0],
	        'Bairro'      	   : args.bairro[0],
	        'Cidade'      	   : args.cidade[0],
	        'ufremetente' 	   : args.uf[0],
	        'pais'		  	   : args.pais[0],
	        'DDD'		  	   : args.ddd[0],
	        'Telefone'    	   : args.tel[0],
	        'E_Mail'     	   : args.email[0],
	        'paisdestinatario' : args.pais[0],
	        'avisorecebimento' : 'Não',
	        'msg'			   : args.msg[0],
	        'Submit'		   : '+Enviar+'
			}
	
	url = 'http://www.correios.com.br/servicos/falecomoscorreios/Grava_Solicitacao.cfm'
	data = urllib.urlencode(post)
	#req = urllib2.Request(url, data)
	#response = urllib2.urlopen(req)
	#the_page = response.read()
	#/html/body/div/table/tbody/tr/td[2]/div/div/div/table/tbody/tr/td[2]/div/div/div[4]/table/tbody/tr/td/table/tbody/tr[3]/td/div/dl/dd/p
	
	print data