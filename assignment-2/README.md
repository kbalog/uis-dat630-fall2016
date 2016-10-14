# Assignment 2

## Task

This assignment is about solving a text classification problem.
The task involves the following four main steps:

  1. Preprocess the data.
    - Preprocess the text by performing tokenization, stopwords removal and (optionally) stemming.
  2. Implement at least two classification approaches and perform a cross-validation experiment.
    - You can implement a classifier from scratch or can use any existing machine learning library or package (e.g., [scikit-learn](http://scikit-learn.org/stable/supervised_learning.html#supervised-learning)). Both Naive Bayes and SVM should produce good results on this task.
    - The two approaches can differ in the preprocessing (e.g., with and without stemming), features (e.g., different term weightings or removing too frequent and/or infrequent words), the classification model (e.g., Naive Bayes vs. SVM), etc. You are encouraged to compare more than two approaches.
    - Use k-fold cross validation with k=5. Take on average accuracy over the 5 iterations. (Note: cross-validation is implemented in [scikit-learn](http://scikit-learn.org/stable/modules/cross_validation.html))
  3. Train a final model using all training data and apply it on the test data.
    - Submit your predictions on kaggle.
    - In order to pass this assignment, you need to reach an **Accuracy of at least 0.8** on the test set.
    - Note that you are given **only 2 attempts/day** to test your performance online (this is to avoid tuning your method on the test data).
    - The best performing team (each team member) will get 5 bonus points at the final exam.
  4. Write a report.
    - Describe your data preprocessing steps.
    - Explain the different approaches you compared and present the cross-validation results.
    - The report should be max 2 (A4) pages long, written in English, and in pdf format.

You may use any programming language/environment of your choice, but you are required to submit the complete source code that produced your output.


## Data

The dataset is based on (a subset of) the WebKB dataset and contains web pages collected from computer science departments of various universities. The pages are manually classified into four different classes: course, faculty, project, and student.

| Class | # train docs | # test docs | Total # docs |
| --- | --: | --: | --: |
| course  |  886 |   44 |  930 |
| faculty | 1090 |   34 | 1124 |
| project |  484 |   20 |  504 |
| student | 1513 |  128 | 1641 |
| Total   | 3973 |  226 | 4199 |

The training data (after uncompressing) is organized into a directory structure, one directory for each class. These directories in turn contain the webpages. Note that the pages start with a MIME-header. All files have an .html extension, but the content is not necessarily valid HTML (e.g., the `<html>`, `<head>`, or `<body>` elements are missing). Also, some of the pages do not contain useful information at all (e.g., only redirect the browser to a different location).

The test data is in a single directory. You task is to classify each of these pages into one of the four categories.


### Output file format

For each html file under test data, you need to output one line with the class label, which is one of {"course", "faculty", "project", "student"}. The output needs to be in CSV format, including a header line:
```
Id,Class
1,course
2,faculty
3,project
4,faculty
5,student
6,faculty
7,student
8,project
etc.
```  
where Id is the file name (without the .html extension).
Mind that the evaluation is case sensitive!


## Submission

  * Each team must **sign up** before the deadline here: https://goo.gl/forms/1WrTdZTRePjhDrxE3
    - A team can be 2 or 3 people. Single-person teams are also possible (even though not recommended).
    - It is possible to form different teams for each assignment.
  * **Submit your predictions at kaggle**: https://inclass.kaggle.com/c/uis-dat630-fall-2016-assignment-2
    - Use the same team name you used on the sign-up form.
    - Submissions are only allowed from uis.no email addresses.
    - This platform provides online evaluation and a real-time leaderboard.
  * **Send your report, output file, and source code in email** to the student assistant Darío Garigliotti <dario.garigliotti@uis.no>
    - The subject of the email should be `[DAT630] {teamname} Assignment 2`
    - The output file should be called `{teamname.out}` and should be zip-ed. This should be the exact same file (i.e., your final solution) that was submitted on kaggle.com
    - The code should be zip-ed and contain a short README file explaining instructions on how to run it. Running this code should produce the exact same output that you attached to the email.
    - The report should be max 2 pages (A4) and in pdf format.
  * The deadline for submitting all files is **14 Oct, 16:00**.
  * Late submissions are allowed until 22 Oct. With each day, the accuracy threshold is increased by 1%. That is:
    - Deliver by 15 Oct, 16:00: min. accuracy = 0.81
    - Deliver by 16 Oct, 16:00: min. accuracy = 0.82
    - ...
    - Deliver by 22 Oct, 16:00: min. accuracy = 0.88


## FAQ

  - **Is it possible to submit results multiple times on kaggle?**
  Yes, but only twice a day. Only the best performing one will be considered.
  - **Is it obligatory to submit results on kaggle?**
  Yes. This way you can check if you passed the Accuracy threshold.
  - **Should I use my uis.no address on kaggle?** Yes, as the competition is restricted to people with an uis.no address. Contact the lecturer if you're following this course but you don't have an uis.no email address.
  - **What resources can be used?**
  Everything can be used. It is OK to look at online tutorials and examples, and to re-use them, but you will need to be able to explain every line of code you submit.
  - **Any advice on which programming language to use?** We are using Python (v3.5) during the practical sessions in the course, so Python is a good choice (but it is merely and advice, not a requirement).
  - **Should each member of the team write a separate report?** No, there is a single report from the team.
  - **Is it possible to get a deadline extension?**
  No. Don't even ask.
  - **Can I take the exam if I fail to complete this assignment?**
  No. So you better take it seriously.
