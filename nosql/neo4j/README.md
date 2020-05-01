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

**Exercise 3.2: Retrieve all people who wrote the movie Speed Racer.**

**Exercise 3.3: Retrieve all movies that are connected to the person,Tom Hanks.**

**Exercise 3.4: Retrieve information about the relationships Tom Hanks had with the set of movies retrieved earlier.**

**Exercise 3.5: Retrieve information about the roles that Tom Hanks acted in.**


