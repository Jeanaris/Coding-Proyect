from load_gmat import *

# Creating the spacecraft and its future propagation using GMAT

# Initial parameters of the spacecraft
SC = gmat.Construct("Spacecraft", "La Flaqui Monster 3000")
SC.SetField("DateFormat", "UTCGregorian")
SC.SetField("Epoch", "24 Dec 2024 12:00:00.000")
SC.SetField("CoordinateSystem", "EarthMJ2000Eq")
SC.SetField("DisplayStateType", "Cartesian")

# Initial state vector of the spacecraft (Adjust to get a desire orbit)
SC.SetField("X", 6600)
SC.SetField("Y", 0)
SC.SetField("Z", 0)
SC.SetField("VX", 0)
SC.SetField("VY", 7.8)
SC.SetField("VZ", 0)

# Spacecraft ballistic properties for the SRP model
SC.SetField("SRPArea", 2.5)
SC.SetField("Cr", 1.8)
SC.SetField("DryMass", 80)

# Force model settings
FM = gmat.Construct("ForceModel", "FM")
FM.SetField("CentralBody", "Earth")

# Creating a gravity force due to a gravity field using the JGM-3 Gravity Model
GF = gmat.Construct("GravityField", "Gravity 8x8JGM-3")
GF.SetField("BodyName","Earth")
GF.SetField("PotentialFile","../data/gravity/earth/JGM3.cof")
GF.SetField("Degree", 8)
GF.SetField("Order", 8)

# Creating a gravity force due to point masses
# Moon gravity force
MG = gmat.Construct("PointMassForce", "Moon Gravity")
MG.SetField("BodyName","Luna")
# Sun gravity force
SG = gmat.Construct("PointMassForce", "Sun Gravity")
SG.SetField("BodyName","Sun")

# Activating solar radiation pressure in our model
SRP = gmat.Construct("SolarRadiationPressure", "SRP")

# Adding all of the forces into the model
FM.AddForce(GF)
FM.AddForce(MG)
FM.AddForce(SG)
FM.AddForce(SRP)

# Creating the propagation state manager, to coordinate all the propagation 
PSM = gmat.PropagationStateManager()
PSM.SetObject(SC)
FM.SetPropStateManager(PSM)
FM.SetState(PSM.GetState())

# Initializing all the previous elements
gmat.Initialize()

# Finish force model setup:
# Map spacecraft state into the model
FM.BuildModelFromMap()
# Load physical parameters needed for the forces
FM.UpdateInitialData()

# Build the propagator 
PROP = gmat.Construct("Propagator","Prop")

# Create and assign a numerical integrator for use in the propagation
IG = gmat.Construct("PrinceDormand78", "Gator")
PROP.SetReference(IG)

# Assign the force model
PROP.SetReference(FM)

# Set some of the fields for the integration
PROP.SetField("InitialStepSize", 60.0)
PROP.SetField("Accuracy", 1.0e-12)
PROP.SetField("MinStep", 0.0)

# Initialize previous elements
gmat.Initialize()

# Setup the spacecraft that will be propagated
PROP.AddPropObject(SC)
PROP.PrepareInternals()

# Refresh the integrator reference
IG = PROP.GetPropagator()