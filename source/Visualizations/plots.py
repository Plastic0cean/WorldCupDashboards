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


class VisualisationsRendere:

    def __init__(self, figure) -> None:
        self.figure = figure

    def render(self):
        return json.dumps(self.figure, cls=PlotlyJSONEncoder)