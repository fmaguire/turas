#!/usr/bin/env python3

from flask_wtf import Form
import os
import wtforms
from wtforms import validators

class NotRequiredIf(validators.DataRequired):
    """
    A custom validator modified from
    http://stackoverflow.com/questions/8463209/how-to-make-a-field-conditionally-optional-in-wtforms
    that makes a field required IFF another field is set
    """

    def __init__(self, other_field_name, *args, **kwargs):
        self.other_field_name = other_field_name
        super(NotRequiredIf, self).__init__(*args, **kwargs)

    def __call__(self, form, field):
        other_field = form._fields.get(self.other_field_name)
        if other_field is None:
            raise Exception('no field named "{}" in form'.format(self.other_field_name))
        if not bool(other_field.data):
            super(NotRequiredIf, self).__call__(form, field)

class LocationForm(Form):
    """
    Form to input conference guest locations
    """
    meeting_name = wtforms.StringField('meeting_name',
                                       validators=[validators.DataRequired(message="Must provide a name")])


    opt_message = "Only one of text form locations or file upload containing locations is required"
    locations = wtforms.TextAreaField('locations',
                                        validators=[NotRequiredIf("file_locations", message=opt_message)])
    file_locations = wtforms.FileField('file_locations',
                                       validators=[NotRequiredIf('locations',
                                                                 message=opt_message)])


def upload_file(request):
    """
    Handle file upload
    """
    form = LocationForm(request.POST)
    data = request.FILES[form.file_locations.data].read()
    open(os.path.join(UPLOAD_PATH, form.file_locations.data), 'w').write(data)

