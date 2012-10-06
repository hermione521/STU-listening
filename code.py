# >_< coding: utf-8 >_<
import web
from web.contrib.template import render_jinja
from datetime import datetime
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *

prefix = '/listening'

urls = (
	prefix + '/',				'index',
	prefix + '/nop',			'nop',
	prefix + '/article/(\d+)',	'article',
	prefix + '/audio/(\d+)',	'audio'
)

def load_sqla(handler):
	web.ctx.orm = scoped_session(sessionmaker(bind = engine))
	try:
		return handler()
	except web.HTTPError:
		web.ctx.orm.commit()
		raise
	except:
		web.ctx.orm.rollback()
		raise
	finally:
		web.ctx.orm.commit()

app = web.application(urls, globals())
app.add_processor(load_sqla)

render = render_jinja(
	'templates',
	encoding = 'utf-8',
)

class index:
	def GET(self):
		web.header('Content-type', 'text/html')
		res = web.ctx.orm.query(BBC).all()
		lis = []
		import sys
		reload(sys)
		for i in res:
			sys.setdefaultencoding('utf8')	
			print i.title
			print type(i.title)
			lis.append([i.indexID, i.date.isoformat(), i.title.decode('latin1'), i.fileName.decode('latin1')])
		print lis
		return render.index(lis = lis)

class article:
	def GET(self, num):
		web.header('Content-type', 'text/html')
		res = web.ctx.orm.query(BBC).filter_by(indexID = num).first()
		return render.article(lis = [res.indexID, res.date.isoformat(), res.title.decode('latin1'), res.fileName.decode('latin1')])

class audio:
	def GET(self, num):
		web.header('Content-type', 'text/html')
		res = web.ctx.orm.query(BBC).filter_by(indexID = num).first()
		return render.audio(fileName = res.fileName)

class nop:
	def GET(self):
		now = datetime.now()
		return render.nop(time = now.isoformat())

if __name__ == '__main__':
	app.run()

