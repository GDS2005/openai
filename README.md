<h1>My Tesis</h1>

<h2>Overview</h2>
<p>This is a simple Python-based text game where players and enemies engage in battles. The game utilizes classes and objects to manage characters, items, and scenes and the ChatGPT API to create the story of the game.</p>

<h2>Folder Structure</h2>
<pre>
game/
|-- main.py
|-- characters/
|   |-- __init__.py
|   |-- player.py
|   |-- enemy.py
|   |-- boss.py
|   |-- companion.py
|-- scenes/
|   |-- __init__.py
|   |-- scene.py
|-- utils/
|   |-- __init__.py
|   |-- function.py
|   |-- menu.py
</pre>

<h2>Usage</h2>
<p>To run the game, execute <code>main.py</code> using Python:</p>
<pre>
    python main.py
</pre>

<h2>Classes</h2>

<h3>Player</h3>
<p>The <code>Player</code> class represents the player character in the game. It has attributes for health, intelligence, strength, dexterity, and agility. Players can attack enemies and cast spells.</p>

<h3>Enemy</h3>
<p>The <code>Enemy</code> class represents the non-player characters in the game. Similar to the player, it has attributes for health, intelligence, strength, dexterity, and agility. Enemies can also attack or cast spells.</p>

<h3>Scene</h3>
<p>The <code>Scene</code> class represents different scenes or levels in the game. It has a <code>name</code> attribute and a method <code>random_location()</code> to return a random location from a list and then remove it </p>

<h2>Functions</h2>
<p>The <code>utils</code> folder contains helper functions such as <code>api_openai</code> and <code>speak()</code>.</p>

<h2>Getting Started</h2>
<ol>
    <li>Clone the repository to your local machine.</li>
    <li>Ensure you have Python installed.</li>
    <li>Use pip to install: openai, colorama and pyttsx3</li>
    <li>Run <code>main.py</code> using Python.</li>
</ol>

<h2>Contributing</h2>
<p>If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.</p>

<h2>License</h2>
<p>This project is licensed under the <a href="LICENSE">Gonzalo Sánchez</a>.</p>
