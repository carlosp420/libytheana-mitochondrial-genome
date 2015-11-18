import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.mpl_style", "default")

df = pd.read_csv("coverage.txt", sep="\t", header=None)

d = {'col2': df[2]}
df2 = pd.DataFrame(data=d, columns=['col2'])
plt.figure()

df2.plot(kind="hist", alpha=0.5, colormap="cubehelix", bins=55)
plt.savefig("a.png")
