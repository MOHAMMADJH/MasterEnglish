import os

from django.core.exceptions import ValidationError


def validate_is_audio(file):
    global file_is_sported
    try:
        print("hi $$$$$$$$$$$$$$$$$$$")
        print(file)
        file_name = str(file)
        file_ext = file_name[-4:]
        print(file_name)
        print("file_ext:" + file_ext)
        if file_ext == '.wav':
            print(file_ext == '.wav')
            print(file_ext)
            print("file_ext:" + file_ext)
            first_file_check = True
        else:
            print("Unsupported file type.")
            # raise ValidationError('Unsupported file type.')
            first_file_check = False

    except Exception as e:
        first_file_check = False

    #
    if not first_file_check:
        raise ValidationError('Unsupported file type.')
    valid_file_extensions = ['.wav']
    ext = os.path.splitext(file.name)[1]
    if ext.lower() not in valid_file_extensions:
        raise ValidationError('Unacceptable file extension.')

def validate_is_video(file):
    global file_is_sported
    try:

        file_name = str(file)
        file_ext = file_name[-4:]

        if file_ext == '.mp4':

            first_file_check = True
        else:
            print("Unsupported file type.")
            # raise ValidationError('Unsupported file type.')
            first_file_check = False

    except Exception as e:
        first_file_check = False

    #
    if not first_file_check:
        raise ValidationError('Unsupported file type.')
    valid_file_extensions = ['.mp4']
    ext = os.path.splitext(file.name)[1]
    if ext.lower() not in valid_file_extensions:
        raise ValidationError('Unacceptable file extension.')