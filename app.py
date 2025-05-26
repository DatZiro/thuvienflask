from flask import Flask, render_template, request, redirect

app = Flask(__name__)
books = []

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        books.append({'title': title, 'author': author, 'read': False})
        return redirect('/')
    return render_template('add_book.html')

@app.route('/delete/<int:index>')
def delete_book(index):
    if 0 <= index < len(books):
        books.pop(index)
    return redirect('/')

@app.route('/toggle/<int:index>')
def toggle_read(index):
    if 0 <= index < len(books):
        books[index]['read'] = not books[index]['read']
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
