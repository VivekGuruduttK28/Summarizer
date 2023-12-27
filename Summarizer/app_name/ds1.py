from summarizer import Summarizer


from summarizer.sbert import SBertSummarizer
     


def sum2(body):
    model = SBertSummarizer('paraphrase-MiniLM-L6-v2')
    result = model(body, num_sentences=5)
    return(result)