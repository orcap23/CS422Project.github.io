#file_upload/forms.py
from django import forms
from .models import File

class FileUploadForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    upload_method = forms.CharField(label="Upload Method", max_length=20,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_file(self):
        file = self.cleaned_data['file']
        ext = file.name.split('.')[-1].lower()
        if ext not in ["txt", "csv", "xlsx"]:
            raise forms.ValidationError("Only txt, csv and xlsx files are allowed.")
        # return cleaned data is very important.
        return file
