# Help

You can find a "skeleton" of the code written in Python (3.5) that builds a decision tree for the small example dataset we used at the lecture. Then, it applies the built model on unseen data. It is called a skeleton, because parts of the complete and working code have been removed; these parts are marked with #TODO. The main logic if however retained, so that you will (hopefully) find it helpful (even if you are not using Python). You may reuse this code in your own implementation.

One practical challenge in this assignment could be how to represent the decision tree. In this implementation, node objects are stored in a list (array), where each node stores pointers to parent and child nodes.

Running this code (**with the missing parts completed**) would produce the following output:
```
Build model:
[Root node] 'Outlook' == ?
  sunny [Internal node] 'Humidity' <= 80.0
    True [Leaf node] class=Yes
    False [Leaf node] class=No
  rain [Internal node] 'Windy' == ?
    false [Leaf node] class=Yes
    true [Leaf node] class=No
  overcast [Leaf node] class=Yes

Apply model:
No
Yes
Yes
```
