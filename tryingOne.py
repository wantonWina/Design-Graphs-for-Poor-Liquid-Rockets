import datetime
import rocketpy

from math import exp
from rocketpy import Environment, Rocket, Flight #for the rocket portion of rocket
#from rocketpy import Fluid, LiquidMotor, CylindricalTank, MassFlowRateBasedTank #for liquid rocket engine portion of rocket

from rocketpy.motors import GenericMotor # no need for fancy motor


thrustToWeight = 5     #ratio of thrust to weight
specificImpulse = 256    #seconds
totalWeight = 50 #kilograms
deadPercent = 0.5 #ratio of dead over total
diameter = rocketpy.units.conversion_factor("in", "m") * 8 #diameter from in to m



env = Environment(latitude=32.990254, longitude=-106.974998, elevation=1400)
gravityAtZero = env.gravity(0)

print("1")

tomorrow = datetime.date.today() + datetime.timedelta(days=1)
print("2")

env.set_date(
    (tomorrow.year, tomorrow.month, tomorrow.day, 12)
)  # Hour given in UTC time
print("3")
env.set_atmospheric_model(type="Forecast", file="GFS")
print("4")


# Define the motor parameters
motor = GenericMotor(
  thrust_source = "../data/motors/cesaroni/Cesaroni_M1670.eng",
  burn_time = (totalWeight * (1-deadPercent)) / (totalWeight * thrustToWeight / (specificImpulse * gravityAtZero)),
  chamber_radius = 33 / 100,
  chamber_height = 600 / 1000,
  chamber_position = 0,
  propellant_initial_mass = 2.5,
  nozzle_radius = 33 / 1000,
  dry_mass = 1.815,
  center_of_dry_mass_position = 0,
  dry_inertia = (0.125, 0.125, 0.002),
  nozzle_position = 0,
  reshape_thrust_curve = False,
  interpolation_method = "linear",
  coordinate_system_orientation = "nozzle_to_combustion_chamber",
)





"""
# Define fluids
oxidizer_liq = Fluid(name="N2O_l", density=1220)
oxidizer_gas = Fluid(name="N2O_g", density=1.9277)
fuel_liq = Fluid(name="ethanol_l", density=789)
fuel_gas = Fluid(name="ethanol_g", density=1.59)

# Define tanks geometry
tanks_shape = CylindricalTank(radius = 0.1, height = 1.2, spherical_caps = True)

# Define tanks
oxidizer_tank = MassFlowRateBasedTank(
    name="oxidizer tank",
    geometry=tanks_shape,
    flux_time=5,
    initial_liquid_mass=32,
    initial_gas_mass=0.01,
    liquid_mass_flow_rate_in=0,
    liquid_mass_flow_rate_out=lambda t: 32 / 3 * exp(-0.25 * t),
    gas_mass_flow_rate_in=0,
    gas_mass_flow_rate_out=0,
    liquid=oxidizer_liq,
    gas=oxidizer_gas,
)

fuel_tank = MassFlowRateBasedTank(
    name="fuel tank",
    geometry=tanks_shape,
    flux_time=5,
    initial_liquid_mass=21,
    initial_gas_mass=0.01,
    liquid_mass_flow_rate_in=0,
    liquid_mass_flow_rate_out=lambda t: 21 / 3 * exp(-0.25 * t),
    gas_mass_flow_rate_in=0,
    gas_mass_flow_rate_out=lambda t: 0.01 / 3 * exp(-0.25 * t),
    liquid=fuel_liq,
    gas=fuel_gas,
)

oxidizer_tank.info()
#fuel_tank.info()

"""

