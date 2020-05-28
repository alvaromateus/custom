# -*- coding: utf-8 -*-
from openerp import models, fields, api

class atendimento(models.Model):
	_name = 'atendimento'
	data_cadastro = fields.Date('Data de Cadastro', required=True)
	
	numero_processo = fields.Char('Número do Processo')
	assistido_id = fields.Many2one('assistido', string='Assistido', required=True)


	realizado = fields.Selection (
		[('realizado','Realizado'),
		('pendente','Pendente')],'Situação')


# campo depreciado, substituido pelo campo area
#	area_atendimento = fields.Selection (
#		[('1_vara','1 Vara Criminal'),
#		('2_vara','2 Vara Criminal'),
#		('3_vara','3 Vara Criminal'),
#		('4_vara','4 Vara Criminal'),
#		('execucao','Execução Penal'),
#		('infancia','Infância Cível'),
#		('infancia_infracional','Infância Infracional'),
#		('cam','Centro de Atendimento Multidisciplinar'),
#		('outro','Outros')],'Área do Atendimento')

	area = fields.Selection (
		[('criminal','Criminal'),
		('execucao','Execução Penal'),

		('infancia','Infância e Juventude'),
		('trabalhista','Direito Trabalhista'),
		('extra_judicial','Extrajudicial'),
		('civel_fazenda','Cível / Fazenda Pública'),
		('familia','Família'),
		('violencia_domestica','Violência Doméstica'),
		('curadoria','Curadoria Especial'),

		('cam','Centro de Atendimento Multidisciplinar')],'Área do Atendimento', required=True)

	vara = fields.Selection (
		[('1','1ª Vara'),
		('2','2ª Vara'),

		('3','3ª Vara'),

		('4','4ª Vara'),
		('5','5ª Vara'),
		('6','6ª Vara'),
		('7','7ª Vara'),
		('8','8ª Vara'),

		('9','9ª Vara'),
		('10','10ª Vara'),
		('execucao','Vara de Execução')],'Vara Judicial')

#
	assunto = fields.Char('Assunto')

#	def _get_procedimentos(self):
#		if self.area == 'Criminal':
#			return [('value1', 'String 1'), ('value2', 'String 2')]
#		if self.area == 'Execução Penal':
#			return [('1', '1'), ('2', '2')]
#
#	procedimento = fields.Selection(_get_procedimentos,'Procedimento realizado')

        sede_id = fields.Many2one('sede', string='Sede/local onde foi realizado o cadastro', required=True)

	sede = fields.Char('Local de Cadastro', related='sede_id.nome',store=True)

        procedimento_id = fields.Many2one('procedimento', string='Procedimento', domain=[('area','=','criminal')] )

	# campo depreciado, substituido pelo campo sede_id
#	sede = fields.Selection (
#		[('ponta_grossa','Ponta Grossa'),
#		('curitiba','Curitiba'),
#		('maringa','Maringá'),
#		('guarapuava','Guarapuava'),
#		('foz','Foz do Iguaçu'),
#		('londrina','Londrina')],'Sede/local onde foi realizado o cadastro')

        defensor_id = fields.Many2one('defensor', string='Defensor Público Responsável', required=True)

	# campo depreciado, substituido pelo campo defensor_id
#	defensor = fields.Selection (
#		[('ana','Dr. Ricardo Padoim'),
#		('ricardo','Dra. Monia Serafim'),
#		('monia','Dra. Ana Paula'),
#		('julio','Dr. Júlio Salem'),
#		('nao_atendido','Não atendido por Defenso Público')],'Defensor Público')

	atendido_por = fields.Selection (
		[('nao_atendido','Não atendido por Defensor Público'),
		('defensor','Atendido por Defensor Público'),
		('sem_advogado','Sem Advogado'),
		('advogado_dativo','Advogado Dativo'),
		('negativa','Negativa de Atendimento'),
		('advogado_particular','Advogado Particular')], 'Situação de Representação Processual', required=True)

	relato = fields.Html('Resumo do caso')

        solicitante_id = fields.Many2one('solicitante', string='Solicitante')

	cpf = fields.Char('CPF Assistido', related='assistido_id.cpf',store=True)
	rg = fields.Char('RG Assistido',   related='assistido_id.rg', store=True)

	email = fields.Char('Email Assistido', related='assistido_id.email',store=True)

	telefone = fields.Char('Telefone(s) Assistido', related='assistido_id.telefone_assistido',store=True)

	parte_colidente = fields.Char('Parte Colidente')

	cpf_colidente = fields.Char('CPF da Parte Colidente')

	endereco_parte_colidente = fields.One2many('endereco', 'parte_colidente_id', string='Endereço da Parte Colidente')

	nome_solicitante = fields.Char('Nome do solicitante',   related='solicitante_id.nome')
	nome_assistido = fields.Char('Nome do assistido',   related='assistido_id.nome')

	negativa_txt = fields.Html('Denegacao', default='NEGATIVA DE ATENDIMENTO JURÍDICO<br><br>Senhor(a)')
	negativa_txt2 = fields.Html('Denegacao', default='<br>A Defensoria Pública do Estado do Paraná (DPPR) é a instituição responsável por prestar assistência jurídica aos necessitados, nos termos do art. 134 da Constituição Federal. No entanto, como a criação da Defensoria é recente e o número de Defensores Públicos na comarca é pequeno, ainda não é possível prestar atendimento jurídico em todas as áreas de atuação.<br>A Administração Superior da DPPR determinou que, em Ponta Grossa, serão atendidas, por enquanto, as seguintes áreas: Criminal, Infância e Juventude, Execução Penal e Medidas Alternativas.<br>As resoluções que estabelecem as áreas de atuação da Defensoria  Pública do Paraná podem ser consultadas no seguinte endereço eletrônico: www.defensoriapublica.pr.def.br.<br>Assim sendo, informamos que a sua pretensão não se enquadra nas áreas atualmente atendidas pela Defensoria, motivo pelo qual não será possível a prestação da assistência jurídica pleiteada.<br>Informamos, ainda, que caso discorde da negativa de atendimento, poderá requerer a revisão de sua pretensão, preenchendo o formulário abaixo.<br><br>RECURSO: _________________________________________________________________________________________'+  '<br><br>___________________________________________________________________________________________________<br>'+
'Recebi uma cópia da negativa')
