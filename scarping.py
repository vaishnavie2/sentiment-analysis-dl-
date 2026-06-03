import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager


# =========================================================
# STEP 1 : CHROME DRIVER SETUP
# =========================================================

def get_driver():

    opts = Options()

    # IF WEBSITE BLOCKS YOU, COMMENT THIS
    # opts.add_argument("--headless")

    opts.add_argument("--start-maximized")

    opts.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0 Safari/537.36"
    )

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=opts
    )

    driver.set_page_load_timeout(300)

    return driver


# =========================================================
# STEP 2 : SCRAPE REVIEWS
# =========================================================

def scrape_reviews(movie, target_reviews=100):

    driver = get_driver()

    data = []

    print(f"\n Scraping: {movie['name']}")

    try:

        driver.get(movie['url'])

        time.sleep(8)

        # SCROLL MANY TIMES
        for i in range(20):

            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            time.sleep(2)

        # GET REVIEWS
        reviews = driver.find_elements(
            By.XPATH,
            "//div[contains(@class,'body-text')]"
        )

        print("Reviews Found:", len(reviews))

        # EXTRACT TEXT
        for r in reviews[:target_reviews]:

            txt = r.text.strip()

            if len(txt) > 5:

                data.append({

                    "Movie": movie['name'],

                    "Genre": movie['genre'],

                    "Year": movie['year'],

                    "Review": txt

                })

    except Exception as e:

        print("❌ Error:", e)

    finally:

        driver.quit()

    return data


# =========================================================
# STEP 3 : BOLLYWOOD MOVIES (2024-2026)
# =========================================================

movies_list = [

    # =====================================================
    # ROMANTIC / COMEDY
    # =====================================================

    {
        "genre": "Romantic-Comedy",
        "name": "Laapataa Ladies",
        "year": 2024,
        "url": "https://letterboxd.com/film/lost-ladies/reviews/"
    },

    {
        "genre": "Romantic-Comedy",
        "name": "Crew",
        "year": 2024,
        "url": "https://letterboxd.com/film/crew-2024/reviews/"
    },

    {
        "genre": "Romantic-Comedy",
        "name": "Teri Baaton Mein Aisa Uljha Jiya",
        "year": 2024,
        "url": "https://letterboxd.com/film/teri-baaton-mein-aisa-uljha-jiya/reviews/"
    },

    {
        "genre": "Romantic-Comedy",
        "name": "Saiyaara",
        "year": 2025,
        "url": "https://letterboxd.com/film/saiyaara/reviews/"
    },

    # =====================================================
    # HORROR
    # =====================================================

    {
        "genre": "Horror",
        "name": "Stree 2",
        "year": 2024,
        "url": "https://letterboxd.com/film/stree-2/reviews/"
    },

    {
        "genre": "Horror",
        "name": "Munjya",
        "year": 2024,
        "url": "https://letterboxd.com/film/munjya/reviews/"
    },

    {
        "genre": "Horror",
        "name": "Bhool Bhulaiyaa 3",
        "year": 2024,
        "url": "https://letterboxd.com/film/bhool-bhulaiyaa-3/reviews/"
    },

    {
        "genre": "Horror",
        "name": "Bhediya",
        "year": 2024,
        "url": "https://letterboxd.com/film/bhediya/reviews/"
    },

    # =====================================================
    # ACTION
    # =====================================================

    {
        "genre": "Action",
        "name": "Kill",
        "year": 2024,
        "url": "https://letterboxd.com/film/kill-2023/reviews/"
    },

    {
        "genre": "Action",
        "name": "Fighter",
        "year": 2024,
        "url": "https://letterboxd.com/film/fighter-2024/reviews/"
    },

    {
        "genre": "Action",
        "name": "Deva",
        "year": 2025,
        "url": "https://letterboxd.com/film/deva-2025/reviews/"
    },

    {
        "genre": "Action",
        "name": "War 2",
        "year": 2025,
        "url": "https://letterboxd.com/film/war-2/reviews/"
    },

    # =====================================================
    # SCI-FI
    # =====================================================

    {
        "genre": "Sci-Fi",
        "name": "Kalki 2898 AD",
        "year": 2024,
        "url": "https://letterboxd.com/film/kalki-2898-ad/reviews/"
    },

    {
        "genre": "Sci-Fi",
        "name": "Brahmastra",
        "year": 2024,
        "url": "https://letterboxd.com/film/brahmastra-part-one-shiva/reviews/"
    },

    {
        "genre": "Sci-Fi",
        "name": "2.0",
        "year": 2024,
        "url": "https://letterboxd.com/film/2-0/reviews/"
    },

    {
        "genre": "Sci-Fi",
        "name": "Krrish 4",
        "year": 2026,
        "url": "https://letterboxd.com/film/krrish-4/reviews/"
    }

]


# =========================================================
# STEP 4 : EXECUTION
# =========================================================

if __name__ == "__main__":

    final_dataset = []

    for movie in movies_list:

        reviews = scrape_reviews(
            movie,
            target_reviews=100
        )

        final_dataset.extend(reviews)

    # CREATE DATAFRAME
    df = pd.DataFrame(final_dataset)

    print("\n==============================")
    print("TOTAL REVIEWS COLLECTED:", len(df))
    print("==============================")

    print(df.head())

    print(df.shape)

    # SAVE CSV
    df.to_csv(
        "bollywood_movies_reviews_2024_2026.csv",
        index=False
    )

    print("\n DATASET SAVED SUCCESSFULLY")
