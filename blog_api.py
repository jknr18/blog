from flask import Flask, request
import sqlite3
import json

HOST = '0.0.0.0'
PORT = 8080
DB_FILE = "blog.db"
DEBUG_MODE = False

blog_api = Flask(__name__)

def get_all_posts():
  dbcon = sqlite3.connect(DB_FILE)
  cur = dbcon.cursor()
  query_results = []
  cur.execute("select post_id, title, body from posts")
  for row in cur:
    query_results.append({"post_id": row[0], "title":row[1], "body":row[2]})
  dbcon.close()
  return query_results

def insert_new_post(incoming_post):
  dbcon = sqlite3.connect(DB_FILE)
  cur = dbcon.cursor()
  cur.execute("INSERT INTO posts (title, body) VALUES (?,?)", incoming_post)
  dbcon.commit()
  dbcon.close()

@blog_api.route("/posts", methods = ['GET'])
def retrieve_posts():
  results = get_all_posts()
  return json.dumps(results)

@blog_api.route("/post", methods = ['POST'])
def save_post():
  try:
    new_post = request.get_json(force=True)
  except Exception as e:
    return e

  try:
    blog_title = new_post['title']
    blog_body = new_post['body']
  except KeyError:
    return "Blog post is missing Title or Body element."

  insert_new_post((blog_title, blog_body))
  return "Post Successful."

if __name__=='__main__':
    blog_api.run(host=HOST, port=PORT, debug=DEBUG_MODE)


