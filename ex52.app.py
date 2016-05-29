import web 
from gothonweb import map

urls (
	'/game', 'GameEngine',
	'/', 'Index',
	)

app = web.application(urls, globals())

# A little hack so that the debug works with sessions
if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.config.Session(app, store,
								 initializer = {'room': None})

	web.config._session
else:
	session = web.config._session

render = web.template.render('templates/', base="layout")


class Index(object):
	def GET(self):
		# This is used to "setup" the session with starting values 
		session.room = map.START
		web.seeother("/game")


class GameEngine(object):

	def GET(self):
		if session.room:
			return render.show_room(room=session.room) 
		else:
			# Why is there here? do I need it? 
			return render.you_died()


	def POST(self):
		form = web.input(action = None)

		# There is a bug here, can you fix it?
		if session.room and form.action:
			session.room = session.room.go(form.action)

		web.seeother("/game")

	if __name__ == "__main__":
		app.run()
