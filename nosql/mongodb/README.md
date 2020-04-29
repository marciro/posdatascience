

# Atividade da Disciplina de Bancos de dados não relacionais

## MongoDB

### Exercício 1

1. **Adicione outro Peixe e um Hamster com nome Frodo**
	
	`db.pets.insert({name: "Frodo", species: "Peixe"})`
	`db.pets.insert({name: "Frodo", species: "Hamster"})`

2. **Faça uma contagem dos pets na coleção**
	
	`db.pets.find().count()`
	
3. **Retorne apenas um elemento o método prático possível**

	`db.pets.findOne()`

4. **Identifique o ID para o Gato Kilha.**
 
	`db.pets.find({"name":"Kilha"},{"_id":1})`

5. **Faça uma busca pelo ID e traga o Hamster Mike**
   
	`var mike_id = db.pets.find({"name": "Mike","species":"Hamster"},{"_id":1})`
	`db.pets.find(mike_id.next())`

6. **Use o find para trazer todos os Hamsters**

	`db.pets.find({'species':'Hamster'})`

7. **Use o find para listar todos os pets com nome Mike**
	
	`db.pets.find({'name':'Mike'})`
	
8. **Liste apenas o documento que é um Cachorro chamado Mike**

	 `db.pets.find({'name':'Mike', 'species':'Cachorro'})`
	 

### Exercício 2


1. **Liste/Conte todas as pessoas que tem exatamente 99 anos. Você pode usar um count para indicar a quantidade.**

	`db.italians.find({'age':99})`

2. **Identifique quantas pessoas são elegíveis atendimento prioritário(pessoas com mais de 65 anos).**

	`db.italians.find({'age':{'$gte':65}}).count()`

3. **Identifique todos os jovens (pessoas entre 12 a 18 anos).**

	`db.italians.find({'age':{'$lte':18,'$gte':12}},{'_id':1,'firstname':1,'surname':1,'age':1})`

4. **Identifique quantas pessoas tem gatos, quantas tem cachorro e quantas não tem nenhum dos dois.**

   `db.italians.find({'dog':{'$exists':1}}).count()`
   `db.italians.find({'cat':{'$exists':1}}).count()`
   `db.italians.find({'$and':[{'dog':{'$not':{'$exists':1}}},{'cat':{'$not':{'$exists':1}}}]}).count()`
   
5. **Liste/Conte todas as pessoas acima de 60 anos que tenham gato.**
	
	`db.italians.find({'$and':[{'age':{'$gt':60}},{'cat':{'$exists':1}}]}).count()`
	`db.italians.find({'$and':[{'age':{'$gt':60}},{'cat':{'$exists':1}}]},{'_id':1,'firstname':1,'surname':1,'age':1,'cat.name':1})`
	
6. **Liste/Conte todos os jovens com cachorro.**

	`db.italians.find({'$and':[{'age':{'$gte':12,'$lte':18}},{'dog':{'$exists':1}}]}).count()`
	`db.italians.find({'$and':[{'age':{'$gte':12,'$lte':18}},{'dog':{'$exists':1}}]},{'_id':1,'firstname':1,'surname':1,'age':1,'dog.name':1})`


7. **Utilizando o $where, liste todas as pessoas que tem gato e cachorro.**
	
   `db.italians.find({'$and':[{'$where':'this.cat != null'},{'$where':'this.dog != null'}]},{'_id':1,'firstname':1,'surname':1,'age':1,'dog.name':1,'cat.name':1})`


8. **Liste todas as pessoas mais novas que seus respectivos gatos.**
   
   `db.italians.find({'$and':[{'age':{'$lte':12}},{'cat':{'$exists':1}}]},{'_id':1,'firstname':1,'surname':1,'age':1,'cat.name':1})`

9. **Liste as pessoas que tem o mesmo nome que seu bichano (gatou ou cachorro).**

	`db.italians.aggregate([{$match: {'cat':{$exists:1}}}, {$project: {"firstname":1,"cat.name":1,"isEqual":{"$cmp":["$firstname","$cat.name"]}}}, {$match: {"isEqual":0}}])`
	`db.italians.aggregate([{$match: {'dog':{$exists:1}}}, {$project: {"firstname":1,"dog.name":1,"isEqual":{"$cmp":["$firstname","$dog.name"]}}}, {$match: {"isEqual":0}}])`
	
10. **Projete apenas o nome e sobrenome das pessoas com tipo de sangue de fator RH negativo.**
	`db.italians.find({"bloodType":{"$eq":"B-"}},{"firstname":1,"surname":1,"bloodType":1})`

11.**Projete apenas os animais dos italianos. Devem ser listados os animais com nome e idade. Não mostre o identificado do mongo (ObjectId).**
	
	`db.italians.find({},{"cat.name":1,"cat.age":1,"dog.name":1,"dog.age":1,"_id":0})`

12. **Quais são as 5 pessoas mais velhas com sobrenome Rossi?**

	`db.italians.find({"surname":{"$eq":"Rossi"}},{"_id":0,"firstname":1,"surname":1,"age":1}).limit(5).sort({"age":-1})`

13. **Crie um italiano que tenha um leão como animal de estimação. Associe um nome e idade ao bichano.**

	`db.italians.insert({"firstname":"Luciano","surname":"Pavarotti","username":"pavaluci32","age":68,"email":"luciano.pavarotti@uol.com.br","bloodType":"A+","id_num":"733732696169","lion":{"name":"Simba","age":17}}`

14. **Infelizmente o Leão comeu o italiano. Remova essa pessoa usando o Id.**
	
	`db.italians.remove({"_id":ObjectId("5ea87e38a30ed235b0a545c3")})`
	
15. **Passou um ano. Atualize a idade de todos os italianos e dos bichanos em 1.**

	`db.italians.update({}, {$inc: { age: 1}}, { multi: true })`
	`db.italians.update({"cat":{"$exists":1}}, {$inc: { "cat.age": 1}}, { multi: true })`
	`db.italians.update({"dog":{"$exists":1}}, {$inc: { "dog.age": 1}}, { multi: true })`

16. **O Corona Vírus chegou na Itália e misteriosamente atingiu pessoas somente com gatos e de 66 anos. Remova esses italianos.**
	
	`db.italians.remove({"$and":[{"age":66},{"cat":{"$exists":1}}]})`

17. **Utilizando o framework agregate, liste apenas as pessoas com nomes iguais a sua respectiva mãe e que tenha gato ou cachorro.**

	`db.italians.aggregate([ {'$match': { mother: { $exists: 1} }}, {'$match': { $or: [ {cat: {$exists: 1}}, {dog: {$exists: 1}}]}},{'$project': { "firstname": 1, "mother": 1, "isEqual": { "$cmp": ["$firstname","$mother.firstname"]} }}, {'$match': {"isEqual": 0}} ])`

18. **Utilizando aggregate framework, faça uma lista de nomes única de nomes. Faça isso usando apenas o primeiro nome.**
	
	`db.italians.aggregate([{$group:{ _id:"$firstname"}}])`
	

19. **Agora faça a mesma lista do item acima, considerando nome completo.**

	`db.italians.aggregate([{$group: {_id: {"$concat": ["$firstname", " ", "$surname"]}}}])`
	
20. **Procure pessoas que gosta de Banana ou Maçã, tenham cachorro ou gato, mais de 20 e menos de 60 anos.**

	`db.italians.find({ $and:[{"age": { "$gt": 20, "$lt": 60 }}, {$or: [{ dog: {$exists: true}}, {cat: {$exists: true}}]}, { $or: [ {favFruits: ["Banana"]}, {favFruits: ["Maçã"]}]} ]})`
	
	
### Exercício 3

1. **Liste as ações com profit acima de 0.5 (limite a 10 o resultado).**
	
	`db.stocks.find( { "Profit Margin": { "$gt": 0.5 } },{"_id":0,"Ticker":1,"Country":1, "Profit Margin":1} ).limit(10)`

2. **Liste as ações com perdas (limite a 10 novamente).**
	
	`db.stocks.find( { "Profit Margin": { "$lt": 0 } },{"_id":0,"Ticker":1,"Country":1, "Profit Margin":1}).limit(10)`
	
3. **Liste as 10 ações mais rentáveis.**
	
	`db.stocks.find({},{"_id":0,"Ticker":1,"Country":1,"Profit Margin":1}).limit(10).sort({"Profit Margin":-1})`
	
4. **Qual foi o setor mais rentável?**
	`db.stocks.find({},{"Sector":1}).limit(1).sort({"Profit Margin":-1})`
	
5. **Ordene as ações pelo profit e usando um cursor, liste as ações.**
	`var stockCursor = db.stocks.find({"Profit Margin":{"$exists":1}},{"_id":0,"Ticker":1,"Country":1,"Profit Margin":1}).sort({ "Profit Margin": -1 });stockCursor.forEach(function(x){print(JSON.stringify(x, null, 2));});`

6. **Renomeie o campo “Profit Margin” para apenas “profit”.**
	`db.stocks.update({"Profit Margin": {$exists: true}}, {$rename:{"Profit Margin":"profit"}}, false, true)`
	
7. **Agora liste apenas a empresa e seu respectivo resultado.**
	`db.stocks.find({}, {"Ticker":1,"Company": 1,"profit": 1})` 
	
8. **Analise as ações. É uma bola de cristal na sua mão... Quais as três ações você investiria?
	`db.stocks.find({},{"_id":1,"Ticker":1,"Country":1,"Profit Margin":1}).limit(3).sort({"Profit Margin":-1})`
	
	`{ "_id" : ObjectId("52853800bb1177ca391c1801"), "Ticker" : "AADR", "Country" : "USA" }`
	`{ "_id" : ObjectId("52853800bb1177ca391c1802"), "Ticker" : "AAIT", "Country" : "USA" }`
	`{ "_id" : ObjectId("52853800bb1177ca391c1800"), "Ticker" : "AA", "Country" : "USA" }`
	
9. **Liste as ações agrupadas por setor**
	`db.stocks.aggregate([{ "$sort" : { "Sector" : 1}},{'$project': { "Sector": 1, "Ticker": 1,"Company": 1}}])`
	