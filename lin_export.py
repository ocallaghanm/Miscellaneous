from qgis.core import QgsProject, QgsStyle

# === USER SETTINGS ===
style_path = r"/mnt/sda1/Documents/UNIL/CDD/geomorph_lin_style.db"
layer_name = "gm_lin"
# ======================

# Load the existing style DB
style = QgsStyle()
if style.load(style_path):
    print(f"Loaded style DB: {style_path}")
else:
    raise Exception("Failed to load the style database")

# Access the layer and renderer
layer = QgsProject.instance().mapLayersByName(layer_name)[0]
renderer = layer.renderer()

for i, rule in enumerate(renderer.rootRule().children()):
    symbol = rule.symbol()
    if not symbol:
        continue
    rule_label = rule.label()
    style.addSymbol(rule_label, symbol, True)
    style.saveSymbol(rule_label, symbol, True, ['lin'])