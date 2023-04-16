import json 
import pandas as pd
from plotly.utils import PlotlyJSONEncoder
import plotly.express as px
import plotly.graph_objects as go


class PieChartPX:

    def __init__(self, data: dict, colors: list, title: str):
        self.colors = colors
        self.title = title
        self.data = data

    def _transform_data_to_df(self):
        return pd.DataFrame(self.data)
    
    def build_figure(self):
        df = self._transform_data_to_df()
        fig = px.pie(df, values=df.columns[1], names=df.columns[0], title=self.title)
        fig.update_traces(marker=dict(colors=self.colors))
        return fig

    def render(self):
        fig = self.build_figure()
        return json.dumps(fig, cls=PlotlyJSONEncoder)


def render_players_goals_by_team(data_as_dict):
    data = pd.DataFrame(data_as_dict)
    title=None
    labels = {
        "number_of_goals": "Number of goals",
        "team": ""
    }    
    fig = px.bar(
        data, 
        y='number_of_goals', 
        x='team', 
        title=title,
        labels=labels
        )
    fig.update_yaxes(visible=False, showticklabels=True)
    return json.dumps(fig, cls=PlotlyJSONEncoder)


def render_player_appearances_by_tournament(data_as_dict):
    data = pd.DataFrame(data_as_dict)

    label = {
    "tournament": "Tournament",
    "number_of_matches": "Number of matches"}

    fig = px.bar(data, labels=label, x="tournament", y="number_of_matches", color="stage", title=None)
    fig.update_yaxes(visible=True, showticklabels=False)
    return json.dumps(fig, cls=PlotlyJSONEncoder)


def render_goals_by_tournament(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['year'], y=data["goals"],
                        mode='markers',
                        name='Scored goals'))

    fig.add_trace(go.Scatter(x=data['year'], y=data["matches"],
                        mode='markers',
                        name='Matches played'))
    return json.dumps(fig, cls=PlotlyJSONEncoder)



def show_stadiums_on_map(data):
    data = pd.DataFrame(data)

    fig = px.scatter_mapbox(
        data, 
        lat="coordinates_lat", lon="coordinates_long", 
        color="number_of_games",
        size="number_of_games",
        hover_name="stadium_name", 
        hover_data=["city_name", "country_name"],
        zoom=3)

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return json.dumps(fig, cls=PlotlyJSONEncoder)
