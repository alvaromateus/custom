# -*- coding: utf-8 -*-
from openerp import models, fields, api

class assistido(models.Model):
	_name = 'assistido'
	data_cadastro = fields.Date('Data de atendimento', required=True)
	nome = fields.Char('Nome', required=True)
	apelido = fields.Char('Nome Social')
	cpf = fields.Char('CPF')
	rg = fields.Char('RG')
	genero = fields.Selection (
			[('M','Masculino'),('F','Feminino')],
			'Gênero')

	naturalidade = fields.Char('Naturalidade')
	orgao_emissor = fields.Char('Órgão emissor RG')
	data_nascimento = fields.Date('Data de Nascimento')
	estado_civil = fields.Selection (
			[('casado','Casado(a)'),('separado','Separado(a)'), ('solteiro','Solteiro(a)'), ('viuvo','Viúvo(a)'), ('estavel','União Estável'), ('outro','Outro')],
			'Estado Civil')

	escolaridade = fields.Selection (
			[('alfabetizado','Alfabetizado'),('nao_alfabetizado','Não alfabetizado'), ('fundamental_incompleto','Ensino Fundamental Incompleto'),('fundamental_completo','Ensino Fundamental Completo'),('fundamental_cursando','Ensino Fundamental Cursando'), ('medio_incompleto','Ensino Médio Incompleto'),('medio_completo','Ensino Médio Completo'),('medio_cursando','Ensino Médio Cursando'), ('superior_incompleto','Ensino superior Incompleto'),('superior_completo','Ensino Superior Completo'),('superior_cursando','Ensino Superior Cursando'), ('tecnico_incompleto','Ensino Técnico Incompleto'),('tecnico_completo','Ensino Técnico Completo'),('tecnico_cursando','Ensino Técnico Cursando'), ('pos_incompleto','Pos Graduação Incompleto'),('pos_completo','Pos Graduação Completo'),('pos_cursando','Pos Graduação Cursando'), ('outros','Outros')],
			'Escolaridade')

	situacao_empregaticia = fields.Selection (
			[('do_lar','Do lar'), ('trabalhador_carteira','Trabalhador com registro em carteira'), ('servidor','Servidor Público estatutário'), ('comissionado','Servidor Público comissionado'), ('terceirizado','Trabalhador terceirizado'), ('empresario','Empresário (grande ou pequeno)'), ('rural','Trabalhador rural'), ('aposentado','Aposentado'), ('pensionista','Pensionista'), ('aposentado_pensionista','Aposentado e Pensionista'),('autonomo','Autônomo'),('inss','Benefício INSS'), ('contrato','Contrato por tempo determinado'),('diarista','Trabalhador Diarista'), ('desempregado','Desempregado'), ('estudante','Estudante'), ('estagio','Estágio Remunerado'), ('outros','Outros')],'Situação empregatícia')

	profissao = fields.Char('Profissão')
	empregador = fields.Char('Empregador')
	previdencia = fields.Boolean('Contribui com a previdência social?')

	email = fields.Char('Email')

	solicitante = fields.One2many('solicitante', 'assistido_id', string='Solicitantes')

	nome_solicitante = fields.Char('Nome do solicitante',   related='solicitante.nome', store=True)

	atendimento = fields.One2many('atendimento', 'assistido_id', string='Atendimentos')
	atendimento_telefonico = fields.One2many('atendimento_telefonico', 'assistido_id', string='Atendimentos telefônicos')

	quantidade_atendimento = fields.Selection (
		[('0','Nenhuma, esta é a primeira'),
		('1','1 vez'),
		('2','2 vezes'),
		('3','3 vezes'),
		('4','4 vezes'),
		('5','5 vezes ou mais')],'Quantas vezes você utilizou os serviços da Defensoria?')

	canal_conhecimento = fields.Selection (
		[('tv','TV'),
		('radio','Rádio'),
		('internet','Internet'),
		('amigos','Amigos'),
		('parentes','Parentes'),
		('jornais_gratuitos','Jornais gratuitos'),
		('jornais', 'Jornais de grande circulação'),
		('espotanea','Por Demanda Espontânea'),
		('forum','Fórum'),
		('cadeia','Cadeia Pública'),
		('cense','Cense'),
		('delegacia','Delegacia'),
		('cras','CRAS'),
		('creas','CREAS'),
		('politica','Política da Educação'),
		('nucleos','Núcleos de Prática Jurídica'),
		('penitenciaria','Penitenciária Estadual de Ponta Grossa'),
		('outros','Outros')],'Como soube da Defensoria?')

	processo_defensoria = fields.Boolean('Tem processo em andamento na Defensoria?')

	relato = fields.Html('Relato do Caso/ Observações/ Informações adicionais')

	tipo_atendimento_juridico = fields.Selection (
		[('inicial','Inicial'),
		('mandado','Mandado'),
		('intimacao','Intimação'),
		('carta_precatoria','Carta Precatória'),
		('outros','Outros')],'Tipo de atendimento jurídico')

	area_judicial = fields.Selection (
		[('civel','Área Cível'),
		('familia','Área de Família'),
		('infancia','Área de Infância e Juventude'),
		('criminal','Área Criminal'),
		('registro_publico','Área de Registro Públicao'),
		('fazenda','Área de Fazenda e Falências'),
		('juizado_civel','Juizado Especial Cível'),
		('juizado_criminal','Juizado Especial Criminal'),
		('outros','Outros')],'Área Judicial')

	# Campo depreciado, substituído por sede_id, ainda na view
#	sede = fields.Selection (
#		[('ponta_grossa','Ponta Grossa'),
#		('curitiba','Curitiba'),
#		('maringa','Maringá'),
#		('guarapuava','Guarapuava'),
#		('foz','Foz do Iguaçu'),
#		('londrina','Londrina')],'Sede/local onde foi realizado o cadastro')

        sede_id = fields.Many2one('sede', string='Sede/local onde foi realizado o cadastro', required=True)

	sede = fields.Char('Local de Cadastro', related='sede_id.nome',store=True)

	lista_assunto = [('1','Alimentos - Exoneração'),
			('2','Alimentos - Fixação'),
			('3','Alimentos - Oferta'),
			('4','Alimentos - Revisão'),
			('5','Alteração de Regime de Bens'),
			('6','Alvará Judicial'),
			('7','Anulação de Casamento'),
			('8','Cautelar de Busca e Apreensão de Bens'),
			('9','Cautelar de Busca e Apreensão de Menor'),
			('10','Cautelar de Exibição'),
			('11','Cautelar de Produção Antecipada de Provas'),
			('12','Cautelar de Separação de Corpos/Afastamento do Lar'),
			('13','Cautelar de Sequestro'),
			('14','Cautelar Inominada'),
			('15','Declaratória de União Homoafetiva'),
			('16','Descumprimento de Cláusula'),
			('17','Divórcio - Litigioso'),
			('18','Divórcio - Consensual'),
			('19','Divórcio - Conversão de Separação'),
			('20','Embargos à Execução'),
			('21','Embargos de Terceiros'),
			('22','Execução de Alimentos - Penhora'),
			('23','Execução de Alimentos - Prisão'),
			('24','Execução de Sentença'),
			('25','Execução de Título Extrajudicial'),
			('26','Formal de Partilha'),
			('27','Guarda e Responsabilidade'),
			('28','Inexistência de Ato Jurídico'),
			('29','Interdição (Curatela)'),
			('30','Inventário/Arrolamento Sumário'),
			('31','Investigação de Paternidade'),
			('32','Investigação de Paternidade Post Mortem'),
			('33','Negatória de Maternidade'),
			('34','Negatória de Paternidade'),
			('35','Reconhecimento de Maternidade'),
			('36','Reconhecimento de Paternidade'),
			('37','Reconhecimento de Paternidade Post Mortem'),
			('38','Regulamentação de Visitas'),
			('39','Restabelecimento da Sociedade Conjugal'),
			('40','União Estável - Reconhecimento/Dissolução'),
			('41','União Estável - Reconhecimento/Dissolução - Post Mortem'),
			('42','Adoção'),
			('43','Autorização judicial'),
			('44','Destituição do Poder Familiar'),
			('45','Emancipação'),
			('46','Habilitação de Casal para Adoção'),
			('47','Medidas de Proteção à Criança e Adolescente'),
			('48','Perda ou Suspensão ou Restabelecimento do Poder Familiar'),
			('49','Regularização de Registro Civil'),
			('50','Remoção, modificação e dispensa de tutor ou curador'),
			('51','Revisão Judicial de Decisão do Conselho Tutelar'),
			('52','Suprimento de Idade e/ou Consentimento'),
			('53','Tutela'),
			('54','Ação Civil Pública'),
			('55','Ação Coletiva Consumerista'),
			('56','Ação Popular'),
			('57','Ação Rescisória'),
			('58','Adjudicação Compulsória'),
			('59','Alvará Judicial'),
			('60','Anulação de Ato Jurídico'),
			('61','Aposentadoria por Invalidez Acidentária'),
			('62','Auxílio Doença Acidentário'),
			('63','Busca e Apreensão Em Alienação Fiduciária'),
			('64','Cautelar de Arresto '),
			('65','Cautelar de Busca E Apreensão'),
			('66','Cautelar de Exibição'),
			('67','Cautelar de Produção Antecipada de Provas'),
			('68','Cautelar de Sequestro'),
			('69','Cautelar de Sustação de Protesto'),
			('70','Cobrança'),
			('71','Consignação em Pagamento'),
			('72','Cumprimento de Sentença'),
			('73','Declaratória'),
			('74','Demarcatória'),
			('75','Desapropriação'),
			('76','Despejo'),
			('77','Discriminatória'),
			('78','Divisória'),
			('79','Embargos de Terceiro'),
			('80','Embargos à Arrematação'),
			('81','Embargos à Execução'),
			('82','Embargos à Penhora'),
			('83','Execução Contra a Fazenda Pública'),
			('84','Execução de Título Extrajudicial'),
			('85','Execução Fiscal'),
			('86','Falência'),
			('87','Habilitação de Crédito'),
			('88','Imissão na Posse'),
			('89','Indenização (Reparação de Danos)'),
			('90','Inexistência de Ato Jurídico'),
			('91','Insolvência Civil'),
			('92','Interdição (Curatela)'),
			('93','Interdito Proibitório'),
			('94','Internação Compulsória'),
			('95','Inventário/Arrolamento Sumário'),
			('96','Juizados Especiais - Rito Sumaríssimo'),
			('97','Mandado de Segurança'),
			('98','Mandado de Segurança - Medicamentos'),
			('99','Manutenção de Posse'),
			('100','Monitória'),
			('101','Nulidade de Ato Jurídico'),
			('102','Obrigação de Entrega de Coisa'),
			('103','Obrigação de Fazer/Não Fazer'),
			('104','Recuperação Judicial'),
			('105','Reintegração de Posse'),
			('106','Reivindicação de Posse'),
			('107','Repetição do Indébito'),
			('108','Rescisão Contratual'),
			('109','Retificação de Registro Civil'),
			('110','Revisão Contratual'),
			('111','Revisional de Aluguel'),
			('112','Usucapião'),
			('113','Outro (Especificar)')]


	assunto1 = fields.Selection (lista_assunto,'Assunto')
	outro1 = fields.Char('Outro (Espec.)')

	assunto2 = fields.Selection (lista_assunto,'Assunto 2')
	outro2 = fields.Char('Outro (Espec.)')

	deliberacao = fields.Boolean('Atende aos critérios da Deliberação Nº 019/2014 do CSDP?')
	recurso = fields.Boolean('Recurso?')
	orientacao_encaminhamento = fields.Boolean('Orientação e encaminhamento?')

	telefone = fields.One2many('telefone', 'assistido_id', string='Telefones para contato')
	telefone_assistido = fields.Char('Telefone Assistido', related='telefone.telefone',store=True)

	endereco = fields.One2many('endereco', 'assistido_id', string='Endereços')

	membro_familia = fields.One2many('membro_familia', 'assistido_id', string='Membros da família')
	diligencia = fields.One2many('diligencia', 'assistido_id', string='Diligências realizadas')

	count = fields.Integer(compute="_count_membros_familia", string='Número Membros da família', store=True)

	def _get_sum_remuneracao(self):
		remuneracao = self.env['membro_familia'].search([('assistido_id','=', self.id)])        
		self.soma_remuneracao = sum(item.remuneracao for item in remuneracao)
	soma_remuneracao = fields.Float(string="Remuneração total da família", compute='_get_sum_remuneracao')

	# quantidade de membros de família
	def _get_count_remuneracao(self):
		self.count_remuneracao = self.env['membro_familia'].search_count([('assistido_id','=', self.id)])
	count_remuneracao = fields.Char(string="Quantidade de membros na família", compute='_get_count_remuneracao')

	# cálculo de renda per capita (não impresso no sistema)
	def _get_renda_per_capita(self):
		if int(self.count_remuneracao) != 0:
			self.renda_per_capita = (self.soma_remuneracao / int(self.count_remuneracao))
		else:
			self.count_remuneracao == 1
	renda_per_capita = fields.Float(string="Renda Per Capita", compute='_get_renda_per_capita')


	# quantidade de membros da famaília com dedução de 1/2 salário mínimo
	def _get_count_deducao_situacao(self):
		dominio_situacao   = 	[
 				 ('assistido_id','=', self.id), 
				 ('situacao','in', ['deficiente','idoso','egresso','dependente'])				 
				]
		self.count_membros_desconto_meio_salario = self.env['membro_familia'].search_count(dominio_situacao)
	count_membros_desconto_meio_salario = fields.Char(string="Quantidade de membros na família dedutíveis (1/2 salário)", compute='_get_count_deducao_situacao')


	# cálculo da renda com desconto
	def _get_renda_com_desconto(self):
		# exclui itens com situação empregatícia com bpc e estágio da soma
		dominio   = 	[ 
 				 ('assistido_id','=', self.id), 
				 ('situacao_empregaticia','not in', ['bpc','estagio'])				 
				]
		remuneracao = self.env['membro_familia'].search(dominio)        
		self.renda_com_desconto = (sum(item.remuneracao for item in remuneracao)-(int(self.count_membros_desconto_meio_salario))*440)-self.gasto_extra
	renda_com_desconto = fields.Float(string="Renda Familiar com descontos", compute='_get_renda_com_desconto')

	gasto_extra = fields.Float ('Gasto extra')
	descricao_gasto = fields.Char ('Descrição do gasto extra')

	tipo_residencia = fields.Selection (
		[('casa','Casa'),
		('apartamento','Apartamento'),
		('albergue','Moradia coletiva (albergue)'),
		('pensionato','Moradia coletiva (pensionato)'),
		('outro','Outros')],'Tipo de residência')

	situacao_residencia = fields.Selection (
		[('proprio','Próprio'),
		('alugado','Alugado'),
		('ocupado','Ocupado'),
		('penhorado','Penhorado'),
		('cedido','Cedido'),
		('financiado','Financiado'),
		('heranca','Herança'),
		('habitacional','Programa Habitacional'),
		('outros','Outros')],'Situação')

	tipo_construcao = fields.Selection (
		[('madeira','Madeira'),
		('alvenaria','Alvenaria'),
		('mista','Mista')],'Tipo de Construção')

	valor_aluguel_financiamento = fields.Float ('Valor do Aluguel ou Financiamento')

	observacao_residencia = fields.Char('Observação')

	cadastro_unico = fields.Boolean('Possui Cadastro Único?')

	familia_deficiencia = fields.Boolean('Algum membro da família possui deficiência?')

	familia_substancia = fields.Boolean('Algum membro da família utiliza substâncias psicoativas (álcool e/ou outras drogas)?')

	descricao_deficiencia = fields.Char('Observação acerca da deficiência')

	situacao_saude_mental_familia = fields.Char('Situação da saúde mental da família')

	acompanhamento_familia = fields.Char('Em acompanhamento?')

	programa_social = fields.One2many('programa_social', 'assistido_id', string='Programas sociais')

	sus = fields.Boolean('Acesso ao Sistema Único de Saúde?')

	unidade_basica = fields.Char('Unidade Básica de Saúde (referência)')

	usuario_drogas = fields.Boolean('Utilização de substâncias psicoativas (álcool e/ou outras drogas) por algum membro da família?')

	cras = fields.Char('CRAS')

	vinculos_familiares = fields.Char('Vínculos familiares')

	_sql_constraints = [('cpf', 'unique(cpf)', 'Outro assistido já foi cadastrado com este CPF!')]
	_sql_constraints = [('rg', 'unique(rg)', 'Outro assistido já foi cadastrado com este RG!')]

	def name_get(self, cr, uid, ids, context=None):
	    if context is None:
		context = {}
	    if isinstance(ids, (int, long)):
		ids = [ids]

	    res = []
	    for record in self.browse(cr, uid, ids, context=context):
		name = record.nome
		cpf = record.cpf
		if cpf == False:
			cpf = "Sem cadastro"
		else:
			cpf = record.cpf
		res.append((record.id, name + " - CPF: " + str(cpf)))
	    return res

        def _check_cpf(self):
            if self.cpf:
                if not self.validate_cpf(self.cpf):
                    raise Warning(_(u'CPF inválido!'))
            return True

	def validate_cpf(cpf):
	    """Rotina para validação do CPF - Cadastro Nacional
	    de Pessoa Física.
	    :Return: True or False
	    :Parameters:
	      - 'cpf': CPF to be validate.
	    """
	    if not cpf.isdigit():
		cpf = re.sub('[^0-9]', '', cpf)

	    if len(cpf) != 11:
		return False

	    # Pega apenas os 9 primeiros dígitos do CPF e gera os 2 dígitos
	    cpf = map(int, cpf)
	    novo = cpf[:9]

	    while len(novo) < 11:
		r = sum([(len(novo) + 1 - i) * v for i, v in enumerate(novo)]) % 11

		if r > 1:
		    f = 11 - r
		else:
		    f = 0
		novo.append(f)

	    # Se o número gerado coincidir com o número original, é válido
	    if novo == cpf:
		return True
	    return False
