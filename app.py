from flask import Flask , render_template

app = Flask(__name__)

all_posts = [
    {
        'title':'Post 1',
        'content':'aaaaaaaaaaaaaaa'
    },

     {
        'title':'Post 2',
        'content':'bbbbbbbbbbbbbbb'
    }
]


@app.route('/posts')
def posts():
    return render_template('posts.html',posts=all_posts)



if __name__ =="__main__":
    app.run(debug=True)



