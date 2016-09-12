# Assignment 1

## Task

This assignment is about solving a classification problem, and it has two parts:

  1. Build a decision tree classifier from the given training data set. Then, apply it on the test set and submit your predictions.
    - You need to build the decision tree classifier from scratch. (I.e., it is not allowed to use existing machine learning libraries or packages.)
    - You may use any programming language/environment of your choice, but you are required to submit the complete source code that produced your output.
    - The output (a single file with the predictions for each test instance) must be generated automatically using the decision tree approach implemented by you. Submitting predictions from any other source (Internet, another team, etc.) is considered cheating and will result in immediate disqualification (i.e., dismissal from the course).   
    - The predictions need to be submitted on kaggle.com (see below).
    - In order to pass this assignment, you need to reach an **Accuracy of at least 0.8** on the test set.
    - The best performing team (each team member) will get 5 bonus points at the final exam (which will be 100 points in total).
  2. Write a short report in which you identify the top three attributes that are used by your decision tree classifier and perform a small analysis of those attributes.
    - Explain in a short paragraph why these 3 are selected as the top attributes.
    - Include summary statistics and some visualizations for these 3 attributes.
    - The report should be max 2 (A4) pages long, written in English, and in pdf format.


## Data

The assignment uses the Adult dataset. The task is to predict, based on census data, whether the income of an individual exceeds $50K/yr.

  - Training set: `data/adult.train`. The file contains 32561 records in total. Each line corresponds to a record, with the attributes comma separated. The last attribute is the target class label: <=50K or >50K.
  - Test set: `data/adult.test`. The file contains 16281 records. It has the exact same format as `adult.train`, except the last column. I.e., the class labels are missing from the test file; your task is to predict these and output the predictions to a separate file.
  - There are 14 attributes, a mixture of categorical and continuous ones. Mind that there are missing attribute values (denoted by ?). See the `adult.txt` file under the `data` folder for further details.
  - The `eval.py` (for Python 2.7) and `eval3.py` (for Python 3.x) scripts can be used for evaluation during development (if the holdout method or cross-validation is employed).
    * The `toy_data` folder contains a toy-sized ground truth set and predictions; this is only provided to allow you to try out the evaluation script. Run `python eval.py toy_data/test.gt toy_data/test.pred` from the assignment's root folder.


### Output file format

For each record in the test data, you need to output one line with the target label (either <=50K or >50K). The output needs to be in CSV format, including a header line:
```
Id,Target
1,<=50K
2,<=50K
3,<=50K
4,<=50K
5,<=50K
6,>50K
7,<=50K
8,>50K
etc.
```  
where Id is the line number and Target is the prediction (<=50K or >50K).
Mind that the evaluation is case sensitive!

## Help

A code skeleton (written in Python) is made available [here](help/).


## Submission

  * Each team must **sign up** before the deadline here: https://goo.gl/forms/igvMBZ25Lf3kxcft2
    - A team can be 2 or 3 people. Single-person teams are also possible (even though not recommended).
    - It is possible to form different teams for each assignment.
  * **Submit your predictions at kaggle**: https://inclass.kaggle.com/c/uis-dat630-fall-2016-assignment-1
    - Use the same team name you used on the sign-up form.
    - Submissions are only allowed from uis.no email addresses.
    - This platform provides online evaluation and a real-time leaderboard.
  * **Send your report, output file, and source code in email** to the student assistant Darío Garigliotti <dario.garigliotti@uis.no>
    - The subject of the email should be `[DAT630] {teamname} Assignment 1`
    - The output file should be called `{teamname.out}` and should be zip-ed. This should be the exact same file (i.e., your final solution) that was submitted on kaggle.com
    - The code should be zip-ed and contain a short README file explaining instructions on how to run it. Running this code should produce the exact same output that you attached to the email.
    - The report should be max 2 pages (A4) and in pdf format.
  * The deadline for submitting all files is **12 Sept, 16:00**.
  * Late submissions are allowed until Saturday. With each day, the accuracy threshold is increased by 1%. That is:
    - Deliver by 13 Sept, 16:00: min. accuracy = 0.81
    - Deliver by 14 Sept, 16:00: min. accuracy = 0.82
    - Deliver by 15 Sept, 16:00: min. accuracy = 0.83
    - Deliver by 16 Sept, 16:00: min. accuracy = 0.84
    - Deliver by 17 Sept, 16:00: min. accuracy = 0.85


## FAQ

  - **Is it possible to submit results multiple times on kaggle?**
  Yes. Only the best performing one will be considered.
  - **Is it obligatory to submit results on kaggle?**
  Yes. This way you can check if you passed the Accuracy threshold.
  - **Should I use my uis.no address on kaggle?** Yes, as the competition is restricted to people with an uis.no address. Contact the lecturer if you're following this course but you don't have an uis.no email address.
  - **Does everything have to be written from the ground up?**
  For the decision tree part, yes. You are allowed to use libraries for data structures and data preprocessing though.
  - **What resources can be used?**
  Everything, except machine learning libraries and ready-made decision tree implementations. It is OK to look at online tutorials and examples, and to re-use them, but you will need to be able to explain every line of code you submit.
  - **Any advice on which programming language to use?** We will be using Python (v3.5) during the practical sessions in the course, so Python is a good choice (but it is merely and advice, not a requirement).
  - **What should I do if I'm feeling lost?**
  Try to follow these steps: 1) build a decision tree on paper by performing the steps of the algorithm manually (see the exercise and the solution from Lecture 3); 2) implement what you just did on paper and apply it on the same toy data set; 3) apply the algorithm for the assignment's data set (you will face some issues, e.g.,  missing attributes, that you'll have to deal with). You can ask for help from the student assistant at any point.
  - **Which decision tree algorithm should I implement?** It's up to you. The one we used for the exercise is [ID3](https://en.wikipedia.org/wiki/ID3_algorithm). It cannot deal with missing attributes and does not include stopping criteria or pruning; you'll have to figure out how to do that. There exist extensions to ID3, like [C4.5](https://en.wikipedia.org/wiki/C4.5_algorithm). You can look for ideas there. The recommendation is to implement ID3 and extend it as you see fit so that it works effectively on the adult dataset.
  - **How general should the implementation be?** It does not have to be general, it should work only on the adult dataset. You may hard-code attribute types and even splitting conditions for continuous attributes. You may also hard-code which attributes should be used and which are to be ignored. However, when running the code, it should produce an output file from the two input files (training and test data) without any human intervention.
  - **Should each member of the team write a separate report?** No, there is a single report from the team.
  - **Is it possible to get a deadline extension?**
  No. Don't even ask.
  - **Can I take the exam if I fail to complete this assignment?**
  No. So you better take it seriously.
