# Atividade da Disciplina de Bancos de dados não relacionais

## HBase

### Exercício 1

**Agora, de dentro da imagem faça os sefuintes procedimentos:**
1. **Crie a tabela com 2 famílias de colunas:**
	**a. personal-data**
	**b. professional-data**

	`hbase(main):001:0> create 'italians','personal-data','professional-data'`
	`Created table italians`
	`Took 2.2690 seconds`
	`=> Hbase::Table - italians`


2. **Importe o arquivo via linha de comando**
	
	`root@a219fb2df5b0:/# hbase shell tmp/italians.txt`



### Exercício 2

**Agora execute as seguintes operações:**


1. **Adicione mais 2 italianos mantendo adicionando informações como data de nascimento nas informações pessoais e um atributo de anos de experiência nas informações profissionais.**
	
	`hbase(main):003:0> count 'italians'`
	`10 row(s)`
	
	*Sendo a quantidade de linhas de 10 registros, somando mais 1 nos próximos números.  Essa operação de count em termos de uso em produção não deve ser feito, pois é custosa e pode levar muito tempo para uma simples inserção de registros e somente funciona se a chave for um número sequencial, e está sendo utilizada somente para fins do exercício.*
	
	`put 'italians', '11', 'personal-data:name', 'Luciano Pavarotti'`  
	`put 'italians', '11', 'personal-data:city', 'Modena'`  
	`put 'italians', '11', 'personal-data:birthdate', '12/10/1935'`  
	`put 'italians', '11', 'professional-data:role', 'Tenor'`  
	`put 'italians', '11', 'professional-data:salary', '9999999'`  
	`put 'italians', '11', 'professional-data:work_experience', '30'`  
	  
	`put 'italians', '12', 'personal-data:name', 'Andrea Bocelli'`  
	`put 'italians', '12', 'personal-data:city', 'Lajatico'`  
	`put 'italians', '12', 'personal-data:birthdate', '22/09/1958'`  
	`put 'italians', '12', 'professional-data:role', 'Cantor'`  
	`put 'italians', '12', 'professional-data:salary', '888888'`  
	`put 'italians', '12', 'professional-data:work_experience', '20'`  

2. **Adicione o controle de 5 versões na tabela de dados pessoais.**
	
	`hbase(main):018:0> alter 'italians', NAME => 'personal-data', VERSIONS => 5´
	`Updating all regions with the new schema...´
	`1/1 regions updated.´
	`Done.´
	`Took 2.5064 seconds´
	
3. **Faça 5 alterações em um dos italianos.**

	`put 'italians', '12', 'personal-data:name', 'Placido Domigo'`
	`put 'italians', '12', 'personal-data:city', 'Madrid'`
	`put 'italians', '12', 'personal-data:birthdate', '21/01/1941'`
	`put 'italians', '12', 'professional-data:salary', '9999991'`
	`put 'italians', '12', 'professional-data:work_experience', '28'`

4. **Com o operador get, verifique como o HBase armazenou o histórico.**
	
	`get 'italians', '12', {COLUMN => 'personal-data:name', VERSIONS => 5}`
	
	`hbase(main):025:0> get 'italians', '12', {COLUMN => 'personal-data:name', VERSIONS => 5}`
	`COLUMN                                      CELL`
	`personal-data:name                         timestamp=1588342332489, value=Placido Domigo`
	`personal-data:name                         timestamp=1588341656043, value=Andrea Bocelli`
	`1 row(s)`
	`Took 0.0349 seconds`
	
	`get 'italians', '12', {COLUMN => 'personal-data:city', VERSIONS => 5}`
	`get 'italians', '12', {COLUMN => 'personal-data:birthdate', VERSIONS => 5}`
	`get 'italians', '12', {COLUMN => 'professional-data:salary', VERSIONS => 5}`
	`get 'italians', '12', {COLUMN => 'professional-data:work_experience', VERSIONS => 5}`

5. **Utilize o scan para mostrar apenas o nome e profissão dos italianos.**

	`scan 'italians', { COLUMNS => ['personal-data:name', 'professional-data:role'] }`
	
6. **Apague os italianos com row id ímpar.**
	
	`deleteall 'italians', '1'`
	`deleteall 'italians', '3'`
	`deleteall 'italians', '5'`
	`deleteall 'italians', '7'`
	`deleteall 'italians', '9'`
	`deleteall 'italians', '11'`

7. **Crie um contador de idade 55 para o italiano de row id 5.**
	
	`put 'italians', '5', 'personal-data:name', 'Zucchero Fornaciari'
	`put 'italians', '5', 'personal-data:city', 'Roncocesi' 	
	`put 'italians', '5', 'personal-data:birthdate', '29/04/1965'
	`incr 'italians','5', 'personal-data:age', 55
	
	`hbase(main):002:0> put 'italians', '5', 'personal-data:name', 'Zucchero Fornaciari'`
	`Took 0.0439 seconds`
	`hbase(main):003:0> put 'italians', '5', 'personal-data:city', 'Roncocesi' Display all 608 possibilities? (y or n)`
	`hbase(main):003:0> put 'italians', '5', 'personal-data:city', 'Roncocesi'`
	`Took 0.0093 seconds`
	`hbase(main):004:0> put 'italians', '5', 'personal-data:city', 'Roncocesi'`
	`Took 0.0074 seconds`
	`hbase(main):005:0> put 'italians', '5', 'personal-data:birthdate', '29/04/1965'`
	`Took 0.0118 seconds`
	`hbase(main):006:0> incr 'italians','5', 'personal-data:age', 55`
	`COUNTER VALUE = 55`
	`Took 0.0376 seconds`
	`hbase(main):007:0>`
	
8. **Incremente a idade do italiano em 1.**
	
	`incr 'italians', '5', 'personal-data:age'`
	
	`hbase(main):007:0> incr 'italians', '5', 'personal-data:age'`
	`COUNTER VALUE = 56`
	`Took 0.0102 seconds`

