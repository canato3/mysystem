from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from app.forms import CustomUserCreationForm
from .models import Question
from .models import Song
import re
from html import escape

def index(request):
    return render(request, 'app/index.html')



def users_detail(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    return render(request, 'app/users_detail.html', {'user': user})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            input_username = form.cleaned_data['username']
            input_password = form.cleaned_data['password1']

            new_user = authenticate(username=input_username, password=input_password)

            if new_user is not None:

                login(request, new_user)
                return redirect('app:users_detail', pk=new_user.pk)
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/signup.html', {'form': form})

def JHstart(request):

    return render(request, 'app/JHstart.html')

def Hstart(request):

    return render(request, 'app/Hstart.html')

def JHquestion(request):
    # TODO: どの問題を出すか決める
    question_id = 2

    #　何問目か（情報がなければ1問目ってことで）
    try:
        question_seq = int(request.POST.get('question_seq'))
    except TypeError:
        question_seq = 1

    question = Question.objects.get(pk=question_id)
    song = Song.objects.get(pk=question.song.pk)

    # 問題文中の [] で囲まれた部分を <input name="answer">タグに変換
    question_string = re.sub(r'\[[^]]+\]', f'<input type="text" name="answers">', escape(question.question))

    return render(request, 'app/JHquestion.html',
                            {'song': song,
                             'question': question,
                             'question_id': question_id,
                             'question_seq': question_seq,
                             'question_string': question_string})

def Hquestion(request):
    return render(request, 'app/Hquestion.html')

def JHanswer(request):
    question_id = request.POST.get('question_id')
    question = Question.objects.get(pk=question_id)
    song = Song.objects.get(pk=question.song.pk)
    question_seq = request.POST.get('question_seq')
    # 問題ページで入力された回答のリスト
    answers = request.POST.getlist('answers')

    # TODO: １問目の解答だった場合には、まずデータベースにtestを作成する
    # TODO: 前のページから受け取った解答をデータベースに記録する

    return render(request, 'app/JHanswer.html',
                           {'song': song,
                            'question':question,
                            'question_seq': question_seq})

def Hanswer(request):
    return render(request, 'app/Hanswer.html')

# Create your views here.
