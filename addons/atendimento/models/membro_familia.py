# -*- coding: utf-8 -*-
from openerp import models, fields

class membro_familia(models.Model):
	_name = 'membro_familia'
	nome = fields.Char('Nome', required=True)
	data_nascimento = fields.Date('Data de Nascimento')

	situacao = fields.Selection (
		[('geral','Geral'),
		('deficiente','Deficiente'),
		('idoso','Idoso'),
		('egresso','Egresso Sis. Prisional'),
		('dependente','Dependente')],
		'Situação')

	grau_parentesco = fields.Selection (
		[('esposo','Esposo(a)'),
		('companheiro','Companheiro(a)'),
		('filho','Filho(a)'),
		('pai','Pai'),
		('mae','Mãe'),
		('enteado','Enteado(a)'),
		('tio','Tio(a)'),
		('irmao','Irmão(ã)'),
		('avo','Avô'),
		('avo','Avó'),
		('amigo','Amigo(a)'),
		('padrasto','Padrasto'),
		('madastra','Madastra'),
		('assistido','Assistido(a)'),
		('outro','Outros')],
		'Grau de parentesco')

	escolaridade = fields.Selection (
		[('alfabetizado','Alfabetizado'),('nao_alfabetizado','Não alfabetizado'), ('fundamental_incompleto','Ensino Fundamental Incompleto'),('fundamental_completo','Ensino Fundamental Completo'),('fundamental_cursando','Ensino Fundamental Cursando'), ('medio_incompleto','Ensino Médio Incompleto'),('medio_completo','Ensino Médio Completo'),('medio_cursando','Ensino Médio Cursando'), ('superior_incompleto','Ensino superior Incompleto'),('superior_completo','Ensino Superior Completo'),('superior_cursando','Ensino Superior Cursando'), ('tecnico_incompleto','Ensino Técnico Incompleto'),('tecnico_completo','Ensino Técnico Completo'),('tecnico_cursando','Ensino Técnico Cursando'),('pos_incompleto','Pos Graduação Incompleto'),('pos_completo','Pos Graduação Completo'),('pos_cursando','Pos Graduação Cursando'), ('outros','Outros')],
		'Escolaridade')

	situacao_empregaticia = fields.Selection (
		[('do_lar','Do lar'), ('trabalhador_carteira','Trabalhador com registro em carteira'), ('servidor','Servidor Público estatutário'), ('comissionado','Servidor Público comissionado'), ('terceirizado','Trabalhador terceirizado'), ('empresario','Empresário (grande ou pequeno)'), ('rural','Trabalhador rural'), ('aposentado','Aposentado'), ('pensionista','Pensionista'), ('aposentado_pensionista','Aposentado e Pensionista'),('autonomo','Autônomo'),('inss','Benefício INSS'), ('contrato','Contrato por tempo determinado'),('diarista','Trabalhador Diarista'), ('desempregado','Desempregado'),('desempregado_seguro','Desempregado (Recebendo Seguro)'), ('estudante','Estudante'), ('estagio','Estágio Remunerado'),('bpc','Benefício Assistencial ao idoso e à Pessoa com Deficiência (BPC)'), ('outros','Outros')],'Situação empregatícia')

	remuneracao = fields.Float ('Remuneração Líquida')

        assistido_id = fields.Many2one('assistido', string='Assistido')
