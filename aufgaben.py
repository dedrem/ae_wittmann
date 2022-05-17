from dataclasses import dataclass

# car
@dataclass
class car:
    color: str
    construction_year: int
    km_driven: float
    seats: int
    model: str

    def honk(self) -> None:
        print("möööööp")

    def drive(self, km: float) -> None:
        print(f"{km} km driven")
        self.km_driven += km

    def park(self) -> None:
        print("parkingspot found")

    def get_km_driven(self) -> None:
        print(f"current km driven: {self.km_driven} km")

ferraroSportiglio: car = car(color="red", construction_year=1337, km_driven=14300, seats=69, model="sportycar")
ferraroSportiglio.honk()
ferraroSportiglio.get_km_driven()
ferraroSportiglio.drive(5)
ferraroSportiglio.get_km_driven()
ferraroSportiglio.park()