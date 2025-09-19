from BCEmbedding import RerankerModel
import logging

logging.basicConfig(level=logging.INFO)

# your query and corresponding passages
query = "input_query"
passages = ["passage_0", "passage_1"]

# construct sentence pairs
sentence_pairs = [[query, passage] for passage in passages]
logging.info(f"Sentence pairs: {sentence_pairs}")

# init reranker model
model = RerankerModel(model_name_or_path="maidalun1020/bce-reranker-base_v1")
logging.info(f"Model initialized: {model}")

# method 0: calculate scores of sentence pairs
scores = model.compute_score(sentence_pairs)
logging.info(f"Scores: {scores}")

# method 1: rerank passages
rerank_results = model.rerank(query, passages)
logging.info(f"Rerank results: {rerank_results}")
