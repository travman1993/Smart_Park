# Smart_Park
Smart Parking Infrastructure System
Smart Parking Infrastructure System
Overview

The Smart Parking Infrastructure System is a modular Python-based parking management simulator designed to replicate real-world parking technologies used in:

Residential communities
Business parking lots
Event parking systems
Parking garages and parking decks

The system simulates:

Vehicle entry and exit detection
AI license plate recognition
Driver and passenger camera systems
Lift arm gate control
Parking occupancy tracking
Timestamp tracking
Ticketless garage billing
Residential auto-access
Event traffic handling
Security monitoring
Tailgating detection

This project is designed as a learning-focused software architecture project that can evolve into a real hardware-integrated system using:

Raspberry Pi
Cameras
Ultrasonic sensors
RFID readers
OpenCV
Databases
Web dashboards
Features
Core Features
Vehicle Detection
Entry sensors
Exit sensors
Vehicle type detection
Tire timing simulation
AI Plate Recognition
OCR plate scanning simulation
Plate database matching
Resident verification
Security blacklist checks
Camera Systems
Driver-side camera
Passenger-side camera
Rear license plate camera
Lift Arm Gates
Open/close logic
Optional no-gate setups
Security-controlled access
Occupancy Tracking
Real-time parking counts
Available space calculations
Full-lot detection
Turn-around handling
Parking Garage Billing
Ticketless parking
Entry timestamps
Exit timestamps
Free grace periods
Hourly billing
Daily max rates
Security Features
Tailgating detection
Blacklisted plates
Unauthorized access alerts
Camera logging
Parking Modes
1. Residential Mode
Designed For
Apartments
Condos
HOAs
Gated communities
Features
AI resident verification
Automatic lift arm opening
Visitor tracking
Vehicle timestamp logging
Entry Logic
Vehicle approaches
Plate scanned
AI checks resident database
If resident verified:
Gate opens automatically
If not verified:
Visitor processing starts
2. Business Mode
Designed For
Office buildings
Warehouses
Employee parking
Commercial lots
Features
Optional badge system
Optional gates
Vehicle logging
Occupancy tracking
Entry Logic
Vehicle detected
Plate scanned
Badge check (optional)
Approval or denial
Gate opens if approved
3. Event Mode
Designed For
Concerts
Festivals
Sports events
Conventions
Features
Fast throughput
Vehicle counting
Occupancy management
Full-lot handling
Optional no-gate setup
Full Lot Handling

If occupancy reaches maximum:

NO ROOM AVAILABLE
PLEASE TURN AROUND
4. Parking Garage / Deck Mode
Designed For
Parking garages
Parking decks
Airports
City parking
Features
Ticketless parking
AI plate recognition
Billing engine
Time tracking
Daily/hourly pricing
Receipt generation
Billing Logic
0–30 minutes = free
Hourly rates apply after grace period
Daily maximum rates supported
System Architecture
Main Modules
File	Purpose
main.py	Master system controller
sensors.py	Vehicle sensor logic
cameras.py	Camera simulation
gates.py	Lift arm control
ai_system.py	AI and plate verification
security.py	Security and tailgating logic
billing.py	Garage billing engine
occupancy.py	Parking count tracking
database.py	Data storage and retrieval
parking_modes.py	Mode-specific logic
config.py	System settings
analytics.py	Reports and statistics
Entry Workflow
Vehicle detected
↓
Check occupancy
↓
Vehicle type calculated
↓
Capture driver image
↓
Capture passenger image
↓
Capture plate image
↓
Run OCR scan
↓
Check database
↓
Apply mode-specific rules
↓
Approve or deny vehicle
↓
Save parking session
↓
Increase occupancy
↓
Open lift arm
Exit Workflow
Exit sensor triggered
↓
Scan rear plate
↓
Find active parking session
↓
Calculate parking duration
↓
Calculate parking fee
↓
Process payment
↓
Generate receipt
↓
Decrease occupancy
↓
Open lift arm
Database Structure
Vehicle Record Example
vehicle_record = {
    "plate": "ATL4289",
    "vehicle_type": "SUV",
    "resident": True,
    "entry_timestamp": "2026-05-13 12:00",
    "driver_photo": "driver_001.jpg",
    "passenger_photo": "passenger_001.jpg"
}
Vehicle Types
Type	Sensor Timing
Motorcycle	0.2 sec
Sedan	0.6 sec
SUV	0.9 sec
Truck	1.5 sec
Semi	2.5+ sec
Occupancy Logic
Occupancy Variables
max_capacity
current_occupancy
available_spaces
Update Logic
Vehicle enters:
    occupancy += 1


Vehicle exits:
    occupancy -= 1
Gate Logic
Gate Variables
gate_enabled
lift_arm_enabled
approved_status
gate_state
Gate Rules
Approved Vehicle
Raise lift arm
Allow vehicle through
Lower lift arm
Denied Vehicle
Keep gate closed
Display turn-around message
Security Features
Tailgating Detection

Detects vehicles entering too closely behind another vehicle.

Blacklisted Plates

Checks for:

Banned vehicles
Stolen vehicles
Unauthorized access
Camera Logging

Stores:

Driver image
Passenger image
Plate image
Entry timestamps
Exit timestamps
Recommended Future Features
GUI Dashboard

Potential additions:

Live occupancy display
Camera feed simulation
Animated lift arms
Revenue dashboard
Hardware Integration

Possible hardware:

Raspberry Pi
Servo lift arms
RFID readers
Ultrasonic sensors
Real cameras
AI Expansion

Potential AI upgrades:

OpenCV OCR
Facial recognition
Vehicle make/model recognition
Predictive occupancy
Suggested Build Order
Phase 1
Startup menu
Parking modes
Occupancy tracking
Phase 2
Sensor simulation
Vehicle type detection
Gate logic
Phase 3
Camera systems
Plate OCR simulation
Database storage
Phase 4
Residential AI verification
Security logic
Tailgating detection
Phase 5
Garage billing engine
Receipt generation
Analytics system
Phase 6
GUI dashboard
Database integration
Hardware integration
Technologies Recommended
Beginner Level
Python
Dictionaries
Functions
Classes
JSON
Intermediate Level
SQLite
Tkinter
OpenCV
Flask
Advanced Level
Raspberry Pi
PostgreSQL
WebSocket dashboards
AI integrations
Learning Goals

This project teaches:

Python programming
Software architecture
Object-oriented programming
State management
Real-world infrastructure logic
Security system design
AI workflow concepts
Billing system design
Modular development
Database concepts
Final Goal

The long-term goal is to evolve this simulator into a realistic smart parking infrastructure platform capable of:

Managing multiple parking environments
Supporting AI-based access systems
Running ticketless parking garages
Tracking occupancy in real time
Integrating with physical hardware
Serving as a portfolio-level engineering project
Final Goal

The final system can evolve from a Python simulator into:

A full desktop application
A smart parking management dashboard
A Raspberry Pi gate system
A cloud-connected infrastructure platform
A portfolio-level engineering project