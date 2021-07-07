const { gql} = require('apollo-server-express')

const typeDefs = `
type Mutation{
    postPerson(id:ID!, name:String!, born:Int!): person
}
`
module.exports = typeDefs