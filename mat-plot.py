import matplotlib.pyplot as plt
import numpy as np

# print(plt.__version__) for only when import matplotlib

# x = np.array([2005, 2018, 2021, 2027])
# y = np.array([8, 10, 11, 20])
# y1 = np.array([17,16,20,30])
# y2 = np.array([30,27,16,10])

# plt.plot(x,y, marker='o', markersize= 8, markerfacecolor = "#12e9a5", markeredgecolor ="#12e9a5",color ="#0b5490ca", linestyle ="solid", linewidth = "4")

# plot_style = dict(marker='o', markersize= 8, markerfacecolor = "#12e9a5", markeredgecolor ="#12e9a5",color ="#0b5490ca", linestyle ="solid", linewidth = "4")
# plt.plot(x,y1, **plot_style)
# plt.plot(x, y2, **{**plot_style, "color": "#e01212ca"})


# plt.title("Class Size Over the Years", fontsize=16, color="#E22929F3", fontweight='bold', family = 'arial')
# plt.xlabel("Year", fontsize = 14, color="#24E0BBF3", family = 'arial', fontweight = 'bold')
# plt.ylabel("Class Size", fontsize = 14, color="#24E0BBF3", family = 'arial', fontweight = 'bold')
# plt.xticks(x)

# plt.plot(x,y)
# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.grid(axis='x', color="#29E29BF3", linestyle='--', linewidth=0.7)

# plt.tick_params(axis= 'both', color= "#E22929F3")
# plt.show()

#=========================================================================================================
# BAR CHARTS = compare categories of data by representing each category with rectangular bars


# categories = np.array(["Grains", "Vegetables", "Proteins", "Fruits", "Dairy"])
# values = np.array([250, 150, 300, 200, 100])

# plt.bar(categories, values, color = "#7F3CD0F3", edgecolor= "#1D1616F3", width = 0.5)
# #plt.barh(categories, values, color = "#7F3CD0F3", edgecolor= "#1D1616F3", height = 0.5) # horizontal bar chart

# plt.title("FOOD CONSUMPTION", fontsize = 18, family ='sans-serif', fontweight= 'bold', color = "#1D1616F3")
# plt.xlabel("FOOD's", fontsize = 14, family ='sans-serif', fontweight= 'bold', color = "#48B58DF3")
# plt.ylabel("CONSUMPTION (in grams)", fontsize = 14, family ='sans-serif', fontweight= 'bold', color = "#48B58DF3")
# plt.tick_params(axis='both', colors="#1D1616F3")

# plt.show()


#=========================================================================================================
# PIE CHARTS = Circular chart divided into slices to show percentages of the total
# Good for visualizing distribution among categories

# Types = np.array(["Freshers", "Sophomores", "Juniors", "Seniors"])
# Counts = np.array([700, 680, 600, 490])
# colors = np.array(["#FF5733", "#33FF57", "#3357FF", "#F333FF"])

# plt.pie(Counts, labels=Types, autopct='%1.1f%%', colors = colors, explode=[0,0,0,0.1], shadow = True, startangle = 90)
# plt.title("COLLEGE DISTRIBUTION")
# plt.show()


#=========================================================================================================
# SCATTER PLOTS = Shows the relationship between two variables
#                 Helps to find a co-relation (+,-, none)
#                 EX: Study hours VS Scores

# x = np.array([0,1,1,3,4,4,5,6,7,7,8])    # Hours Studied
# y = np.array([55,65,66,70,72,75,78,80,85,87,90])   # Scores

# x1 = np.array([0,2,2,3,3,5,6,6,7,8,8])
# y1 = np.array([50,55,58,60,62,65,70,72,75,78,80])

# plt.scatter(x, y, color = "#FF33A8F3", marker='o', s=100,alpha =0.5 , edgecolor="#1D1616F3", label = "Class A")
# plt.scatter(x1, y1, color = "#33FF57F3", marker='o', s=100,alpha =0.5 , edgecolor="#1D1616F3", label = "Class B")
# plt.xlabel("Hours Studied")
# plt.ylabel("GRADES")
# plt.title("STUDY HOURS VS GRADES")
# plt.legend()

# plt.show()


#=========================================================================================================
# HISTOGRAMS = A Visual representation of the distribution of quantitative data
#              They group data into bins (intervals)
#              and count how many fall into each bin

# x = np.random.normal(loc = 80, scale = 10, size =100)   # normal = normal distribution, loc = mean, scale = std deviation, size = number of values
# x = np.clip(x, 0,100) # to limit values between 0 and 100

# plt.hist(x, bins =10, color = 'lightgreen', edgecolor = 'black')
# plt.title("HISTOGRAM")
# plt.xlabel("Value Ranges")
# plt.ylabel("Frequency")
# plt.show()


#=========================================================================================================
# SUB PLOTS = multiple plots in a single figure
# Figure = overall window or page that contains all the plots and subplots
# Subplot = individual plot within the figure

# x = np.array([1,2,3,4,5])

# figure, axes = plt.subplots(2,2)

# axes[0,0].plot(x,x*2, color = 'red')
# axes[0,0].set_title("X * 2")

# axes[0,1].bar(x,x**2, color = 'blue')
# axes[0,1].set_title("X ^ 2")

# axes[1,0].plot(x,x**3, color ='green')
# axes[1,0].set_title("X ^ 3")

# axes[1,1].plot(x,x**4,color ='orange')
# axes[1,1].set_title("X ^ 4")
# plt.tight_layout()
# plt.show()


#=========================================================================================================
# PANDAS MATPLOLIB INTEGRATION
import pandas as pd

df = pd.read_csv('Movie_data.csv', on_bad_lines='skip')

type_count = df['IMDB_Rating'].round(0).value_counts().sort_index()

# Plot
plt.barh(type_count.index, type_count.values, color="#4682B4")
plt.xlabel("Number of Movies")
plt.ylabel("IMDB Rating")
plt.title("Distribution of IMDb Ratings")
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.show()