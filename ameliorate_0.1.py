
# coding: utf-8

# ### Loading Libraries

# In[222]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display
from ipywidgets import *
import seaborn as sns
import matplotlib.image as mpimg


# ### Loading Datasets

# In[52]:


df =  sns.load_dataset('iris')


# In[193]:


data = df.groupby('species').mean()
data


# # Beautiful graphs
# ### 1. Bar Graphs

# In[267]:


def bar_graphs(data):
    
    style = {'description_width': 'initial'}
    inline  = Layout(display = 'inline-flex', width = '30%', height = '25px')
    box_layout = Layout(display='flex',
                    flex_flow='row',
                    align_items='stretch',
                    width='100%')
    
    # width of the bars in bar chart
    width = widgets.FloatSlider(
        value=0.8,
        min=0.1,
        max=0.9,
        step=0.1,
        description='Bar Width:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
        style = style,
        layout = inline
    )
    
    # X-AXIS label 
    xlabel = widgets.Text(
        value='Category',
        placeholder='Your X Label',
        description='X Label:',
        disabled=False,
        style = style,
        layout = inline
    )

    # Y Axis description
    ylabel = widgets.Text(
        value='value',
        placeholder='Your Y Label',
        description='Y Label:',
        disabled=False,
        style = style,
        layout = inline
    )

    # texts in legends
    legend = widgets.Text(
        value=",".join(data.columns.values),
        placeholder='list',
        description='Legend:',
        disabled=False,
        style = style,
        layout = inline
    )
    
    # Plot Title
    title = widgets.Text(
        value='Your Title',
        placeholder='Title',
        description='Title:',
        disabled=False,
        style = style,
        layout = inline
    )

    # Image width
    img_w = widgets.IntSlider(
        value=10,
        min=1,
        max=50,
        step=1,
        description='Image width:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d',
        style = style,
        layout = inline
    )
    
    # Image Height
    img_ht = widgets.IntSlider(
        value=6,
        min=1,
        max=50,
        step=1,
        description='Image Height:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d',
        style = style,
        layout = inline
    )
    
    # Vertical space between bars and annotated text
    annot_h = widgets.FloatText(
        value=0,
        description='Annotation height: ',
        disabled=False,
        style = style,
        layout = inline
    )
    
    # Annotation values rounded values 
    annot_rnd = widgets.IntText(
        value=0,
        description='Round Annotations to: ',
        disabled=False,
        style = style,
        layout = inline
    )
    
    # legend number of columns
    leg_ncol =  widgets.IntSlider(
        value=len(data.columns),
        min=1,
        max=len(data.columns),
        step=1,
        description='Legend Columns:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d',
        style = style,
        layout = inline
    )
    
    # legend location
    leg_loc =  widgets.IntSlider(
        value=9,
        min=0,
        max=9,
        step=1,
        description='Legend Location:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d',
        style = style,
        layout = inline
    )
    
    # toggle legend show/hide
    leg_true = widgets.ToggleButton(
        value=True,
        description='Toggle Legend',
        disabled=False,
        layout = inline
    )
    
    # toggle yticks and values
    tog_yticks = widgets.ToggleButton(
        value=True,
        description='Toggle Y Ticks',
        disabled=False,
        layout = inline
    )
    
    # Save figure button
    sv_fig = widgets.Button(
        description='Save Figure',
        disabled=False,
        button_style='success',
        tooltip='Save last generated figure to png file',
        layout = inline,
        style = style
    )
    

    @interact
    def bg(width = width, xl = xlabel, yl = ylabel, title = title, legend = legend, img_ht = img_ht, 
           img_w = img_w, annot_rnd = annot_rnd, annot_h = annot_h, leg_ncol = leg_ncol, leg_loc = leg_loc,
          leg_true = leg_true, tog_yticks = tog_yticks):
        
        # plot
        k = data.plot(kind = 'bar', width = width, figsize = (img_w,img_ht))
        
        # annotations
        for i in k.patches:
            k.text(i.get_x()+i.get_width()/2, i.get_height()+annot_h, round(i.get_height(), annot_rnd), ha ='center')
        plt.xticks(rotation = 0)
        plt.xlabel(xl, size = 12)
        plt.ylabel(yl, size = 12)
        
        # legend toggle
        if leg_true:
            plt.legend(legend.split(','), bbox_to_anchor=(1., 1.02), ncol = leg_ncol, loc = leg_loc)
        else:
            plt.legend().remove()
        
        # yticks toggle
        if tog_yticks==False:
            plt.yticks([])
        
        sns.despine(left = True)
        
        plt.title(title, size = 16)
        
        # save_fig
        filename = 'bar_chart_' + '_'.join(data.index.values)[:20] + '.png'
        plt.savefig(filename, bbox_inches = 'tight')
        
        plt.show()
        
        # save figure after making changes
        display(sv_fig)
        sv_fig.on_click(mpimg.imsave(filename, mpimg.imread(filename)))


# In[269]:


bar_graphs(data)

