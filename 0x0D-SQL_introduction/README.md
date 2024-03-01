# 0x0F. Python - Object-relational mapping
# Python
# OOP
# SQL
# MySQL
# ORM
# SQLAlchemy

 # Project over - took place from Nov 16, 2023 3:00 PM to Nov 20, 2023 3:00 PM


 <div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <h2>Before you start…</h2>

<p><strong>Please make sure your MySQL server is in 8.0</strong> -&gt; <a href="/rltoken/paGukker_0KoG3D9FqymNQ" title="How to install MySQL 8.0 in Ubuntu 20.04" target="_blank">How to install MySQL 8.0 in Ubuntu 20.04</a></p>

<h2>Background Context</h2>

<p>In this project, you will link two amazing worlds: Databases and Python!</p>

<p>In the first part, you will use the module <code>MySQLdb</code> to connect to a MySQL database and execute your SQL queries.</p>

<p>In the second part, you will use the module <code>SQLAlchemy</code> (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM). </p>

<p>The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.</p>

<p>Without ORM:</p>

<pre><code>conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
</code></pre>

<p>With an ORM:</p>

<pre><code>engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
</code></pre>

<p>Do you see the difference? Cool, right? </p>

<p>The biggest difficulty with ORM is: The syntax!</p>

<p>Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something. </p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/a8DUOWhXpNX3TEwgyT-U8A" title="Object-relational mappers" target="_blank">Object-relational mappers</a> </li>
<li><a href="/rltoken/JtFaKjnqxudr6Hi05Us1Lw" title="mysqlclient/MySQLdb documentation" target="_blank">mysqlclient/MySQLdb documentation</a> (<em>please don’t pay attention to <code>_mysql</code></em>)</li>
<li><a href="/rltoken/TdUSYFNGbXJG1WjCEoq5FA" title="MySQLdb tutorial" target="_blank">MySQLdb tutorial</a> </li>
<li><a href="/rltoken/YyL5hsscviNH04XGW-XpfA" title="SQLAlchemy tutorial" target="_blank">SQLAlchemy tutorial</a> </li>
<li><a href="/rltoken/j9azWF2Db_2rNolTxOF3SA" title="SQLAlchemy" target="_blank">SQLAlchemy</a> </li>
<li><a href="/rltoken/0zLhY9KqKjn-zmdb7X598Q" title="mysqlclient/MySQLdb" target="_blank">mysqlclient/MySQLdb</a> </li>
<li><a href="/rltoken/pw50Bl1Bj84wksxm018dwA" title="Introduction to SQLAlchemy" target="_blank">Introduction to SQLAlchemy</a> </li>
<li><a href="/rltoken/B-xIdMtGvpus8vHxAIRrPg" title="Flask SQLAlchemy" target="_blank">Flask SQLAlchemy</a> </li>
<li><a href="/rltoken/deIzPMrfK8Ixqm-AboFHWg" title="10 common stumbling blocks for SQLAlchemy newbies" target="_blank">10 common stumbling blocks for SQLAlchemy newbies</a> </li>
<li><a href="/rltoken/dZfUNK3lJicGMK5PU0bE7Q" title="Python SQLAlchemy Cheatsheet" target="_blank">Python SQLAlchemy Cheatsheet</a> </li>
<li><a href="/rltoken/hNxBKC8lHge5XjsRO8ksHQ" title="SQLAlchemy ORM Tutorial for Python Developers" target="_blank">SQLAlchemy ORM Tutorial for Python Developers</a> (<em><strong>Warning:</strong> This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL</em>)</li>
<li><a href="/rltoken/5G_R2NmQRFqiZb84qxYERQ" title="SQLAlchemy Tutorial" target="_blank">SQLAlchemy Tutorial</a></li>
<li><a href="/rltoken/OXle6kXpmD88D0WbgbTWqg" title="Python Virtual Environments: A primer" target="_blank">Python Virtual Environments: A primer</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/vPPdh3HKg3t23YFxUqHpFg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome</li>
<li>How to connect to a MySQL database from a Python script</li>
<li>How to <code>SELECT</code> rows in a MySQL table from a Python script</li>
<li>How to <code>INSERT</code> rows in a MySQL table from a Python script </li>
<li>What ORM means</li>
<li>How to map a Python Class to a MySQL table</li>
<li>How to create a Python Virtual Environment</li>
</ul>


<h2>Requirements</h2>

<h3>General</h3>



<h2>More Info</h2>

<h3>Install and activate venv</h3>

<p>To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:</p>

<pre><code>$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
</code></pre>

<h3>Install <code>MySQLdb</code> module version <code>2.0.x</code></h3>

<p>For installing <code>MySQLdb</code>, you need to have <code>MySQL</code> installed: <a href="/rltoken/paGukker_0KoG3D9FqymNQ" title="How to install MySQL 8.0 in Ubuntu 20.04" target="_blank">How to install MySQL 8.0 in Ubuntu 20.04</a></p>

<pre><code>$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
&gt;&gt;&gt; import MySQLdb
&gt;&gt;&gt; MySQLdb.version_info 
(2, 0, 3, 'final', 0)
</code></pre>

<h3>Install <code>SQLAlchemy</code> module version <code>1.4.x</code></h3>

<pre><code>$ sudo pip3 install SQLAlchemy
...
$ python3
&gt;&gt;&gt; import sqlalchemy
&gt;&gt;&gt; sqlalchemy.__version__ 
'1.4.22'
</code></pre>

<p>Also, you can have this warning message:</p>

<pre><code>/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)  
</code></pre>

<p>You can ignore it.</p>

  </div>
</div>
