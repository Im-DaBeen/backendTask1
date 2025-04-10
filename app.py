from flask import Flask, render_template, request, redirect, url_for, flash
import os
from dotenv import load_dotenv
from models import Book

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev')

# Temporary storage for books
books = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exam1', methods=['GET', 'POST'])
def exam1():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        author = request.form.get('author', '').strip()
        category = request.form.get('category', '')
        
        # Validation
        if not title:
            flash('제목을 입력해주세요.', 'error')
            return render_template('exam1.html')
        if not author:
            flash('저자를 입력해주세요.', 'error')
            return render_template('exam1.html')
        if not category:
            flash('카테고리를 선택해주세요.', 'error')
            return render_template('exam1.html')
            
        # Store the book
        books.append({
            'title': title,
            'author': author,
            'category': category
        })
        
        return redirect(url_for('list_books'))
    
    return render_template('exam1.html')

@app.route('/exam2', methods=['GET', 'POST'])
def exam2():
    book = Book(
        title="기본 제목",
        author="기본 저자",
        category_id=1,
        price=10000
    )
    
    if request.method == 'POST':
        book.title = request.form.get('title', '').strip()
        book.author = request.form.get('author', '').strip()
        book.category_id = int(request.form.get('category_id', 0))
        book.price = int(request.form.get('price', 0))
        
        # Print to console
        print(f"Book saved: {book.__dict__}")
        
        flash('책이 저장되었습니다.', 'success')
    
    return render_template('exam2.html', book=book)

@app.route('/list')
def list_books():
    return render_template('list.html', books=books)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8088))
    app.run(host='0.0.0.0', port=port, debug=True) 