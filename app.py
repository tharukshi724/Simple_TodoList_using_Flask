from flask import Flask , render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db = SQLAlchemy(app)

class TodoPost(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200),nullable=False)
    content = db.Column(db.Text,nullable=False)
    


    def __repr__(self):
        return 'Todo post'+ str(self.id)

all_post = [

]


@app.route('/posts', methods=['GET','POST'])
def posts():
    if request.method == 'POST':
        todo_title = request.form['title']
        todo_content = request.form['content']
        new_todo = TodoPost(title=todo_title,content=todo_content)
        db.session.add(new_todo)
        db.session.commit()
        return redirect('./posts')
    else:
        all_post = TodoPost.query.order_by(TodoPost.title).all()
        return render_template('posts.html',posts=all_post)


@app.route('/posts/delete/<int:id>')
def delete(id):
    posts = TodoPost.query.get_or_404(id)
    db.session.delete(posts)
    db.session.commit()
    return redirect('/posts')

@app.route('/posts/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    posts = TodoPost.query.get_or_404(id)
    if request.method == 'POST':
        
        posts.title =  request.form['title']
        posts.content =  request.form['content']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html',posts=posts)





if __name__ =="__main__":
    app.run(debug=True)



