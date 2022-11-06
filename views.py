from flask import Blueprint, render_template, session, redirect
from backend import *
# import numpy as np
# import pandas as pd

views = Blueprint(__name__, "views")



@views.route("/")
def home():
    
    return render_template("index.html", total_orders_inbound = total_number_of_orders, \
                                         total_orders_this_month_inbound = total_orders_this_month, \
                                         number_of_orders_in_progress_inbound= number_of_orders_in_progress,\
                                         total_revenue_inbound = total_revenue,\
                                        #  list_of_recent_orders_inbound = recent_orders_df,\
                                         list_of_orders_by_product_inbound = list2,\
                                         update_time_inbound = update_time,\
                                         list_of_recent_orders_inbound=[recent_orders_df.to_html(classes='data', header="true",index=False)]\
                                         #titles=recent_orders_df.columns.values
                           )