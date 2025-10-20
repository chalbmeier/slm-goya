
from IPython.display import HTML, display
import html

def show_images(df, image_dir, columns=2, img_height=300):
    cards = []

    for i, row in df.iterrows():
        title = row["label_en"]
        year = row["inception"]
        id = row["id"]
        caption = row["caption"]
        #score = str(round(row["scores"], 2))
        src = image_dir/row["file"]
        caption = html.escape(caption)
        caption_style = ("max-heigt:200px; overflow:auto; padding:8px;")
        image_style = (
            f"width:auto; height:{img_height}px; object-fit:contain; display:block; margin-left:auto; margin-right:auto;"
        )
        card = f"""
        <div class="card">
            <img src="{src}" loading="lazy" style="{image_style}"/>
            <div style="padding:0 8px;">Title: {title}.</div> 
            <div style="padding:0 8px;">Wikidata ID: {id}</div>
            <div class="caption" style="{caption_style}">AI-generated caption:<Br>\
            {caption}</div>
        </div>
        """ 
        cards.append(card)
    
    grid_css = f"""
    <style>
        .img-grid {{
            display: grid;
            grid-template-columns: repeat({columns}, minmax(0, 1fr));
            gap: 8px;
        }}
        .card {{
            background: white;
            padding: 6px;
            color: black; 
        }}
    </style>
    """

    html_out = grid_css + f'<div class="img-grid">{"".join(cards)}</div>'
    display(HTML(html_out))

