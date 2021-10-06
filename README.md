# razer-problem

## Contents: 
- [Data Exploratory Analysis](explore-data.ipynb)
- [Data Generation Process file](generate.py)
- [Simulated data](simulated_data.csv)

## Questions
1. What is source of this data file?
   
   **Answer:** I guess it is some kind of system or program log file
   
2. What does each column represent?

   **Answer:** See below for each column:
   
   - 1st column is obvious, it represent unix timestamps
   - 2nd column represents some coded category: `{-1, 0, 1}`
      - When 2nd column is `-1`: 4th and 5th represent some integer data in the range of `0` to `43`. No idea what they represent.
      - When 2nd column is `0`: 4th,6th and 7th columns represent some coded category: `{0, 1, 2}`, and 5th column represents some integer data of range `-1` to `5`. The values of 4th,6th and 7th columns seems to determine the value of the 5th column to some extent. I guess they represent the inputs for each group. 
      - When 2nd column is `1`: 4th column represent some coded category of `{0, 1}`. I guess they represent the outputs for each group.
   - 3rd column represents some group or iteration (total 12 of them)
 
3. Why is there inconsistent number of fields per line?
  
   **Answer:**  It depends on the 2nd column `{-1, 0, 1}`, it will determine the number of fields `{5, 7, 4}` respectively.

4. What happened on 16 Oct Friday morning?

   **Answer:** No idea

5. What kind of system log needs timestamps with microseconds down to the 20th places?
   
   **Answer:** I guess it is some CPU/GPU log that requires logs with a more precise clock

6. Why different groups have different time gaps?

   **Answer:** It depends on the number of rows with 2nd column = `0`.

7. Why the last row with 2nd column = `0` to the row with 2nd column = `1` time gap is different for each group?

   **Answer:** It depends on the number of rows with 2nd column = `0` within the group. It will take longer to for the row with 2nd column = `1` to appear.
   
8. (For 2nd column = `-1`) Why are there 2 different patterns in values in 4th & 5th column for groups `0-2` and `3-11`?

    **Answer:** No idea

9. (For 2nd column = `-1`) Why is the pattern in 5th columns only differs in 1 value and cycle between `5`, `18`, and `23`?

    **Answer:** No idea
    
10. (For 2nd column = `0`) Where are there different number of rows with sizes `{5, 10, 17, 33}` for different groups?

    **Answer:** It seems the 5 is a common input to all groups, while others contain additional rows, which depends on values in 4th, 6th and 7th column.
    
11. (For 2nd column = `0`) Why the 4th column seems to be more sorted as the group/iteration increases?

    **Answer:** I guess 4th column represents some task difficulty (the lower the number the faster it completes?)

