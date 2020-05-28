# -*- coding: utf-8 -*-
from openerp import models, fields

class endereco(models.Model):
	_name = 'endereco'
	rua = fields.Char('Rua/Avenida', required=True)
	numero = fields.Char('Numero', required=True)
	complemento = fields.Char('Complemento')
	cep = fields.Char('CEP')
	bairro = fields.Char('Bairro')
	cidade = fields.Char('Cidade')
	estado = fields.Selection (
		[('AC', 'Acre'),
		('AL', 'Alagoas'),
		('AP', 'Amapá'),
		('AM', 'Amazonas'),
		('BA', 'Bahia'),
		('CE', 'Ceará'),
		('DF', 'Distrito Federal'),
		('ES', 'Espírito Santo'),
		('GO', 'Goiás'),
		('MA', 'Maranhão'),
		('MT', 'Mato Grosso'),
		('MS', 'Mato Grosso do Sul'),
		('MG', 'Minas Gerais'),
		('PA', 'Pará'),
		('PB', 'Paraíba'),
		('PR', 'Paraná'),
		('PE', 'Pernambuco'),
		('PI', 'Piauí'),
		('RJ', 'Rio de Janeiro'),
		('RN', 'Rio Grande do Norte'),
		('RS', 'Rio Grande do Sul'),
		('RO', 'Rondônia'),
		('RR', 'Roraima'),
		('SC', 'Santa Catarina'),
		('SP', 'São Paulo'),
		('SE', 'Sergipe'),
		('TO', 'Tocantins')])
	tipo = fields.Selection ([('domiciliar','Domiciliar'), ('trabalho','Trabalho'), ('outro','Outro')])
        assistido_id = fields.Many2one('assistido', string='Assistido') 
        solicitante_id = fields.Many2one('solicitante', string='Solicitante')
        parte_colidente_id = fields.Many2one('atendimento', string='Endereço da Parte Colidente')
