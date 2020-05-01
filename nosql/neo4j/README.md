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

**Exercise 2.4: Retrieve all Movies released in a specific year, returning their titles.**

**Exercise 2.5: Display title, released, and tagline values for every Movie node in the graph.**

**Exercise 2.6: Display more user-friendly headers in the table.**

