# Table of Contents
- [Problem](README.md#Problem)
- [Approach](README.md#Approach)
- [Run](README.md#Run)

# Problem

The problem we have been given is to be able to produce data trends on H1-B
Visas with past information. In particular, we are interested interested in
analyzing 2 trends. The first is the top 10 occupations of 'CERTIFIED'
applications. The second is the top 10 working states of 'CERTIFIED' applicants.

At a programmatic level, our challenge is to read in an input file, and produce
2 output files for the 2 trends that were previously mentioned. Furthermore, our
project should be modular, so other trends can also be monitored and collected
in the future.

# Approach

My approach involves being mindful of separation of concerns.

# Run

The run.sh script can be called to run both scripts for getting the Top
Occupations and the Top States.

The following calls can be made to test with a custom input file. The
'custim_input_file.csv' name needs to be modified.

    python ./src/top_occupations.py ./input/custom_input_file.csv ./output/top_10_occupations.txt
    python ./src/top_states.py ./input/custom_input_file.csv ./output/top_10_states.txt