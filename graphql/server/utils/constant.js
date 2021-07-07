const constants = {
    ELASTIC_SEARCH:{
        enumSearchOptions = {
            isSearchNone:"isSearchNone",
            isSearchFuzzy:"isSearchFuzzy",
            isSearchExactMatch:"isSearchExactMatch",
            isSearchProximity:"isSearchProximity"
        },
        statusRange={
            min:10,
            max:500
        },
        maxEditDistanceConfig = 4,
        maxFuzzyConfig = 'auto'
    },
    NEO_NUM:[],
    QL_NUM:[]
}
module.exports = constants