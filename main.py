from dotenv import load_dotenv
import os
load_dotenv()
from src.ingestion import get_data


def main():
    print("Hello from wikipedia-pageview-analytics!")
    print(os.getenv("API_URL"))
    data = get_data()
    print(data)



if __name__ == "__main__":
    main()
