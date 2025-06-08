from fastapi import FastAPI, Query
from app.matcher import NameMatcher

app = FastAPI()
names = [line.strip() for line in open("data/names.txt")]
matcher = NameMatcher(names)

@app.get("/match")
def match_name(name: str, top_k: int = 5):
    top_matches = matcher.get_matches(name, top_k)
    best_match = top_matches[0]
    return {
        "input": name,
        "best_match": {"name": best_match[0], "score": best_match[1]},
        "top_matches": [{"name": n, "score": s} for n, s in top_matches]
    }
