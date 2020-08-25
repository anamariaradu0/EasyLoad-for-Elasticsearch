from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class CommandForm(forms.Form):
    INDEX_OPTIONS = (
        ("new", "new"),
        ("delete", "delete"),
        ("update", "update"),
    )
    ENCODING_OPTIONS = (
        ("utf-8", "utf-8"),
        ("latin-1", "latin-1"),
    )
    FORMAT_OPTIONS = (
        ("csv", "csv"),
        ("json", "json"),
    )
    bulk_size = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'How many docs to collect'}),
                                   label="Bulk size", initial=500, required=False)
    es_host = forms.CharField(label="ElasticSearch Host", initial="dummy_val", max_length=200, required=False)
    username = forms.CharField(max_length=200, required=False)
    password = forms.CharField(max_length=200, required=False)
    index = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Cluster entry point'}),
                            label="Kibana index name", max_length=200, required=True)
    changes_to_index = forms.ChoiceField(choices=INDEX_OPTIONS, required=True)
    type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type of docs to be collected'}),
                           label="Type of documents", initial="_doc", max_length=200, required=True)
    id_field = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Field name to be used as doc ID'}),
                               label="ID Field", max_length=200, required=False)
    with_retry = forms.BooleanField(label="Retry in case of error?", required=False)
    encoding = forms.ChoiceField(choices=ENCODING_OPTIONS, required=False, initial="utf-8")
    keys = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comma separated keys to pick from each doc'}),
                           label="Keys to pick from each document", max_length=200, required=False)
    file = forms.FileField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'bulk_size',
            'es_host',
            Row(
                Column('username', css_class='form-group col-md-6 mb-0'),
                Column('password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('index', css_class='form-group col-md-6 mb-0'),
                Column('changes_to_index', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('type', css_class='form-group col-md-6 mb-0'),
                Column('id_field', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('keys', css_class='form-group col-md-6 mb-0'),
                Column('encoding', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'with_retry',
            'file',
            Submit('submit', 'Create command', css_class='orange_success')
        )
