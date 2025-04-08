from flask_wtf import FlaskForm
from wtforms import BooleanField, RadioField, IntegerField, SubmitField
from wtforms.validators import InputRequired
from wtforms.widgets import NumberInput
from wtforms import SelectField, FloatField, BooleanField, IntegerField



class FieldsRequiredForm(FlaskForm):
    """Require all fields to have content. This works around the bug that WTForms radio
    fields don't honor the `DataRequired` or `InputRequired` validators.
    """
    class Meta:
        def render_field(self, field, render_kw):
            if field.type == "_Option":
                render_kw.setdefault("required", True)
            return super().render_field(field, render_kw)


class DiagnoseForm(FieldsRequiredForm):
    gender = SelectField('Gender', choices=[(0, 'Female'), (1, 'Male')])  # Store as '0' or '1'

    age = IntegerField('Age',
                       widget = NumberInput(min=1, max=140),
                       validators=[InputRequired()])
        
    hypertension = BooleanField('Hypertension')  
    heart_disease = BooleanField('Heart Disease')       
    smoking_history_choices = [
        (0, 'No Info'),
        (1, 'current'),
        (2, 'ever'),
        (3, 'former'),
        (4, 'never')
    ]
    smoking_history = SelectField('Smoking History', choices=smoking_history_choices, coerce=int)
    bmi = FloatField('BMI')  
    HbA1c_level = FloatField('HbA1c Level')  
    blood_glucose_level = IntegerField('Blood Glucose Level')  
    submit = SubmitField('Get result')
