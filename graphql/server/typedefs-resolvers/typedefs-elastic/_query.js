const { gql} = require('apollo-server')

const typeDefs = `
type Query{
    people: [person]
    person(name:String!): person
    movies: [movie]
    movie(title:String!): movie
    elastic(review:String!): [es]
}
`
module.exports = typeDefs