import json 
import pandas as pd
from plotly.utils import PlotlyJSONEncoder
import plotly.express as px


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