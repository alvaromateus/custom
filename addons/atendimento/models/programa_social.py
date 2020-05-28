# -*- coding: utf-8 -*-
from openerp import models, fields

class programa_social(models.Model):
	_name = 'programa_social'
	tipo = fields.Selection (
		[('bpc', 'BPC'),
		('carteira_idoso', 'Carteira do idoso'),
		('bolsa_familia', 'Bolsa Família'),
		('pro_jovem', 'Pro Jovem'),
		('energia_social', 'Tarifa social energia elétrica/agua'),
		('minha_casa', 'Minha Casa, Minha Vida'),
		('leite_criancas', 'Leite das Crianças'),
		('prolar', 'Prolar/Cohapar'),
		('outro', 'Outro')])
	valor = fields.Float ('Valor')
        assistido_id = fields.Many2one('assistido', string='Assistido')
