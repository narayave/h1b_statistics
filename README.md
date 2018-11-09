# Table of Contents
- [Problem](README.md#Problem)
- [Approach](README.md#Approach)
    - [Assumptions](README.md###Assumptions)
    - [Multithreaded](README.md###Multithreaded)
- [Run](README.md#Run)

# Problem

The problem we have been given is to be able to produce data trends on H1-B
Visas with past information. In particular, we are interested interested in
analyzing 2 trends. The first is the top 10 occupations of 'CERTIFIED'
applications. The second is the top 10 working states of 'CERTIFIED' applicants.

At a programmatic level, our challenge is to read in a CSV input file, and
produce 2 output files for the 2 trends that were previously mentioned. Results
for the former challenge should be outputted to *top_10_occupations.txt*. The
second challenge results should be outputted to *top_10_states.txt*. Each record
for these files contains either the occupation or state names, the number of the
certified applications, and the percentage of the entire set of certified
applications. Our project should be modular, so other trends can also be
monitored and collected in the future.

# Approach

My approach involves being mindful of separation of concerns. In particular, I
have 3 classes (OutputWriter, DataGatherer, FindTrend) that allow for producing
trends for occupations, states, and other potential trends. 
- OutputWriter - Used for outputting data to proper files.
- DataGatherer - Used to parse and find the appropriate data to work with.
    - There are 2 different ways to get data. The first method involves getting
    all raw data, and then processing the records to delete records without a
    specific application status. The second method involves specifying the
    application status of interest upfront, so only those records are gathered.
    Both these methods have their advantages and disadvantages. When the data is
    collected, it is stored in a list.
- FindTrends - Can be used to get results to a variety of trends from H1-B Visa
    data.
    - The data structure that lends itself to this problem is a Dictionary. It
    allows for O(1) lookup when keeping count of top occupations or states.
    Once the counts have been gathered, we find the top 10 entries and create a
    list of it. This allows for easier handling when calculating percentages,
    and outputting to a file.

The results for the occupations and states can be gathered by running the
*h1b_counting.py* script. There consists 2 functions for the two trends. They
are both very similar because they both make use of the FindTrends class to
accomplish their goal. This shows that other trends can also be gathered by making similar function calls to the 3 classes mentioned above.


### Assumptions
Trend analyses are not chained together. So, every trend is independently sought
after.

The 'SOC_NAME' field is provided by the applicant, and contains duplicates or
more specific job titles. Ideally, these titles can all be consolidated for a
common dictionary key. However, this has not been tackled in the project.


### Multithreaded
An idea that I was aware of and wanted to experiment with was making the program
multithreaded. This idealogy had potential because getting results for the
trends was independent and did not rely on each other. Based on the minimal
experimentation, it was faster to run them sequentially. However, more
experiments need to be run to determine the advantages and the right situations
to use this method.


# Run

The run.sh script can be called to run both scripts for getting the Top
Occupations and the Top States.

    python ./src/h1b_counting.py ./input/h1b_input.csv ./output/top_10_occupations.txt ./output/top_10_states.txt
