import json 
from typing import Callable
import pandas as pd
from plotly.utils import PlotlyJSONEncoder
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "ggplot2"


def render_figure(func: Callable):
    # The decorator which is used to render a js scirpt for plotly visualisations.
    # It requires that "func" returns plotly figure object.
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

    def _transform_data(self):
        return pd.DataFrame(self.data)
    
    def build_figure(self):
        df = self._transform_data()
        fig = px.pie(df, values=df.columns[1], names=df.columns[0], title=self.title, hole=0.4)
        fig.update_traces(marker=dict(colors=px.colors.diverging.balance))
        fig.update_traces(hoverinfo="percent", textinfo="value", textfont_size=14, pull=0.02)
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
    fig = px.treemap(
        data, 
        values="number_of_goals", 
        names="team", 
        title=title,
        labels=labels
        )
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


def render_goals_by_tournament(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data["year"], y=data["goals"],
                        mode="lines+markers",
                        name="Goals scored"))

    fig.add_trace(go.Scatter(x=data["year"], y=data["matches"],
                        mode="lines+markers",
                        name="Matches played"))
    fig.update_layout(margin=dict(l=10, r=10, t=10, b=10))
    fig.update_yaxes(visible=False, showticklabels=False)
    fig.update_xaxes(nticks=5)
    fig.data[0].line.color = "#171C42"
    fig.data[1].line.color = "#0B66BD"
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


@render_figure
def starter_or_substitute(data):
    if not data:
        return None
    data = pd.DataFrame(data)
    trace = go.Pie(labels=data["starer_or_sub"], values=data["number_of_matches"], textinfo="value", hole=0.4)
    fig = go.Figure(data=[trace])
    return fig


@render_figure
def overall_minutes_played(data):
    trace = go.Pie(
    labels=["Playing", "Bench"], 
    values=[data["minutes_played"][0], data["minutes_on_bench"][0]],
    textinfo="value", hole=0.4)
    fig = go.Figure(data=[trace])
    return fig


@render_figure
def team_goals_by_opponent(data):
    data = pd.DataFrame(data)
    labels = {"opponent_name": "", "number_of_goals": ""}
    fig = px.bar(data, labels=labels, x="opponent_name", y="number_of_goals", color_discrete_sequence=px.colors.diverging.balance)
    fig.update_yaxes(visible=False, showticklabels=False)
    fig.update_layout(margin=dict(l=10, r=10, t=10, b=10))
    return fig

@render_figure
def team_goals_by_tournament(data):
    data = pd.DataFrame(data)
    fig = px.pie(data, names="tournament_name", values="number_of_goals", hole=0.5, color_discrete_sequence=px.colors.diverging.balance)
    fig.update_traces(hoverinfo="percent", textinfo="value", textfont_size=14, pull=0.02)
    fig.update_layout(margin=dict(l=10, r=10, t=10, b=10))
    return fig


@render_figure
def players_with_most_minutes(data):
    data = pd.DataFrame(data)
    fig = px.treemap(
        data, 
        path=["player_name"], 
        values="minutes_played",
        color="minutes_played",
        color_discrete_sequence=px.colors.diverging.balance)
    fig.update_layout(coloraxis_showscale=False)
    return fig


@render_figure
def all_matches_by_team(data):
    data = pd.DataFrame(data)
    wins = data.query("win == '1'")
    loses = data.query("lose == '1'")
    fig = go.Figure()

    fig.add_trace(go.Bar(x=wins.match_id, y=wins.goal_differential,
                    base=0,
                    marker_color="green",
                    name="win",
                    hovertext=[s for s in wins.score],
                    hoverinfo="text",
                    text=[match for match in wins.opponent_name] 
                    ))

    fig.add_trace(go.Bar(x=loses.match_id, y=loses.goal_differential.apply(abs),
                    base=[int(diff) for diff in loses.goal_differential],
                    marker_color="crimson",
                    name="lose",
                    hovertext=[f"Score: {s}" for s in loses.score],
                    hoverinfo="text",
                    text=[match for match in loses.opponent_name]))
    fig.update_xaxes(categoryorder="array", categoryarray=data.match_id, visible=False, showticklabels=False)
    fig.update_yaxes(visible=False, showticklabels=False)
    fig.update_layout(
        margin=dict(l=15, r=15, t=15, b=15), 
        plot_bgcolor="rgb(246, 246, 247)")
    return fig

@render_figure
def goals_by_minute_hist(data: pd.DataFrame):
    fig = px.histogram(data, x="minute", color_discrete_sequence=px.colors.diverging.balance)
    fig.update_layout(bargap=0.2)
    fig.layout["xaxis"].title = dict()
    fig.layout["yaxis"].title = dict()
    fig.update_yaxes(visible=False, showticklabels=False)
    fig.update_layout(margin=dict(l=10, r=10, t=10, b=10))
    return fig

@render_figure
def goals_difference_by_team_bubble(data: pd.DataFrame):
    data["size"] = data["goals_difference"] + abs(data.goals_difference.min())
    fig = px.scatter(data, y="goals_for", x="goals_against", size="size", color="team_name", color_discrete_sequence=px.colors.diverging.balance)
    fig.update_yaxes(visible=False, showticklabels=False)
    fig.update_xaxes(visible=False, showticklabels=False)
    fig.update_layout(margin=dict(l=10, r=10, t=10, b=10))
    return fig