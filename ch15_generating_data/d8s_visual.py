from die import Die
import plotly.express as px

# Instantiate 2d8
d8_1 = Die(8)
d8_2 = Die(8)

# Make 1,000 rolls
results = [d8_1.roll() + d8_2.roll() for _ in range(1_000)]

# Analyze the results
max_results = d8_1.num_sides + d8_2.num_sides
possible_results = range(1, max_results + 1)
frequencies = [results.count(value) for value in possible_results]

# Visualize the Results
title = "Results of Rolling 2 D8 1,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)

# Write results as html
fig.write_html("./figures/dice_visual_2d8.html")
