# Analyzing Java Security Topics From StackOverflow
This repository contains the scripts for extracting and analyzing posts from stackoverflow to topic models that are related to java security

<h3> Collect posts from StackOverflow</h3>
Run the folowing commands in a <code>unix</code> terminal:<br>
<code>cd ./StackOverflowGetData</code><br>
<code>scrapy crawl StackOverflowQA</code><br>
It creates a json file (<b>Q_and_A.json</b>) that contains the posts and its metadata.


<h3>Topic Modeling</h3>
The json file Q_and_A.json, contains the posts relevant to java and security posts from StackOverflow.  It comprises the questions and answers of each post, and its metadata (positive votes, favorite votes, date of posted question, number of answers, etc) so, by running the
<code>LDA_model.py</code> script we get the list of topics, the number of posts for each topic and the share metric. Also, this script provides with a matrix-like file that contains the questions (rows) by the topics (columns), the values of each cell corresponds to the probability that the topic belongs to the post (question+answers).

<h3></h3>


