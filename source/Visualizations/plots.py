import json 
from typing import Callable
import pandas as pd
from plotly.utils import PlotlyJSONEncoder
import plotly.express as px

def render_figure(func: Callable):
    # The decorator which could be use to renders a js scirpt for plotly charts
    # It requires that 'func' returns plotly figure object 
    def inner(*args, **kwargs):
        fig = func(*args, **kwargs)
        result = json.dumps(fig, cls=PlotlyJSONEncoder)
        return None if result == "null" else result
    return inner


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


@render_figure
def players_goals_by_team(data_as_dict):
    if not data_as_dict:
        return None
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
    return fig


@render_figure
def player_appearances_by_tournament(data_as_dict):
    if not data_as_dict:
        return None
    data = pd.DataFrame(data_as_dict)

    label = {
    "tournament": "Tournament",
    "number_of_matches": "Number of matches"}

    fig = px.bar(data, labels=label, x="tournament", y="number_of_matches", color="stage", title=None)
    fig.update_yaxes(visible=True, showticklabels=False)
    return fig

