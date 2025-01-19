from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_scrape_reviews():
    url = "https://www.amazon.com/i9-13900H-Processor-GeForce-Display-ANV15-51-99DR/dp/B0D8JXHZTH/ref=sr_1_1_sspa?_encoding=UTF8&content-id=amzn1.sym.860dbf94-9f09-4ada-8615-32eb5ada253a&dib=eyJ2IjoiMSJ9.k70XAEMU3DcsVwDpL5Grpp2prRZjzsRxjMNSMWbh7TPVzoQiClU7PMof7fSPM27HatJuS-Qw2Go1NBpzFhIPhaF3wyad4e1F8ztvntMv4qxWRPFr2heABfZwJtP_jnGWF8jR1IH2-d3lbVZ7RvqEJDpEJgDSgW1ov04MfA0pXDVYxR4VwYKk7DkYA_LU4_9Vdwtw_ND6zys1SRA2wFbkRWDxYznFXdkP6KtpHwX_zMjCt0FREtiZD1rZCXddUfqCJbI1iAUvcwNFj9bt0064Ec9PXHNi1r0rZtUZ87VfVlU.rNa7AoCMAl8PJ_5fOD-A0V4BS3oVlOZKR4Yw4iISkls&dib_tag=se&keywords=gaming&pd_rd_r=4bc991ef-5613-4871-a294-51288c266da0&pd_rd_w=B7tPt&pd_rd_wg=IN2oc&pf_rd_p=860dbf94-9f09-4ada-8615-32eb5ada253a&pf_rd_r=FNSEV6EYMP4PASQJ2QQY&qid=1736688461&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1#customerReviews"
    response = client.get(f"/api/reviews?url={url}")
    assert response.status_code == 200
    data = response.json()
    assert "reviews_count" in data
    assert "reviews" in data
    assert isinstance(data["reviews"], list)
    assert all("title" in review for review in data["reviews"])
    assert all("body" in review for review in data["reviews"])
    assert all("rating" in review for review in data["reviews"])
    assert all("reviewer" in review for review in data["reviews"])
