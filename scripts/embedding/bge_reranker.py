from FlagEmbedding import FlagReranker
import logging
import os

# Configure verbose logging
os.environ["FLAGEMBEDDING_LOG_LEVEL"] = (
    "DEBUG"  # Enable debug logging for FlagEmbedding
)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("bge_reranker.log")],
)
logger = logging.getLogger(__name__)

logger.debug("Starting FlagReranker initialization...")
logger.info(
    "Initializing FlagReranker with model 'BAAI/bge-reranker-base' and fp16 enabled"
)
reranker = FlagReranker("BAAI/bge-reranker-base", use_fp16=True)
logger.debug("FlagReranker initialized successfully")

logger.debug("Starting basic query-passage score computation")
logger.info("Computing score for basic query-passage pair")
score = reranker.compute_score(["query", "passage"])
logger.debug(f"Computed raw score: {score}")
logger.info(f"Raw score: {score}")  # -5.65234375

logger.debug("Starting normalized score computation")
logger.info("Computing normalized score for basic query-passage pair")
score = reranker.compute_score(["query", "passage"], normalize=True)
logger.debug(f"Computed normalized score: {score}")
logger.info(f"Normalized score: {score}")  # 0.003497010252573502

logger.debug("Preparing multiple query-passage pairs")
query_pairs = [
    ["what is panda?", "hi"],
    [
        "what is panda?",
        "The giant panda (Ailuropoda melanoleuca), sometimes called a panda bear or simply panda, is a bear species endemic to China.",
    ],
]
logger.debug(f"Query pairs prepared: {query_pairs}")

logger.debug("Starting multiple scores computation")
logger.info("Computing scores for multiple query-passage pairs")
scores = reranker.compute_score(query_pairs)
logger.debug(f"Computed raw scores: {scores}")
logger.info(f"Raw scores: {scores}")  # [-8.1875, 5.26171875]

logger.debug("Starting normalized multiple scores computation")
logger.info("Computing normalized scores for multiple query-passage pairs")
scores = reranker.compute_score(query_pairs, normalize=True)
logger.debug(f"Computed normalized scores: {scores}")
logger.info(
    f"Normalized scores: {scores}"
)  # [0.00027803096387751553, 0.9948403768236574]

logger.debug("All computations completed successfully")
