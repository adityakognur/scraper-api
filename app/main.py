from fastapi import FastAPI
from pydantic import BaseModel
from app.scraper import Scraper

app = FastAPI()

class Review(BaseModel):
    title: str
    body: str
    rating: int
    reviewer: str

@app.get("/api/reviews")
def get_reviews(url: str):
    try:
        scraper = Scraper(url)
        scraper.start_browser()
        reviews = scraper.extract_reviews()
        scraper.close_browser()

        reviews_count = len(reviews)
        return {"reviews_count": reviews_count, "reviews": reviews}

    except Exception as e:
        return {"detail": f"Error: {e}"}
