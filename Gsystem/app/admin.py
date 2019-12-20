from django.contrib import admin
from .models import User
from .models import Test
from .models import Song
from .models import Question
from .models import History
from .models import Wordlist

admin.site.register(User)
admin.site.register(Test)
admin.site.register(Song)
admin.site.register(Question)
admin.site.register(History)
admin.site.register(Wordlist)
# Register your models here.
