


class search:
    """indexing 기법은 아래의 elasticsearch 기법 활용.
    score(q,d)  =  
                queryNorm(q)  
            · coord(q,d)    
            · ∑ (           
                    tf(t in d)   
                · idf(t)²      
                · t.getBoost() 
                · norm(t,d)    
                ) (t in q)    
                    
    score(q,d) is the relevance score of document d for query q.


    queryNorm(q) is the query normalization factor (new).


    coord(q,d) is the coordination factor (new).


    The sum of the weights for each term t in the query q for document d.


    tf(t in d) is the term frequency for term t in document d.


    idf(t) is the inverse document frequency for term t.


    t.getBoost() is the boost that has been applied to the query (new).


    norm(t,d) is the field-length norm, combined with the index-time field-level boost, if any. (new).

"""

    def __init__(self):
        self.map = np.array([])
    
    def queryNorm(self, query):
        """Query Normalization method
        
            Args:
                query is the varables which compare to document
        """
        return self.tf_idf(query) / math.sqrt(sum(self.idf(query)*self.idf(query)))
    
    def coord(self, query,doc):
        """coord is used to reward documents that contain a higher percentage of the query terms

            Args:
                query is the sentences which compare to doc
                doc is the webpage's html content

            exmaple)
                query: quick brown fox
                doc with fox -> score: 1.5 * 1 / 3 = 0.5
                doc with quick fox -> score: 3.0 * 2 / 3 = 2.0
                doc with quick brown fox -> score: 4.5 * 3 / 3 = 4.5
        """
        if not query:
            return
        if not doc:
            return
        if not isinstance(query, str):
            return
        if not isinstance(doc, str):
            return
            
        words_number = len(query.split())
        for word in words_number:
            doc.count(word)

    def tf_idf(self,query):
        pass
    def tf(self,query):
        pass
    def idf(self):
        pass