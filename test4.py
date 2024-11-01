from mrjob.job import MRJob
from math import log

class TermFrequency(MRJob):
    def mapper(self, _, line):
        doc_id, content = line.split("\t", 1)  
        words = content.split()
        total_words = len(words)
        
        for word in words:
            yield (word, doc_id), 1 / total_words 

    def reducer(self, key, values):
        yield key, sum(values)  


class DocumentFrequency(MRJob):
    def mapper(self, key, tf_value):
        term, doc_id = key
        yield term, doc_id  

    def reducer(self, term, doc_ids):
        unique_docs = set(doc_ids)
        yield term, len(unique_docs)  


class TFIDF(MRJob):
    def configure_args(self):
        super(TFIDF, self).configure_args()
        self.add_file_arg('--df')  
        self.add_passthru_arg('--num_docs', type=int, default=1, help='Total number of documents')

    def load_df(self):
        self.df = {}
        with open(self.options.df, 'r') as f:
            for line in f:
                term, count = line.strip().split("\t")
                self.df[term] = int(count)

    def mapper_init(self):
        self.load_df()

    def mapper(self, key, tf_value):
        term, doc_id = key
        tf = tf_value

        if term in self.df:
            df = self.df[term]
            idf = log(self.options.num_docs / (1 + df))  
            tf_idf = tf * idf
            yield (term, doc_id), tf_idf