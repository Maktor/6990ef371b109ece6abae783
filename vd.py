import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_hickory_venn_diagram():

    fig, ax = plt.subplots(figsize=(10, 10))

    fig.patch.set_facecolor('#E6E6E6')
    ax.set_facecolor('#E6E6E6')

    circle_settings = [
        {'center': (0.35, 0.6), 'radius': 0.35},  # Top Left
        {'center': (0.65, 0.6), 'radius': 0.35},  # Top Right
        {'center': (0.5, 0.35), 'radius': 0.35}   # Bottom
    ]

    for circle in circle_settings:
        c = patches.Circle(
            circle['center'],
            circle['radius'],
            linewidth=6,
            edgecolor='black',
            facecolor='none'
        )
        ax.add_patch(c)

    text_elements = [
        (0.24, 0.66, 'L', 'black', 35),
        (0.20, 0.60, 'F', 'black', 35), 
        (0.15, 0.55, 'Z', 'blue', 35),
        (0.23, 0.75, 'H', 'black', 35), 

        (0.76, 0.70, 'C', 'black', 35), 
        (0.80, 0.65, 'S', 'black', 35),
        (0.77, 0.60, 'O', 'black', 35), 
        (0.73, 0.76, 'U', 'black', 35),

        (0.53, 0.10, 'α', 'black', 40),
        (0.44, 0.14, 'δ', 'black', 40), 
        (0.60, 0.20, 'ρ', 'black', 40), 
        (0.46, 0.20, 'θ', 'green', 40), 

        (0.53, 0.75, 'D', 'black', 35), 
        (0.53, 0.82, '9', 'black', 35), 
        (0.50, 0.65, 'P', 'red', 35),  
        (0.53, 0.58, 'G', 'black', 35), 

        (0.30, 0.44, 'Δ', 'black', 40), 
        (0.39, 0.33, 'Σ', 'black', 40), 
        (0.30, 0.35, 'Ξ', 'black', 40), 

        (0.70, 0.45, 'β', 'black', 40), 
        (0.65, 0.32, 'ψ', 'black', 40), 
        (0.75, 0.39, 'ξ', 'black', 40), 

        (0.50, 0.48, '?', 'black', 45) 
    ]

    for x, y, char, color, size in text_elements:
        ax.text(
            x, y, char,
            color=color,
            fontsize=size,
            ha='center',
            va='center',
            fontfamily='serif',
            fontweight='bold'
        )

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    create_hickory_venn_diagram()
