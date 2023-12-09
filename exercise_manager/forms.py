from django import forms
from .models import Workout, Exercise, Comment


class WorkoutForm(forms.ModelForm):
    name = forms.CharField(label='Name', required=True, widget=forms.TextInput(attrs={'placeholder': 'Название', 'class':'creat-workout-input'}))
    overview = forms.CharField(label='Overview', required=True,
                                widget=forms.Textarea(attrs={'placeholder': 'Краткое описание', 'class':'creat-workout-input',
                                                             'type':'textarea', 'rows':'3', 'maxlength':'260'}))
    detailed_description = forms.CharField(label='Detailed description', required=True,
                                widget=forms.Textarea(attrs={'placeholder': 'Подробное описание', 'class':'creat-workout-input',
                                                             'type':'textarea', 'rows':'9', 'maxlength':'600'}))
    preview = forms.ImageField(label='Preview', required=True,
                               widget=forms.FileInput(attrs={'placeholder': 'Preview', 'class':'preview-input', 'id':'id_preview',
                                                             'onchange': "handleFileChange('id_preview', 'chooseFileBtn')"}))
    level = forms.ChoiceField(choices=Workout.workoutLevels, label='Workout Level', widget=forms.Select(attrs={'class':'select-tr-level'}))

    class Meta:
        model = Workout
        fields = ['name', 'overview', 'detailed_description', 'preview', 'level']

class ExercisesForm(forms.ModelForm):
    name = forms.CharField(label='Name', required=True, widget=forms.TextInput(attrs={'placeholder': 'Name', 'class':'ex_input'}))
    description = forms.CharField(label='Description', required=True, widget=forms.TextInput(attrs={'placeholder': 'Description', 'class':'ex_input'}))
    startPositionImage = forms.ImageField(label='start Position Image', required=True,
                                          widget=forms.FileInput(attrs={'placeholder': 'start Position Image',
                                                                        'id': "id_preview1", 'class':'preview-input',
                                                                        'onchange': "handleFileChange('id_preview1', 'chooseFileBtn1')"}))
    finalPositionImage = forms.ImageField(label='final Position Image', required=True,
                                          widget=forms.FileInput(attrs={'placeholder': 'final Position Image',
                                                                        'id': "id_preview2", 'class':'preview-input',
                                                                        'onchange': "handleFileChange('id_preview2', 'chooseFileBtn2')"}))

    class Meta:
        model = Exercise
        fields = ['name', 'description', 'startPositionImage', 'finalPositionImage']

class CommentForm(forms.ModelForm):
    text = forms.CharField(label='Comment', required=False, widget=forms.TextInput(attrs={'placeholder': 'Comment', 'class':'forms'}))
    
    class Meta:
        model = Comment
        fields = ['text']
        