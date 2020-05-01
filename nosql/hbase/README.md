# Atividade da Disciplina de Bancos de dados não relacionais

## HBase'

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



### Exercício 1
**Agora execute as seguintes operações:**


1. **Adicione mais 2 italianos mantendo adicionando informações como data de nascimento nas informações pessoais e um atributo de anos de experiência nas informações profissionais.**
	
	`hbase(main):003:0> count 'italians'`
	`10 row(s)`
	
	*Sendo a quantidade de linhas de 10 registros, somando mais 1 nos próximos números
	*Essa operação de count em termos de uso em produção não deve ser feito, pois é custosa e pode levar muito tempo para uma simples inserção de registros
	*e somente funciona se a chave for um número sequencial, e está sendo utilizada somente para fins do exercício.
	
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
3. **Faça 5 alterações em um dos italianos.**
4. **Com o operador get, verifique como o HBase armazenou o histórico.**
5. **Utilize o scan para mostrar apenas o nome e profissão dos italianos.**
6. **Apague os italianos com row id ímpar.**
7. **Crie um contador de idade 55 para o italiano de row id 5.**
8. **Incremente a idade do italiano em 1.**


