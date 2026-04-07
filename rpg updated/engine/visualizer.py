import matplotlib.pyplot as plt
import numpy as np

class DataVisualization:
    @staticmethod
    def plot_radar(character):
        labels = ['Strength', 'Intelligence', 'Wisdom', 'Charisma']
        stats = character.attributes
        
        # Calculate angles for radar
        angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
        stats = stats + stats[:1]
        angles = angles + angles[:1]

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        ax.fill(angles, stats, color='red', alpha=0.25)
        ax.plot(angles, stats, color='red', linewidth=2)
        ax.set_yticklabels([])
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels)
        plt.title(f"Character Profile: {character.name}")
        plt.show()
