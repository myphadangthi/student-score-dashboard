# BƯỚC 8 
from io import BytesIO
import matplotlib
matplotlib.use("Agg")  # Backend không giao diện, bắt buộc dùng cho server
import matplotlib.pyplot as plt
import seaborn as sns


# Biểu đồ tĩnh Seaborn
def distribution_png(df):
    fig, ax = plt.subplots(figsize=(8, 4.5))
    sns.histplot(data=df, x="total_score", bins=10, kde=True, color="#b456a6", ax=ax)
    ax.set(title="Phan phoi diem tong ket", xlabel="Diem tong ket", ylabel="So sinh vien")
    fig.tight_layout()
    
    buffer = BytesIO()
    fig.savefig(buffer, format="png", dpi=140)
    plt.close(fig)  # Bắt buộc đóng figure để giải phóng bộ nhớ
    buffer.seek(0)
    return buffer
# BƯỚC 9 
# Biểu đồ tương tác Plotly
import plotly.express as px

def classification_chart_html(df):
    counts = (
        df["classification"].astype(str)
        .value_counts()
        .rename_axis("classification")
        .reset_index(name="count")
    )
    fig = px.bar(
        counts, x="classification", y="count",
        color="classification",
        title="So sinh vien theo xep loai"
    )
    fig.update_layout(showlegend=False, height=420)
    return fig.to_html(full_html=False, include_plotlyjs="cdn"
    )
