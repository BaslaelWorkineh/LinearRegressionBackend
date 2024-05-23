# from flask import Blueprint, jsonify
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import io
# import base64
# import os
# from config import Config
# from matplotlib.figure import Figure

# data_visualization_bp = Blueprint('data_visualization', __name__)

# @data_visualization_bp.route("/visualizeData", methods=["GET"])
# def visualize_data():
#     data_path = Config.DATA_PATH
#     data = pd.read_csv(data_path)
#     data = data.drop(['date', 'street', 'city', 'statezip', 'country'], axis=1)

#     # Pairplot
#     pairplot_img = io.BytesIO()
#     pairplot_fig = sns.pairplot(data).fig
#     pairplot_fig.savefig(pairplot_img, format='png')
#     pairplot_img.seek(0)
#     pairplot_url = base64.b64encode(pairplot_img.getvalue()).decode('utf8')
#     plt.close(pairplot_fig)

#     # Heatmap
#     heatmap_img = io.BytesIO()
#     heatmap_fig = Figure(figsize=(10, 8))
#     ax = heatmap_fig.subplots()
#     sns.heatmap(data.corr(), annot=True, cmap='coolwarm', ax=ax)
#     heatmap_fig.savefig(heatmap_img, format='png')
#     heatmap_img.seek(0)
#     heatmap_url = base64.b64encode(heatmap_img.getvalue()).decode('utf8')
#     plt.close(heatmap_fig)

#     response = {
#         'pairplot_url': pairplot_url,
#         'heatmap_url': heatmap_url
#     }

#     return jsonify(response)

# Sending the row data and handling the visualization on the frontend

from flask import Blueprint, jsonify
import pandas as pd
import os
from config import Config

data_visualization_bp = Blueprint('data_visualization', __name__)

@data_visualization_bp.route("/visualizeData", methods=["GET"])
def visualize_data():
    data_path = Config.DATA_PATH
    data = pd.read_csv(data_path)
    data = data.drop(['date', 'street', 'city', 'statezip', 'country'], axis=1)

    response = data.to_dict(orient='records')
    return jsonify(response)

