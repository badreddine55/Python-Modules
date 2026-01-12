#!/usr/bin/env python3

"""
Garden Management System - OOP demonstration with inheritance,
nested classes, and different method types.
"""


class Plant:
    """Basic plant with name, height, and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Create a plant with name, height (cm), and age (days)."""
        self.name = name
        self.height = height
        self.Age = age

    def grow(self) -> None:
        """Increase height by 1cm."""
        self.height += 1

    def display_info(self, ending='\n') -> None:
        """Print plant information."""
        print(f'- {self.name}: {self.height}cm', end=ending)


class FloweringPlant(Plant):
    """Plant with flowers and color."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Create a flowering plant with color."""
        super().__init__(name, height, age)
        self.color = color
        self.blooming = False

    def display_info(self, ending='\n') -> None:
        """Print plant info with color."""
        super().display_info('')
        print(f', {self.color} flowers (blooming)', end=ending)


class PrizeFlower(FloweringPlant):
    """Special flower with competition points."""

    def __init__(self, name: str, height: int, age: int, color: str,
                 prize_points: int) -> None:
        """Create a prize flower with points."""
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def display_info(self, ending='\n') -> None:
        """Print flower info with prize points."""
        super().display_info('')
        print(f', Prize points: {self.prize_points}', end=ending)


class GardenManager:
    """Manages a garden with plants and calculates statistics."""

    total_gardens = 0

    def __init__(self, name: str) -> None:
        """Create a garden for the owner."""
        self.name = name
        self.plants = []

    @classmethod
    def add_garden(cls):
        """Count total gardens created."""
        cls.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to this garden."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all(self) -> None:
        """Make all plants grow by 1cm."""
        print(f"{self.name} is helping all plants grow...")
        for p in self.plants:
            p.grow()
            print(f"{p.name} grew 1cm")

    def generate_report(self) -> None:
        """Show garden report with statistics."""
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.display_info()

        stats = self.GardenStats(self.plants)
        print()
        print(f"Plants added: {stats.total_plants}, "
              f"Total growth: {stats.total_growth}cm")
        print(f"Plant types: {stats.regular_count} regular, "
              f"{stats.flowering_count} flowering, "
              f"{stats.prize_count} prize flowers")

    def get_total_score(self) -> int:
        """Calculate total garden score."""
        stats = self.GardenStats(self.plants)
        return stats.total_score

    @staticmethod
    def validate_height(height: int) -> bool:
        """Check if height is valid (positive number)."""
        return height > 0

    class GardenStats:
        """Helper class to calculate garden statistics."""

        def __init__(self, plant_list: list) -> None:
            """Calculate stats from plant list."""
            self.plant_list = plant_list
            self.total_plants = 0
            self.total_growth = 0
            self.regular_count = 0
            self.flowering_count = 0
            self.prize_count = 0
            self.total_score = 0

            for p in self.plant_list:
                self.total_plants += 1
                self.total_growth += 1
                if p.__class__.__name__ == PrizeFlower.__name__:
                    self.prize_count += 1
                    self.total_score += p.height
                    self.total_score += 15
                if p.__class__.__name__ == FloweringPlant.__name__:
                    self.total_score += p.height
                    self.total_score += 15
                    self.flowering_count += 1
                if p.__class__.__name__ == Plant.__name__:
                    self.total_score += p.height
                    self.total_score += 10
                    self.regular_count += 1


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print()

    # Create plant objects
    oak = Plant("Oak Tree", 100, 365)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 60, "yellow", 10)

    # Create gardens
    alice = GardenManager("Alice")
    GardenManager.add_garden()
    bob = GardenManager("Bob")
    GardenManager.add_garden()

    # Add plants to Alice's garden
    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    # Add plants to Bob's garden
    bob.add_plant(Plant("chajra", 27, 200))
    bob.add_plant(FloweringPlant("wrda", 40, 45, "pink"))

    print()

    # Make Alice's plants grow
    alice.grow_all()

    print()

    # Generate Alice's report
    alice.generate_report()

    print()

    # Test static method
    print(f"Height validation test: {GardenManager.validate_height(25)}")

    # Display garden scores
    print(f"Garden scores - {alice.name}: {alice.get_total_score()}, "
          f"{bob.name}: {bob.get_total_score()}")

    # Display total gardens using class variable
    print(f"Total gardens managed: {GardenManager.total_gardens}")
