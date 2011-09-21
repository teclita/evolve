from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('evolve.game.views',
    url(r'^$', 'game_list', name='games'),
    url(r'^new/$', 'new_game', name='new-game'),
    url(r'^(?P<game_id>\d+)/$', 'game_detail', name='game-detail'),
)

# /1/ : Main game screen, redirects according to state: If game...
#       - is not started and not joined, join/
#       - is not started and joined, wait-start/ (link to start/ if owner)
#       - is finished, score/
#       - is in progress, and haven't played play/
#       - is in progress, and have already played wait-turn/
#       - in special turn, wait-turn/ (discard or extra turn)

