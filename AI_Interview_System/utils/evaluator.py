from sentence_transformers import (
    SentenceTransformer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)

model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

def evaluate_answer(
    user_answer,
    correct_answer
):

    emb1 = model.encode(user_answer)

    emb2 = model.encode(correct_answer)

    similarity = cosine_similarity(
        [emb1],
        [emb2]
    )[0][0]

    return round(similarity * 100, 2)