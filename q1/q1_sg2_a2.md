# Annex C
## Code Quality Assessment Worksheet
Section: 9-Balingkilat          Score:___________

C#/Name:#25/Allaina Maxene Leyran   Date: 08/15/26
     #26/Caelyn Arabelle Maglaya
     #27/Trish Aubrey Malaca

### Instructions:
The problem: Finding the highest (Maximum) number from a given list of numbers.

| PseudoCode 1 | PseudoCode 2 |
| :--- | :--- |
| <pre>Algorithm FindMax1(numbers)<br>  max ← numbers[0]<br>  For i from 1 to length(numbers)-1<br>    If numbers[i] &gt; max Then<br>      max ← numbers[i]<br>    EndIf<br>  EndFor<br>  Return max<br>EndAlgorithm</pre> | <pre>Algorithm FindMax2(numbers)<br>  For i from 0 to length(numbers)-1<br>    bigger ← true<br>    For j from 0 to length(numbers)-1<br>      If numbers[j] &gt; numbers[i] Then<br>        bigger ← false<br>      EndIf<br>    EndFor<br>    If bigger = true Then<br>      Return numbers[i]<br>    EndIf<br>  EndFor<br>EndAlgorithm</pre> |



Questions with Checklists
1. Efficiency Which algorithm is faster when the list of numbers is very large? Why?

Checklist to guide your answer:

| PseudoCode 1 | PseudoCode 2 |
| :--- | :--- |
| [] Does the algorithm use one loop or two nested loops?<br>[] Does the algorithm repeat work unnecessarily?<br>[] Which algorithm finishes in fewer steps? | [] Does the algorithm use one loop or two nested loops?<br>[] Does the algorithm repeat work unnecessarily?<br>[] Which algorithm finishes in fewer steps? |

2. Readability

Which algorithm is easier to understand at first glance? What makes it clearer?

Checklist to guide your answer:

| PseudoCode 1 | PseudoCode 2 |
| :--- | :--- |
| [] Are variable names meaningful (e.g., max vs. bigger)?<br>[] Is the logic simple or complicated?<br>[] Are there fewer lines of code? | []  Are variable names meaningful (e.g., max vs. bigger)?<br>[] Is the logic simple or complicated?<br>[] Are there fewer lines of code? |

3. Maintainability

If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?

Checklist to guide your answer:

PseudoCode 1	PseudoCode 2
[] Is the structure straightforward?
[] Would adding new steps break the code easily?
[] Is there less chance of errors when updating?	[] Is the structure straightforward?
[] Would adding new steps break the code easily?
[] Is there less chance of errors when updating?
4. Testability

Which algorithm is easier to test with different inputs? Why?

Checklist to guide your answer:

PseudoCode 1	PseudoCode 2
[] Can you test with small lists easily?
[] Does the algorithm have fewer conditions to check?
[] Is the output predictable and clear?	[] Can you test with small lists easily?
[] Does the algorithm have fewer conditions to check?
[] Is the output predictable and clear?
5. Security

Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?

Checklist to guide your answer:

PseudoCode 1	PseudoCode 2
[] Does the algorithm check if the list is empty?
[] Does it handle invalid inputs (like letters instead of numbers)?
[] Does it avoid crashing when inputs are unusual?	[] Does the algorithm check if the list is empty?
[] Does it handle invalid inputs (like letters instead of numbers)?
[] Does it avoid crashing when inputs are unusual?
6. Final Answer

Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer


