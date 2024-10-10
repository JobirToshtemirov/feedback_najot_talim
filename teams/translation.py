from modeltranslation.translator import TranslationOptions, register

from teams.models import TeamsModel


@register(TeamsModel)
class FeedbackModelTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'role', 'description')
