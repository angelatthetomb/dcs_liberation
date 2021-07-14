from __future__ import annotations

from dataclasses import dataclass

from game.commander.tasks.packageplanningtask import PackagePlanningTask
from game.commander.theaterstate import TheaterState
from game.data.doctrine import Doctrine
from game.theater.theatergroundobject import VehicleGroupGroundObject
from gen.flights.flight import FlightType


@dataclass
class PlanBai(PackagePlanningTask[VehicleGroupGroundObject]):
    def preconditions_met(self, state: TheaterState) -> bool:
        if not super().preconditions_met(state):
            return False
        if not state.has_garrison(self.target):
            return False
        return self.target_area_preconditions_met(state)

    def apply_effects(self, state: TheaterState) -> None:
        state.eliminate_garrison(self.target)

    def propose_flights(self, doctrine: Doctrine) -> None:
        self.propose_flight(FlightType.BAI, 2, doctrine.mission_ranges.offensive)
        self.propose_common_escorts(doctrine)