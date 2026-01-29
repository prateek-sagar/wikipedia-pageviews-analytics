from dotenv import load_dotenv # type: ignore
import os
from src.ingestion.gathering import get_data
from datetime import date
from src.common.utils import read_data_and_apply_schema, provide_spark_engine
from datetime import date, datetime, timedelta
from src.transformation.cleaning import cleaning
import uuid

load_dotenv()

def run():
    print("Hello from wikipedia-pageview-analytics!")

    engine = provide_spark_engine()
    
    start_str = "2023010100"
    
    start_dt = datetime.strptime(start_str, "%Y%m%d%H")

    WEEK_HOURS = 24 * 7

    today_dt = datetime.combine(date.today(), datetime.min.time())

    # a piece of code that stop runs when data get fetched upto today from the start day but it regularly
    # compare previous extracted data and then get the data for the following three views:
    # data extracted weekly so there must be atleast 7 days gap between
    while start_dt < today_dt:
    
        end_dt = start_dt + timedelta(hours=WEEK_HOURS)
        

        if end_dt > today_dt:
            break

        start = start_dt.strftime("%Y%m%d%H")
        end = end_dt.strftime("%Y%m%d%H")
        
        #gathering
        #input time start and end
        #output data
        #functions to perform
        run = datetime.now().strftime('%I_%M') + str(uuid.uuid4())

        data = get_data(start, end)   

        if (not data):
            raise RuntimeError(f"Not Getting the data from {start} to {end} ")
        
        #collect the evidence
        
        #function to save the data in the lakehouse
        
        # set the data as per schema and convert it into the dataframe
        df = read_data_and_apply_schema(data, engine)

        #cleaning
        #input dataframe
        #output dataframe
        #functions to perform
        #collect the evidence
        run_id_for_cleaning = datetime.now().strftime('%I_%M') + str(uuid.uuid4())
        df, evidence = cleaning(df, engine)

        #casting
        #input dataframe
        #output dataframe
        #functions to perform
        #collect the evidence

        #enriching
        #input dataframe
        #output dataframe
        #functions to perform
        #collect the evidence

        #aggregating
        #input dataframe
        #output dataframe
        #functions to perform
        #collect the evidence

        #loading
        #input dataframe
        #output bool of success or failure to go to the next window
        #functions to perform
        #collect the evidence
        
        start_dt = end_dt



if __name__ == "__main__":
    run()
