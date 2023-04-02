from flask_wtf import FlaskForm, Form
from wtforms import SelectField, SubmitField


class DropdownSelectionForm(Form):
    values = SelectField()
    submit = SubmitField("Search")

    def __init__(self, choices: list, title: str) -> None:
        super().__init__()
        self.values.choices = choices
        self.values.label = title
