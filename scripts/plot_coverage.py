import pygal

GENOME_LENGTH = 15227

line_chart = pygal.Bar(y_title="Coverage",
                       title="Coverage at each base position",
                       height=300, width=1500,
                       truncate_label=-1,
                       show_minor_x_labels=False,
                       show_legend=False)

with open("coverage.txt", "r") as handle:
    raw_data = handle.readlines()

raw_coverage = {}
for raw_line in raw_data:
    line = raw_line.strip()
    line = line.split("\t")
    this_base_position = line[1]
    this_coverage = int(line[2])

    raw_coverage[this_base_position] = this_coverage


data = []
for i in range(0, GENOME_LENGTH):
    try:
        this_coverage = raw_coverage[str(i)]
    except KeyError:
        this_coverage = 0
    data.append(this_coverage)

line_chart.x_labels = map(str, range(0, 16500))
line_chart.x_labels_major = ['0', '2000', '4000', '6000', '8000', '10000', '12000', '14000', '16000']
line_chart.add("Coverage", data)
line_chart.render_to_png("coverage.png")
line_chart.render_to_file("coverage.svg")
