const { gql} = require('apollo-server')

const typeDefs = `
type Query{
    people: [person]
    person(name:String!): person
    movies: [movie]
    movie(title:String!): movie
    elastic(review:String!): [es]
    neo4j(cypher:String!):[neo4j]
}
`
module.exports = typeDefs