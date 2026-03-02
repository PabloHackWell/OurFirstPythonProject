<h1>🧠 Advanced AI/ML Quiz Game</h1>

<p>A fully functional, object-oriented desktop trivia application built with Python. This project moves beyond basic console scripts by implementing a live database backend, event-driven graphical UI, and dynamic game states.</p>

<h2>✨ Features</h2>
<ul>
    <li><strong>MySQL Database Integration:</strong> Questions are not hardcoded; they are fetched dynamically from a local MySQL server.</li>
    <li><strong>Dynamic Difficulty:</strong> Implements SQL queries to pull questions based on Easy, Medium, or Hard classifications.</li>
    <li><strong>Interactive GUI:</strong> Built entirely with Tkinter, featuring real-time visual feedback for correct/incorrect answers.</li>
    <li><strong>Asynchronous Countdown Timer:</strong> A built-in 15-second active timer that automatically grades unanswered questions and resets upon progression.</li>
    <li><strong>Highly Customizable:</strong> The database architecture makes it incredibly easy to swap out the AI/ML questions for any topic you want.</li>
</ul>

<h2>🛠️ Tech Stack</h2>
<ul>
    <li><strong>Language:</strong> Python 3.x</li>
    <li><strong>Frontend:</strong> Tkinter (Python's standard GUI library)</li>
    <li><strong>Backend:</strong> MySQL Server</li>
    <li><strong>Libraries:</strong> <code>mysql-connector-python</code>, <code>python-dotenv</code></li>
</ul>

<h2>🚀 Getting Started</h2>

<p><strong>1. Install Requirements:</strong></p>
<pre><code class="language-bash">pip install mysql-connector-python python-dotenv</code></pre>

<p><strong>2. Database Setup:</strong></p>
<ul>
    <li>Ensure you have a local MySQL server running.</li>
    <li>Create a <code>.env</code> file in your root directory and add your database credentials (<code>DB_HOST</code>, <code>DB_USER</code>, <code>DB_PASSWORD</code>, <code>DB_NAME</code>).</li>
    <li>Run the included SQL script or Python setup file to generate the <code>quiz_game</code> database and populate the <code>questions</code> table.</li>
</ul>

<p><strong>3. Launch the Game:</strong></p>
<pre><code class="language-bash">python main.py</code></pre>

<hr>

<h2>🧠 System Architecture</h2>
<p>This project utilizes a clean Object-Oriented Programming (OOP) approach to separate data, logic, and the user interface:</p>
<ul>
    <li><strong><code>Question</code> Model:</strong> Handles individual trivia data points and answer validation.</li>
    <li><strong><code>QuizBrain</code> Engine:</strong> A headless manager that tracks the score, question limits, and overall game states.</li>
    <li><strong><code>QuizInterface</code>:</strong> An event-driven Tkinter class that handles all user interactions, timers, and canvas updates.</li>
</ul>

<hr>

<h2>👨‍💻 Developed By</h2>
<p><strong>Team Schattenweisheit</strong></p>
<ul>
    <li><strong>HINA</strong> (LEADER)</li>
    <li>Anuj Kumar</li>
    <li>Jatin</li>
    <li>Jiya</li>
    <li>Mitali</li>
</ul>

