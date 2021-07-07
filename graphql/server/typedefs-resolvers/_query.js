const { gql} = require('apollo-server-express')

const typeDefs = gql`
type Query{
    people: [person]
    person(name:String!): person
    movies: [movie]
    movie(title:String!): movie
}
`
module.exports = typeDefs