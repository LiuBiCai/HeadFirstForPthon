from flask import Flask,render_template,request,escape
from vsearch import search4letters
app=Flask(__name__)

def log_request(req:'flask_resquest',res:str)->None:
	with open('vsearch.log','a') as log:
		#print(str(dir(req)),res,file=log)
		#print(req.form,file=log,end='|')
		#print(req.remote_addr,file=log,end='|')
		#print(req.user_agent,file=log,end='|')
		#print(res,file=log,end='|')
		print(req.form,req.remote_addr,req.user_agent,res,file=log,sep='|')

@app.route('/search4',methods=['POST'])
def do_search() -> 'html':
	phrase=request.form['phrase']
	letters=request.form['letters']
	title='Here are your results:'
	results=str(search4letters(phrase,letters))
	log_request(request,results)
	return render_template('results.html',
						the_phrase=phrase,
						the_letters=letters,
						the_title=title,
						the_results=results,)

@app.route('/viewlog')
def view_the_log()->str:
	with open('vsearch.log') as log:
		contents=log.read()
	#return escape(contents)
	return contents
@app.route('/')
@app.route('/entry')
def entery_page()->'html':
	return render_template('entry.html',the_title="Welcome to search4letters on the web!")

if __name__=='__main__': #aim to put on PythonAnywhere
	app.run(debug=True)
