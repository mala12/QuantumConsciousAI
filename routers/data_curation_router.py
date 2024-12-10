from fastapi import APIRouter

router = APIRouter()

@router.get("/data-curation")
def data_curation():
    # Updated author name
    curated_data = {
        "papers": [
            {"title": "Quantum Vortex Math", "author": "N. Tesla", "abstract": "Exploring 3-6-9 patterns."},
            {"title": "Relativity and Consciousness", "author": "A. Einstein", "abstract": "Interplay of time and thought."}
        ]
    }
    return curated_data

