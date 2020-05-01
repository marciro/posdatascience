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


1. **Adicione mais 2 italianos mantendo adicionando informações como data de nascimento nas informações pessoais e um atributo de anos deexperiência nas informações profissionais.**
2. **Adicione o controle de 5 versões na tabela de dados pessoais.**
3. **Faça 5 alterações em um dos italianos.**
4. **Com o operador get, verifique como o HBase armazenou o histórico.**
5. **Utilize o scan para mostrar apenas o nome e profissão dos italianos.**
6. **Apague os italianos com row id ímpar.**
7. **Crie um contador de idade 55 para o italiano de row id 5.**
8. **Incremente a idade do italiano em 1.**


