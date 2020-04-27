from . import *

from werkzeug.utils import secure_filename


import os
main = Blueprint('index', __name__)




@main.route('/')
def index():
   return render_template('index.html')

#
# @main.route('/register',methods=['POST'])
# def register():
#     print('注册成功')
#     form = request.form
#     u = User(form)
#     u = User.register(form)
#     return redirect(url_for('.index'))
#
# @main.route("/login", methods=['POST'])
# def login():
#     form = request.form
#     u = User.validate_login(form)
#     if u is None:
#         return redirect(url_for('.index'))
#     else:
#         session['user_id'] = u.id
#         session.permanent = True
#         return redirect(url_for('topic.index'))
#
#
# @main.route('/logout')
# def logout():
#     session.pop('user_id')
#     return redirect(url_for('topic.index'))



