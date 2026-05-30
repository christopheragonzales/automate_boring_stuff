from die import Die
import plotly.express as px

# Instantiate 3d6
d6_1 = Die()
d6_2 = Die()
d6_3 = Die()

# Make 1,000 rolls
results = [d6_1.roll() + d6_2.roll() + d6_3.roll() for _ in range(1_000)]

# Analyze the Results
max_results = d6_1.num_sides + d6_2.num_sides + d6_3.num_sides
possible_results = range(1, max_results + 1)
frequencies = [results.count(value) for value in possible_results]

# Visualize the Results
title = "Results of Rolling 3d6 1,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=[1, 2])

# Write the results as HTML
fig.write_html("./figures/dice_visual_3d6.html")
