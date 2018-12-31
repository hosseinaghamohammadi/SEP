from django.shortcuts import render
from django.http import HttpResponse
from .models import WorkSeeker, Employer,




def first_page(request):
    return render(request, 'website/firstPage.html')


def sign_in(request):

    try:
        username = request.post['username']
        password = request.post['password']
        question = get_object_or_404(WorkSeeker, pk = username)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))