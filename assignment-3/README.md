# Assignment 3

## Task

This assignment is about solving a document retrieval problem.
The task involves the following four main steps:

  1. Index the document collection using Elasticsearch.
    - See [this document](../Elasticsearch.md) for help on Elasticsearch.
  2. Perform a baseline retrieval using the BM25 retrieval model (default setting in Elasticsearch) and evaluate its performance.
    - Return the top 100 documents for each query and measure Mean Average Precision (MAP).
  3. Implement the Mixture of Language Models approach with two fields (title and content). Find the field weights, smoothing method, and smoothing parameter that yield the best performance.
    - You need to reach a min. MAP score of XX in order to pass this assignment.
    - Submit your best ranking on kaggle.
    - The best performing team (each team member) will get 5 bonus points at the final exam.
  4. Write a report.
    - Present a results table with Mean Average Precision scores for baseline BM25 and you MLM models.
    - Explain how did you choose the LM field weights and smoothing configuration.
    - Make a plot showing which queries were improved and which were hurt when moving from BM25 to MLM.
    - The report should be max 2 (A4) pages long, written in English, and in pdf format.

You may use any programming language/environment of your choice, but you are required to submit the complete source code that produced your output.


## Data

### Document collection

The AQUAINT document collection consists of newswire text data in English, drawn from three sources: the Xinhua News Service (`xie`), the New York Times News Service (`nyt`), and the Associated Press Worldstream News Service (`apw`). It has been used in official benchmark evaluations conducted by National Institute of Standards and Technology (NIST).

The text data are separated into directories by source (`apw`, `nyt`, `xie`); within each source, data files are subdivided by year, and within each year, there is one file per date of collection. Each file contains a stream of SGML-tagged text, i.e., blocks of text bounded by <DOC> and </DOC> tags.

The collection is 1.1GB compressed and can be dowloaded from here: http://www.ux.uis.no/~balog/dat630/aquaint.zip

You are requested to delete the collection after this assignment.


### Queries


### Relevance judgments


### Output file format

For each input query, you need to output a ranked list of up to 100 documents, in the following format:

```
TBA
```

## Code

A utility class and some sample code for indexing and retrieval will be provided in Python.


## Submission

  * Each team must **sign up** before the deadline here: TBA
    - A team can be 2 or 3 people. Single-person teams are also possible (even though not recommended).
    - It is possible to form different teams for each assignment.
  * **Submit your predictions at kaggle**: TBA
    - Use the same team name you used on the sign-up form.
    - Submissions are only allowed from uis.no email addresses.
    - This platform provides online evaluation and a real-time leaderboard.
  * **Send your report, output file, and source code in email** to the student assistant Darío Garigliotti <dario.garigliotti@uis.no>
    - The subject of the email should be `[DAT630] {teamname} Assignment 3`
    - The output file should be called `{teamname.out}` and should be zip-ed. This should be the exact same file (i.e., your final solution) that was submitted on kaggle.com
    - The code should be zip-ed and contain a short README file explaining instructions on how to run it. Running this code should produce the exact same output that you attached to the email.
    - The report should be max 2 pages (A4) and in pdf format.
  * The deadline for submitting all files is **2 Nov, 16:00**.
  * Late submissions will not be allowed!


## FAQ

  - **Is it possible to submit results multiple times on kaggle?**
  Yes, but only twice a day. Only the best performing one will be considered.
  - **Is it obligatory to submit results on kaggle?**
  Yes. This way you can check if you passed the required threshold.
  - **Should I use my uis.no address on kaggle?** Yes, as the competition is restricted to people with an uis.no address. Contact the lecturer if you're following this course but you don't have an uis.no email address.
  - **What resources can be used?**
  Everything can be used. It is OK to look at online tutorials and examples, and to re-use them, but you will need to be able to explain every line of code you submit.
  - **Any advice on which programming language to use?** We are using Python (v3.5) during the practical sessions in the course, so Python is a good choice (but it is merely and advice, not a requirement).
  - **Should each member of the team write a separate report?** No, there is a single report from the team.
  - **Is it possible to get a deadline extension?**
  No. Don't even ask.
  - **Can I take the exam if I fail to complete this assignment?**
  No. So you better take it seriously.