import uuid
from datetime import datetime


from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _


FILE_TYPES = {
    r'^(jpg|jpeg|png|gif|JPG|webp|svg)$': 'image',
    r'^(pdf)$': 'pdf',
    r'^(doc|docx|ppt)$': 'document',
    r'^(xlsx|xls)$': 'excel',
    r'^(mp4)$': 'video',
    r'^(mp3)$': 'audio'
}


def upload_media_path(instance, filename):
    f_name, *args, file_type = filename.split('.')
    today = str(datetime.today())[0:7]

    for regex, folder in FILE_TYPES.items():
        try:
            RegexValidator(regex).__call__(file_type)
            return '%s/%s/%s.%s' % (
                folder, today, uuid.uuid4(), file_type)
        except ValidationError as e:
            raise ValidationError(_('Invalid file type'))
