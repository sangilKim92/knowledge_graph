const peopleCypher = `
MATCH (n:Person) 
RETURN n
LIMIT 2000
`
const personCypher = `
MATCH (n:Person{name:$name}) 
RETURN n 
LIMIT 25
`

const moviesCypher = `
MATCH (n:Movie) 
RETURN n 
LIMIT 25
`

const movieCypher = `
MATCH(n:Movie{title:args.title})
RETURN n
LIMIT 25
`

module.exports = {
    peopleCypher : peopleCypher,
    personCypher : personCypher,
    movieCypher : movieCypher,
    moviesCypher: moviesCypher
}