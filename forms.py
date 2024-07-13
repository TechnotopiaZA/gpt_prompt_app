from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class PromptForm(FlaskForm):
    role = SelectField('Role', choices=[
        ('Expert Accountant', 'Expert Accountant'),
        ('Skilled Software Developer', 'Skilled Software Developer'),
        # Add other roles
    ], validators=[DataRequired()])
    needs = StringField('Needs', validators=[DataRequired()])
    task = SelectField('Task', choices=[
        ('Translate', 'Translate'),
        ('Calculate', 'Calculate'),
        # Add other tasks
    ], validators=[DataRequired()])
    details = TextAreaField('Details', validators=[DataRequired()])
    format = SelectField('Format', choices=[
        ('Plain text', 'Plain text'),
        ('HTML', 'HTML'),
        # Add other formats
    ], validators=[DataRequired()])
    submit = SubmitField('Create Prompt')

class SettingsForm(FlaskForm):
    # Add fields for settings
    submit = SubmitField('Save Settings')
