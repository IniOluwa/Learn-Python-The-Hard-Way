import web 

url = (
	'/' 'Index'
	)

app = web.appliction(urls, globals())

render = we.template.render('templates/')

class Index(object):
	def GET(self):
		greeting = "Hello World"
		return render.index(greeting = greeting)


if __name__ == "__main__"
	app.run()