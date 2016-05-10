# Analyzing Java Security Topics From StackOverflow
This repository contains the scripts for extracting and analyzing posts from stackoverflow to topic models that are related to java security

<h3>Collect posts from StackOverflow</h3>
Run the folowing commands in a <code>unix</code> terminal:<br>
<code>cd ./StackOverflowGetData</code><br>
<code>scrapy crawl StackOverflowQA</code><br>
It creates a json file (<b>Q_and_A.json</b>) that contains the posts and its metadata.


<h3>Topic Modeling</h3>
The json file Q_and_A.json, contains the posts relevant to java and security posts from StackOverflow.  It comprises the questions and answers of each post, and its metadata (positive votes, favorite votes, date of posted question, number of answers, etc) so, by running the
<code>LDA_model.py</code> script we get the list of topics, the number of posts for each topic and the share metric. Also, this script provides with a matrix-like file that contains the questions (rows) by the topics (columns), the values of each cell corresponds to the probability that the topic belongs to the post (question+answers).

<h3>Process topics</h3>
Get the posts and its metadata and join it to the topics probability matrix. The script <code>process.py</code> generates a file <code>TOPICS.COUNTS</code> that contains the posts information and its most probable topic (highest probability).
The file <code>TOPICS.COUNTS.2.tsv</code> is the same as the <code>TOPIC.COUNTS</code> except that it contains the topic names in the last column using the file (topics.share.csv). 

<h3>Get distributions</h3>
The R script <code>process.R</code> contains all the instructions for making the topics distributions (heatmaps) by computing the evaluation metrics and normalization.

<h3>Topics temporal distribution</h3>
The python script <code>time_profile.py</code> generates a file containing the post's submission date and last answer date
The script <code>process.R</code> also contains the instructions for making the topics-time distributions. 

<h2>Datasets</h2>
Under <code>./FILES/</code> we stored all the current files used for analyzing the StackOverflow java security posts, including a sqlite database with the posts-topics information. This database is useful for retrieving specific data.

