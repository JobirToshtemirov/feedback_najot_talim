from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from frequently_questions.models import FrequentlyQuestionsModel
from user_t.models import TeamUserModel
from .forms import FeedbackOfferForm, FeedbackProblemForm
from .models import FeedbackModel


def feedbacksView(request):
    problems = FeedbackModel.objects.all().filter(feedback_type='problem')
    offers = FeedbackModel.objects.all().filter(feedback_type='offer').order_by('-created_at')
    context = {
        'problems': problems,
        'offers': offers,
    }
    return render(request, 'offer.html', context)


# Home page view
def landingPageView(request):
    all_frequently_asked_questions = FrequentlyQuestionsModel.objects.all()
    team_members = TeamUserModel.objects.all()
    context = {
        'all_frequently_asked_questions': all_frequently_asked_questions,
        'team_members': team_members
    }
    return render(request, 'index.html', context)


def commentsView(request):
    return render(request, 'comment.html')


def offerFormView(request):
    if request.method == 'POST':
        print(request.POST)
        keys = request.POST.keys()
        second_key = list(keys)[4]
        form = FeedbackOfferForm(request.POST)
        if second_key == 'problemForm':
            form = FeedbackProblemForm(request.POST)
        if form.is_valid():
            if second_key == 'problemForm':
                form.cleaned_data['feedback_type'] = 'problem'
            print(form.cleaned_data)
            form.save()
            return redirect(reverse_lazy('feedbacks'))
        else:
            errors = form.errors
            return render(request, 'offer.html', {'errors': errors})
    else:
        return render(request, 'offer-form.html')
