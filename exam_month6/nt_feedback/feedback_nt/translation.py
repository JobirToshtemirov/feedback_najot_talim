from modeltranslation.translator import TranslationOptions, register

from feedback_nt.models import FeedbackModel


@register(FeedbackModel)
class FeedbackModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
