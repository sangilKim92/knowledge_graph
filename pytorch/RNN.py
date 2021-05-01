class RNNClassifier(nn.Module):
    
    def __init__(self,
                input_size,
                word_vec_dim,
                hidden_size,
                n_classes,
                n_layers=4,
                dropout=.3):
        super(RNNClassifier).__init()
        self.input_size = input_size
        self.word_vec_dim = word_vec_dim
        self.hidden_size = hidden_size
        self.n_classes = n_classes
        self.n_layers = n_layers
        self.dropout = dropout
        
        self.emb = nn.Embedding(input_size, word_vec_dim)
        self.rnn = nn.LSTM(input_size = word_vec_dim,
                          hidden_size = hidden_size,
                          num_layers = n_layers,
                          dropout = dropout,
                          batch_first = True,
                          bidirectional = True)
        self.geneator = nn.Linear(hidden_size * 2, n_classes)
        
        self.activation = nn.LogSoftmax(dim=-1)
        
    def forward(self, x):
        x = self.emb(x)
        
        x, _ = self.rnn(x)
        
        y = self.activation(self.generator(x[:,-1]))
        
        return y