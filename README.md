# World Cup Dashboards

This is a web application inspired by some fantastic services like [Sofascore](https://sofascore.com), [Flashscore](https://flashscore.com). It presents some football statistics about World Cup tournaments between years 1930 and 2022 (on the day of writing these words, this is every tournament that happened).

## Dataset
The core and most important thing in this project is historical data about football matches and players. The dataset originally comes from another [Github repository](https://github.com/jfjelstul/worldcup). Thanks to Joshua C. Fjelstul who performed the data scrapping and published a dataset under a CC-BY-SA 4.0 license.

## Tech Stack
**Database**: MySQL 8.0  
**Backend**: Python Flask framework (to see all libraries used, please check a *requirements.txt* file)  
**Frontend**: HTML Jinja Templates, CSS, JS  
**DevOps**: Docker


## Live demo
*Not available yet*

## Screenshots
![Matches list](demo/assets/matches_list.png)
<br>
![Match list](demo/assets/match_details.png)
<br>
![Player details](demo/assets/player_details.png)
<br>
![Team details](demo/assets/team_details.png)
<br>
![Team details](demo/assets/team_details(2).png)
<br>

## How to run?

To run the project you should have a [Docker](https://www.docker.com/) already installed on your machine.

First, to build the project, run the following command in a docker console:

``docker compose up --build``

The docker will use docker-compose.ylm and two dockerfiles stored in this repository. First dockerfile (in the root directory of the project) is used for installing Python and its all required dependencies and finally for running flask server.

The second dockerfile (which is stored in the *./db* directory) is used for creating and building a database - it pulls MySQL image from a dockerhub, then runs a script to create tables, stored procedures and functions.

After building the project you need to run a data import. The command below performs an easy ETL process - it runs another Python script to transform and import data from csv files into a database. It needs an ID of the container created in the previous step, you can get it by running ``docker ps`` in a console.

``docker exec <container_id> python DataImporting/files/run_data_import.py``
