from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# ... (previous code)

@app.route('/remove_task/<int:task_id>')
def remove_task(task_id):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
