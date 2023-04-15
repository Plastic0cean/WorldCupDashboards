from dataclasses import dataclass
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd 
from Db.DbConnection import conn 


@dataclass
class Coordinates:
    latitude: float
    longitude: float

    @classmethod
    def from_dms(cls, latitude, longitude):
        def convert_dms_to_decimals(coordinate):
            deg, minutes, seconds, direction =  re.split('[°\′\″]', coordinate)
            return (float(deg) + float(minutes)/60 + float(seconds)/(60*60)) * (-1 if direction in ['W', 'S'] else 1)
        
        latitude_dec = convert_dms_to_decimals(latitude)
        longitude_dec = convert_dms_to_decimals(longitude)
        return cls(latitude_dec, longitude_dec)


def read_stadiums_dataset(conn):
    with conn:
        stadiums = pd.read_sql("SELECT * FROM stadiums", con=conn.conn)
    stadiums["latitude"] = None
    stadiums["longitude"] = None
    return stadiums


def scrape_coordinates(url: str):
    page_content = requests.get(url).content
    soup = BeautifulSoup(page_content, 'html.parser')

    coordinates = Coordinates.from_dms(
        soup.find("span", class_="latitude").text,
        soup.find("span", class_="longitude").text)
    return coordinates


def write_coordinates_in_df(stadiums: pd.DataFrame):
    for index, row in stadiums.iterrows():
        try:
            url = row.stadium_wikipedia_link
            coordinates = scrape_coordinates(url)

            stadiums.latitude.iloc[index] = coordinates.latitude
            stadiums.longitude.iloc[index] = coordinates.longitude
        except:
            continue    
    return stadiums


def update_coordinates_in_db(stadiums: pd.DataFrame, conn):
    for _, row in stadiums.iterrows():
        if row.latitude and row.longitude:
            update_stmt = f"""UPDATE stadiums SET coordinates_lat = {row.latitude}, coordinates_long = {row.longitude} WHERE stadium_id = '{row.stadium_id}'"""
            with conn:
                conn.execute(update_stmt)


def main():
    stadiums = read_stadiums_dataset(conn)
    stadiums = write_coordinates_in_df(stadiums)
    update_coordinates_in_db(stadiums, conn)


if __name__ == "__main__":
    main()