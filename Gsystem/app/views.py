from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from app.forms import CustomUserCreationForm
from .models import Question
from .models import Song
from .models import Test
import re
from html import escape
#MYDO
import random
import sqlite3

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
    question_id = 3
    # MYDO:
    #候補1　: 1問ずつ取り出してそれをquestion_idに入れる
    #questionall = Question.objects.values_list('question_id',flat=True)
    #for i in range(5):
        #x = random.choice(questionall)
        #question_id = x

    #　何問目か（情報がなければ1問目ってことで）
    try:
        question_seq = int(request.POST.get('question_seq'))
    except TypeError:
        question_seq = 1

    question = Question.objects.get(pk=question_id)
    song = Song.objects.get(pk=question.song.pk)

    # 問題文中の [] で囲まれた部分を <input name="answer">タグに変換
    question_string = re.sub(r'\[[^]]+\]', f'<input type="text" n   ame="answers">', escape(question.question))

    return render(request, 'app/JHquestion.html',
                            {'song': song,
                             'question': question,
                             'question_id': question_id,
                             'question_seq': question_seq,
                             'question_string': question_string
                             })

def Hquestion(request):
    # TODO: どの問題を出すか決める
    question_id = 3
    # MYDO:
    #候補1　: 1問ずつ取り出してそれをquestion_idに入れる
    #questionall = Question.objects.values_list('question_id',flat=True)
    #for i in range(5):
        #x = random.choice(questionall)
        #question_id = x

    #　何問目か（情報がなければ1問目ってことで）
    try:
        question_seq = int(request.POST.get('question_seq'))
    except TypeError:
        question_seq = 1

    question = Question.objects.get(pk=question_id)
    song = Song.objects.get(pk=question.song.pk)

    # 問題文中の [] で囲まれた部分を <input name="answer">タグに変換
    question_string = re.sub(r'\[[^]]+\]', f'<input type="text" n   ame="answers">', escape(question.question))

    return render(request, 'app/Hquestion.html',
                            {'song': song,
                             'question': question,
                             'question_id': question_id,
                             'question_seq': question_seq,
                             'question_string': question_string
                             })

def JHanswer(request):
    question_id = request.POST.get('question_id')
    question = Question.objects.get(pk=question_id)
    song = Song.objects.get(pk=question.song.pk)
    question_seq = request.POST.get('question_seq')
    # 問題ページで入力された回答のリスト
    answers = request.POST.getlist('answers')

    # TODO: １問目の解答だった場合には、まずデータベースにtestを作成する
    # MYDO
    #if question_seq is 1
       #conn = sqlite3.connect('db.sqlite3')
       #c = conn.cursor()
       #sql = 'insert into Test values(?,?)'
       #c.execute(sql)

    # TODO: 前のページから受け取った解答をデータベースに記録する
    # MYDO
    #sql = 'insert into History values (?,?,?,?)'
    #c.execute(sql)

    #conn.commit()
    #conn.close()

    return render(request, 'app/JHanswer.html',
                           {'song': song,
                            'question':question,
                            'question_seq': question_seq})

def Hanswer(request):
    question_id = request.POST.get('question_id')
    question = Question.objects.get(pk=question_id)
    song = Song.objects.get(pk=question.song.pk)
    question_seq = request.POST.get('question_seq')
    # 問題ページで入力された回答のリスト
    answers = request.POST.getlist('answers')

    # TODO: １問目の解答だった場合には、まずデータベースにtestを作成する
    # MYDO
    #if question_seq is 1
       #conn = sqlite3.connect('db.sqlite3')
       #c = conn.cursor()
       #sql = 'insert into Test values(?,?)'
       #c.execute(sql)

    # TODO: 前のページから受け取った解答をデータベースに記録する
    # MYDO
    #sql = 'insert into History values (?,?,?,?)'
    #c.execute(sql)

    #conn.commit()
    #conn.close()

    return render(request, 'app/Hanswer.html',
                           {'song': song,
                            'question':question,
                            'question_seq': question_seq})

# Create your views here.
