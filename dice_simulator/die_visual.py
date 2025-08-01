import plotly.express as px

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die(10)

# Roll the dice and store results in a list.
results = []
for rull_number in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
title = "Results of Rolling a D6 and a D10 die 50,000 Times"
labels = {'x': 'Results', 'y': 'Frequency of Results'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customer chart.
fig.update_layout(xaxis_dtick=1)

fig.write_html('dice_visual_d6d10.html')