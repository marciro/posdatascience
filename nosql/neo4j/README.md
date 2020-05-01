# Atividade da Disciplina de Bancos de dados não relacionais

## Neo4j

### Exercício 1

**Exercise 1.1: Retrieve all nodes from the database.**

	`match(n) return (n)`

**Exercise 1.2: Examine the data model for the graph.**

*Conforme visualizado na ferramenta:*
![Exercise_1_2](images/exercicio_1_2.png)
	
**Exercise 1.3: Retrieve all Person nodes.**

`match(p:Person) return (p)`

**Exercise 1.4: Retrieve all Movie nodes.**

`match(m:Movie) return (m)`


### Exercício 2

**Exercise 2.1: Retrieve all movies that were released in a specific year.**

`match(m:Movie{released: 2009}) return (m)`

**Exercise 2.2: View the retrieved results as a table.**

*Conforme visualizado na ferramenta:*
![Exercise_2_2](images/exercicio_2_2.png)

**Exercise 2.3: Query the database for all property keys.**

`match(a) UNWIND keys(a) AS key RETURN collect(distinct key)`

**Exercise 2.4: Retrieve all Movies released in a specific year, returning their titles.**

`match(m{released:1999}) return (m.title)`

**Exercise 2.5: Display title, released, and tagline values for every Movie node in the graph.**

`match(m:Movie) return m.title, m.released, m.tagline`

**Exercise 2.6: Display more user-friendly headers in the table.**

`match(m:Movie) return m.title as Título, m.released as Lançamento, m.tagline as Slogan`


### Exercício 3

**Exercise 3.1: Display the schema of the database.**

`call db.schema.visualization()`

*Conforme visualizado na ferramenta:*
![Exercise_3_1](images/exercicio_3_1.png)

**Exercise 3.2: Retrieve all people who wrote the movie Speed Racer.**

`match (p:Person)-[:WROTE]->(m:Movie{title:'Speed Racer'}) return p`

**Exercise 3.3: Retrieve all movies that are connected to the person,Tom Hanks.**

`match (m:Movie)<--(:Person{name:'Tom Hanks'}) return m`

**Exercise 3.4: Retrieve information about the relationships Tom Hanks had with the set of movies retrieved earlier.**

`match (m:Movie)<-[r]-(:Person{name:'Tom Hanks'}) return distinct type(r)`

**Exercise 3.5: Retrieve information about the roles that Tom Hanks acted in.**

`match (m:Movie)<-[:ACTED_IN]-(:Person{name:'Tom Hanks'}) return m.title, m.role`


### Exercício 4


**Exercise 4.1: Retrieve all movies that Tom Cruise acted in.**

`match (p:Person)-[:ACTED_IN]->(m:Movie) where p.name = 'Tom Cruise' return m`

**Exercise 4.2: Retrieve all people that were born in the 70’s.**

`match (p:Person) where  p.born >= 1970 and p.born < 1980 return p`

**Exercise 4.3: Retrieve the actors who acted in the movie The Matrix who were born after 1960.**

**Exercise 4.4: Retrieve all movies by testing the node label and a property.**

**Exercise 4.5: Retrieve all people that wrote movies by testing the relationship between two nodes.**

**Exercise 4.6: Retrieve all people in the graph that do not have a property.**
