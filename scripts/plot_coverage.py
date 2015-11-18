import pygal


hist = pygal.Histogram(y_title="Coverage",
                       title="Coverage at each base position",
                       height=300, width=1500,
                       show_legend=False)

with open("coverage.txt", "r") as handle:
    raw_data = handle.readlines()

data = []
past_position = None
for raw_line in raw_data:
    line = raw_line.strip()
    line = line.split("\t")

    this_position = int(line[1])
    if not past_position:
        past_position = this_position - 1
    this_coverage = int(line[2])

    data.append((this_coverage, past_position, this_position))

    past_position = this_position

hist.add("Coverage", data)
hist.x_labels = (
    {'label': '0', 'value': 0},
    {'label': '2000', 'value': 2000},
    {'label': '4000', 'value': 4000},
    {'label': '6000', 'value': 6000},
    {'label': '8000', 'value': 8000},
    {'label': '10000', 'value': 10000},
    {'label': '120000', 'value': 12000},
    {'label': '140000', 'value': 14000},
    {'label': '160000', 'value': 16000},
)
hist.render_to_png("coverage.png")
hist.render_to_file("coverage.svg")
