# Install packages
import pandas as pd
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Blues8
import csv

# Function to visualize the word count data
def keyword_chart():

    # using pandas to access the csv
    df = pd.read_csv('output.csv')

    # removing the words with count = 1 
    df_filtered = df[df['count'] != 1]

    # data source for the bokeh plot
    source = ColumnDataSource(df_filtered)

    # creating the output file
    output_file('index.html')

    # converting the word column into a list
    keyword_list = source.data['word'].tolist()

    # plot properties
    p = figure(
        y_range=keyword_list,
        width=800,
        height=600,
        title='Keywords',
        x_axis_label='Count',
        tools="pan,box_select,zoom_in,zoom_out,save,reset"
    )

    # plot type
    p.hbar(
        y='word',
        right='count',
        left=0,
        height=0.4,
        fill_color=factor_cmap(
            'word',
            palette=Blues8,
            factors=keyword_list
        ),
        fill_alpha=0.9,
        source=source,
    )

    # hover for count
    hover = HoverTool()
    hover.tooltips = """
    <div>
        <h3>@word</h3>
        <div><strong>Count: </strong>@count</div>
    </div>
    """
    p.add_tools(hover)

    show(p)